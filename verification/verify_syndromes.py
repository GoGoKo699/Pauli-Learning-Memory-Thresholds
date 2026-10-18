#!/usr/bin/env python3
"""Exact small-instance checks of the partial-Bell decision construction.

Run from any directory with Python 3.10+; only the standard library is used.
The checks are exhaustive for n <= 3, except that complete sample-sequence
enumeration is restricted to syndrome dimensions m <= 3.  No random sampling,
quantum simulator, external data, or network is used.  These checks verify the
GF(2) construction and finite constants, not the analytic coherent lower bound.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import ceil, comb, log
import json


def parity(value):
    return value.bit_count() & 1


def symplectic_row(label, n):
    """Pauli label bits are x_0,z_0,x_1,z_1,... ."""
    result = 0
    for site in range(n):
        pair = (label >> (2 * site)) & 3
        result |= ((pair >> 1) | ((pair & 1) << 1)) << (2 * site)
    return result


def weight(label, n):
    return sum(bool((label >> (2 * site)) & 3) for site in range(n))


def rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                break
            vector ^= pivots[pivot]
    return len(pivots)


def span_with_coordinates(rows):
    span = {0: 0}
    for index, row in enumerate(rows):
        span.update({value ^ row: coordinates | (1 << index)
                     for value, coordinates in list(span.items())})
    return span


def project(rows, vector):
    return sum(parity(row & vector) << index
               for index, row in enumerate(rows))


def settings(n, k):
    for bell_sites in combinations(range(n), k):
        paired = frozenset(bell_sites)
        local_sites = [site for site in range(n) if site not in paired]
        for local_axes in product((1, 2, 3), repeat=n-k):
            axes = dict(zip(local_sites, local_axes))
            rows = []
            for site in range(n):
                if site in paired:
                    rows.extend((1 << (2 * site), 1 << (2 * site + 1)))
                else:
                    rows.append(symplectic_row(axes[site], 1) << (2 * site))
            yield paired, axes, rows


def compatibility_probability(n, k, u):
    numerator = Fraction(0)
    for matched in range(u + 1):
        if 0 <= k-matched <= n-u:
            numerator += (Fraction(comb(u, matched) * comb(n-u, k-matched),
                                   3 ** (u-matched)))
    return numerator / comb(n, k)


def null_rank_distribution(m, length, tau):
    distribution = [Fraction(1)] + [Fraction(0)] * m
    for _ in range(length):
        next_distribution = [Fraction(0)] * (m + 1)
        for current_rank, probability in enumerate(distribution):
            stay = 1 - tau + tau * Fraction(2 ** current_rank, 2 ** m)
            next_distribution[current_rank] += probability * stay
            if current_rank < m:
                next_distribution[current_rank + 1] += probability * (1-stay)
        distribution = next_distribution
    return distribution


def main():
    counts = Counter()
    taus = (Fraction(1), Fraction(1, 2), Fraction(1, 7))
    for n in range(1, 4):
        errors = range(4 ** n)
        for k in range(n + 1):
            m = n + k
            all_settings = list(settings(n, k))
            compatible_counts = Counter()
            for paired, axes, rows in all_settings:
                counts["settings"] += 1
                assert rank(rows) == m
                span = span_with_coordinates(rows)
                syndromes = [project(rows, error) for error in errors]
                null_counts = Counter(syndromes)
                assert len(null_counts) == 2 ** m
                assert set(null_counts.values()) == {2 ** (2*n-m)}
                for tau in taus:
                    for form in range(1, 2 ** m):
                        constrained_mass = sum(
                            (1-tau if y == 0 else 0)
                            + tau * Fraction(null_counts[y], 4 ** n)
                            for y in range(2 ** m) if parity(form & y) == 0)
                        assert constrained_mass == 1 - tau/2
                        counts["weak_null_constraint_cases"] += 1
                for hidden in range(1, 4 ** n):
                    counts["projection_cases"] += 1
                    form = symplectic_row(hidden, n)
                    compatible = form in span
                    axis_compatible = all(
                        ((hidden >> (2*site)) & 3) in (0, axis)
                        for site, axis in axes.items())
                    assert compatible == axis_compatible
                    compatible_counts[hidden] += int(compatible)
                    spike_counts = Counter(
                        syndrome for error, syndrome in zip(errors, syndromes)
                        if parity(form & error) == 0)
                    assert sum(spike_counts.values()) == 4 ** n // 2
                    if compatible:
                        coordinates = span[form]
                        assert coordinates != 0
                        expected_support = {
                            y for y in range(2 ** m)
                            if parity(coordinates & y) == 0}
                        assert set(spike_counts) == expected_support
                        assert set(spike_counts.values()) == {2 ** (2*n-m)}
                        # Identity mixing preserves the exact hidden constraint.
                        for tau in taus:
                            outside_mass = sum(
                                (1-tau if y == 0 else 0)
                                + tau * Fraction(spike_counts[y], 4 ** n // 2)
                                for y in range(2 ** m)
                                if parity(coordinates & y))
                            assert outside_mass == 0
                            counts["weak_spike_constraint_cases"] += 1
                    else:
                        assert set(spike_counts) == set(range(2 ** m))
                        assert set(spike_counts.values()) == {2 ** (2*n-m-1)}
            for hidden in range(1, 4 ** n):
                u = weight(hidden, n)
                empirical = Fraction(compatible_counts[hidden], len(all_settings))
                exact = compatibility_probability(n, k, u)
                assert empirical == exact
                # An integer-power check of p_u >= 3^{-u(n-k)/n}.
                assert exact ** n * 3 ** (u*(n-k)) >= 1
                counts["compatibility_probability_cases"] += 1

    # Enumerate every vector sequence for m <= 3.  Counting by the number of
    # nonzero outcomes gives exact probabilities for every rational tau below.
    for m in range(1, 4):
        for length in range(1, m + 3):
            sequence_counts = Counter()
            for sequence in product(range(2 ** m), repeat=length):
                sequence_counts[(rank(sequence), sum(v != 0 for v in sequence))] += 1
                counts["enumerated_null_sequences"] += 1
            for tau in taus:
                p_zero = 1 - tau + tau / (2 ** m)
                p_nonzero = tau / (2 ** m)
                exact = [Fraction(0)] * (m + 1)
                for (sequence_rank, nonzero_count), multiplicity in sequence_counts.items():
                    exact[sequence_rank] += (multiplicity
                        * p_zero ** (length-nonzero_count)
                        * p_nonzero ** nonzero_count)
                assert exact == null_rank_distribution(m, length, tau)
                counts["rank_recurrence_comparisons"] += 1

    for m in range(1, 7):
        for tau in taus:
            for length in range(m + 9):
                deficient_probability = sum(null_rank_distribution(m, length, tau)[:-1])
                union_bound = (2 ** m - 1) * (1 - tau/2) ** length
                assert deficient_probability <= union_bound
                counts["exact_rank_union_bound_cases"] += 1

    # Check the published finite J,L choices, including all small w,k endpoints.
    for n in range(1, 4):
        for k in range(n + 1):
            for w in range(1, n + 1):
                compatibility = compatibility_probability(n, k, w)
                for tau in taus:
                    for delta in (Fraction(1, 3), Fraction(1, 10)):
                        resource = Fraction(w*(n-k), n)
                        blocks = ceil(3 ** float(resource) * log(2/float(delta)))
                        length = ceil((2/float(tau))
                            * ((n+k)*log(2) + log(2*blocks/float(delta))))
                        assert (1-compatibility) ** blocks <= delta/2
                        assert ((2 ** (n+k)-1) * (1-tau/2) ** length
                                <= delta/(2*blocks))
                        counts["finite_J_L_cases"] += 1

    print(json.dumps({
        "status": "passed",
        "arithmetic": "exact integers and fractions; floating point only selects finite J,L",
        "maximum_qubits": 3,
        "counts": dict(sorted(counts.items())),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
