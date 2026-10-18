"""Finite consistency checks for the coherent-memory Pauli lower bound.

Checks support normalization/transposition and the hybrid implementation;
the universal theorem relies on the analytic Holder/hypercontractive proof.
"""
from itertools import product
import json
import numpy as np

rng = np.random.default_rng(41286)
single = [np.eye(2), np.array([[0, 1], [1, 0]]),
          np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]

def paulis(n):
    out = []
    for label in product(range(4), repeat=n):
        p = np.ones((1, 1), dtype=complex)
        for digit in label:
            p = np.kron(p, single[digit])
        out.append((sum(d != 0 for d in label), p))
    return out

def trace_norm_hermitian(a):
    return float(np.abs(np.linalg.eigvalsh((a + a.conj().T) / 2)).sum())

def partial_signal(rho, p, d, r):
    z = rho.reshape(d, r, d, r)
    return np.einsum('ij,jaib->ab', p, z)

def channel(rho, p, d, r, amplitude):
    marginal = partial_signal(rho, np.eye(d), d, r)
    result = np.kron(np.eye(d) / d, marginal)
    if amplitude:
        result += amplitude * np.kron(p / d, partial_signal(rho, p, d, r))
    return result

def random_unitary(d):
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, rr = np.linalg.qr(z)
    phase = np.diag(rr)
    return q * (phase / np.abs(phase)).conj()

max_fidelity_identity = 0.0
max_holder_excess = 0.0
max_weighted_rank_excess = 0.0
max_hybrid_excess = 0.0
max_channel_norm_identity = 0.0
matrix_cases = weighted_cases = hybrid_cases = 0

for n in range(1, 5):
    d = 2**n
    pp = paulis(n)
    for k in range(n + 1):
        r = 2**k
        matrix_cases += 1
        m = rng.normal(size=(d, r)) + 1j * rng.normal(size=(d, r))
        m /= np.linalg.norm(m)
        # SVD preserves the prescribed rank and avoids square-root amplification
        # of floating-point eigenvalues that should be exactly zero.
        left, singular, _ = np.linalg.svd(m, full_matrices=False)
        sq = (left * singular) @ left.conj().T
        fidelities = np.array([trace_norm_hermitian(m.conj().T @ p @ m)
                               for _, p in pp])
        affinities = np.array([np.trace(sq @ p @ sq @ p).real for _, p in pp])
        for index, (_, p) in enumerate(pp):
            other = trace_norm_hermitian(sq @ p @ sq)
            max_fidelity_identity = max(max_fidelity_identity,
                                        abs(other - fidelities[index]))
        max_holder_excess = max(max_holder_excess,
                               float(np.max(fidelities**2 - affinities)))
        for x in (0.03, 0.2, 1.0):
            weighted_cases += 1
            weights = np.array([x**weight / (1 + 3*x)**n for weight, _ in pp])
            bound = 2**(-(n-k) * 2*x/(1+x))
            max_weighted_rank_excess = max(max_weighted_rank_excess,
                                           float(weights @ affinities - bound),
                                           float(weights @ fidelities**2 - bound))
        if n > 2:
            continue
        rho0 = np.outer(m.reshape(-1), m.reshape(-1).conj())
        controls = [random_unitary(d*r) for _ in range(3)]
        null = rho0.copy()
        cut_states = []
        for u in controls:
            null = u @ null @ u.conj().T
            cut_states.append(null.copy())
            null = channel(null, np.eye(d), d, r, 0)
        for _, p in pp[1:]:
            for a in (-0.7, 1.0):
                hybrid_cases += 1
                sig = rho0.copy()
                for u in controls:
                    sig = u @ sig @ u.conj().T
                    sig = channel(sig, p, d, r, a)
                final_td = trace_norm_hermitian(sig-null)/2
                budget = 0.0
                for cut in cut_states:
                    b = partial_signal(cut, p, d, r)
                    norm = trace_norm_hermitian(channel(cut, p, d, r, a)
                                                - channel(cut, p, d, r, 0))
                    expected = abs(a)*trace_norm_hermitian(b)
                    max_channel_norm_identity = max(max_channel_norm_identity,
                                                     abs(norm-expected))
                    budget += expected/2
                max_hybrid_excess = max(max_hybrid_excess, final_td-budget)

result = dict(matrix_cases=matrix_cases, weighted_cases=weighted_cases,
              coherent_three_query_cases=hybrid_cases,
              max_fidelity_identity_error=max_fidelity_identity,
              max_holder_excess=max_holder_excess,
              max_weighted_rank_bound_excess=max_weighted_rank_excess,
              max_hybrid_excess=max_hybrid_excess,
              max_channel_norm_identity_error=max_channel_norm_identity)
assert max_fidelity_identity < 2e-10, result
assert max_holder_excess < 2e-10, result
assert max_weighted_rank_excess < 2e-10, result
assert max_hybrid_excess < 2e-10, result
assert max_channel_norm_identity < 2e-10, result


# Fresh-experiment response bound, including nonnormal complex matrices.
max_complex_response_imaginary = 0.0
max_complex_response_excess = 0.0
max_pauli_coefficient_cap_excess = 0.0
max_parseval_error = 0.0
complex_cases = 0
for n in range(1, 5):
    d = 2**n
    pp = paulis(n)
    for k in range(n + 1):
        r = 2**k
        left = rng.normal(size=(d, r)) + 1j*rng.normal(size=(d, r))
        right = rng.normal(size=(r, d)) + 1j*rng.normal(size=(r, d))
        c = left @ right
        c /= np.linalg.norm(c)
        response = np.array([np.trace(p @ c @ p @ c.conj().T)
                             for _, p in pp])
        max_complex_response_imaginary = max(
            max_complex_response_imaginary,
            float(np.max(np.abs(response.imag))))
        q = np.array([abs(np.trace(p @ c))**2/d for _, p in pp])
        max_parseval_error = max(max_parseval_error, abs(float(q.sum())-1))
        max_pauli_coefficient_cap_excess = max(
            max_pauli_coefficient_cap_excess, float(q.max())-r/d)
        for x in (0.03, 0.2, 1.0):
            complex_cases += 1
            prior = np.array([x**weight/(1+3*x)**n for weight, _ in pp])
            bound = 2**(-(n-k)*2*x/(1+x))
            moment = float(prior @ response.real**2)
            max_complex_response_excess = max(
                max_complex_response_excess, moment-bound)
assert max_complex_response_imaginary < 2e-10
assert max_complex_response_excess < 2e-10
assert max_pauli_coefficient_cap_excess < 2e-10
assert max_parseval_error < 2e-10
result.update(
    complex_weighted_cases=complex_cases,
    max_complex_response_imaginary=max_complex_response_imaginary,
    max_complex_response_excess=max_complex_response_excess,
    max_pauli_coefficient_cap_excess=max_pauli_coefficient_cap_excess,
    max_parseval_error=max_parseval_error,
)
print(json.dumps(result, indent=2))
