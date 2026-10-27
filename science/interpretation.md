# What the memory threshold means

The relevant obstruction is access to an unknown correlation. A Pauli channel has a simple diagonal action in a known operator basis, yet its informative direction can be spread over many possible supports and axes. The memory threshold quantifies how much of that hidden direction a channel call can reveal.

## Missing reference width and Pauli support

Write $`D=n-k`$ for the deficit from a full $`n`$-qubit reference and $`R=wD/n`$. A partial-Bell probe reads both Pauli-error bits at each of its $`k`$ paired sites. At an unpaired site it reads only the commutation bit for one chosen axis. A target coefficient is usable precisely when every nonidentity factor on an unpaired site agrees with that chosen axis.

For a target of weight $`u`$, a random paired subset leaves an average of $`uD/n`$ relevant sites unpaired. Each such site contributes a factor $`1/3`$ to compatibility. The exact hypergeometric average obeys

```math
p_u\ge3^{-uD/n}.
```

This gives the constructive exponential dependence on $`R`$. The lower bound allows arbitrary entangled probes and coherent reuse, so its dependence cannot be explained merely by a weakness of these local measurements. The [weighted bounds](weighted_bounds.md) control the average signal accessible with a limited reference for every allowed input.

The resulting polynomial frontier is attained up to exponential constants. It does not identify the optimal constant in the exponent.

## Distinct asymptotic regimes

The frontier compares a sequence of problems as $`n`$ grows. Polynomial query cost means that some constant $`C`$, independent of $`n`$, bounds the required calls by $`n^C`$ for sufficiently large $`n`$. A lower bound limits every allowed learner; an upper bound gives a protocol that achieves the stated cost. Here the two bounds have different exponential constants but agree on which parameter sequences admit polynomial cost. Changing the fixed base of the logarithm does not change this frontier.

At fixed learning accuracy and confidence:

| Maximum weight | Required deficit for polynomial calls | Consequence |
|---|---|---|
| $`w=O(\log n)`$ | Every $`0\le D\le n`$ is allowed. | No reference qubits are necessary for polynomial query complexity. |
| $`w=(\log n)^2`$ | $`D=O(n/\log n)`$ | The fraction of missing reference qubits must vanish. |
| $`w=\sqrt n`$ | $`D=O(\sqrt n\log n)`$ | A sublinear correlation support can still require nearly $`n`$ reference qubits. |
| $`w=\Theta(n)`$ | $`D=O(\log n)`$ | Only a logarithmic deficit from a full reference is allowed. |

For $`w=n/4`$ and $`k=0.9n`$, the coherent theorem gives an exponential factor at least $`2^{n/220}`$, while the fresh-experiment theorem gives $`2^{n/110}`$. The earlier small-weight expression proportional to $`2^{-k}3^w`$ does not show exponential growth in this regime. This is a comparison of evaluated bounds, not a claim that the exact optimal exponent is known. The precise predecessor and its access model are discussed in [related work](../references/RELATED_WORK.md#kimoh2026).

## Why coherent reuse does not remove the obstruction

In a real adaptive execution, the current state can depend on the hidden Pauli. The proof therefore does not apply a fixed-prior estimate to an arbitrary posterior state.

Instead, it compares neighboring mathematical executions whose entire common prefix uses the null channel. The state immediately before their differing call is then independent of the hidden index. The bounded-width signal estimate applies at that cut. Their common suffix may contain more channel calls, arbitrary coherent controls and feedback; for a fixed hidden index it is a CPTP map and cannot increase trace distance.

Adding these changes over all calls yields the coherent lower bound. Long coherent blocks may reduce the number of terminal measurements, but every invocation in those blocks remains charged. The distinction between measurement count and query count is already central to [Chen–Gong](../references/RELATED_WORK.md#chengong2025).

The apparatus may retain all $`n+k`$ qubits between invocations. The constraint is the total accessible quantum width when an invocation occurs, rather than a rule that some specially named ancillary register must be fresh.

## One retained classical correlation is enough

At $`\tau=1`$, the positive-spike channel has a direct measure-and-prepare form. With $`\Pi_\pm=(I\pm P_e)/2`$,

```math
\Lambda_e(X)
=\sum_{s=\pm1}\mathrm{Tr}(\Pi_sX)\frac{2\Pi_s}{d}.
```

It measures one Pauli parity and replaces the input by the maximally mixed state in the corresponding eigenspace. This channel is entanglement breaking, even though a learner's reference entanglement can substantially reduce the effort needed to discover its hidden preserved correlation.

Equivalently, its Pauli errors are uniform over the commuting hyperplane $`[e,v]=0`$. Its classical specification uses $`O(n)`$ bits. Given that specification, an error sample can be generated with $`O(n)`$ bit operations by imposing one linear parity constraint on uniformly sampled bits. The alternative family therefore does not need an exponentially long channel description.

The [decision algorithm](correlation_detection.md) asks only whether a hidden correlation exists under this promise. It detects a linear constraint in partial-Bell syndrome records and never searches through all Pauli indices. In the polynomial regime, its total processing time is polynomial as well. An exponentially long output or exhaustive classical decoder does not explain the lower bound.

The exact preserved-correlation promise is essential to this particular algorithm. A damped hidden correlation produces noisy parity constraints, for which rank deficiency need not persist. The general coefficient-learning result remains valid for arbitrary Pauli channels, but it is a different task from efficiently finding an unknown noisy parity.

## Weak channels and the cost of rare information

For the known mixture $`\widetilde\Lambda=(1-\tau)\mathrm{Id}+\tau\Lambda`$, the distance to the identity is at most $`2\tau`$ in diamond norm. Small $`\tau`$ makes informative error events rare.

At relative accuracy $`\varepsilon=\alpha\tau`$ with fixed $`0<\alpha<1/3`$, the [weak-noise bounds](weak_noise.md) give the same polynomial boundary in both acquisition models:

```math
R+\log(1/\tau)=O(\log n).
```

The additional logarithm accounts for the $`1/\tau`$ query factor. Even a full reference cannot estimate a superpolynomially rare signal to fixed relative accuracy with polynomially many calls. The positive-spike decision theorem has the same boundary without introducing an estimation accuracy parameter.

These mixtures permit rare, globally correlated Pauli errors. They do not impose a local interaction geometry or independent single-qubit noise. For $`\tau<1`$, the identity mixture of an entanglement-breaking spike channel need not itself be entanglement breaking.

## Scope of the complete result

The lower and upper bounds locate a joint threshold over all support and axis choices in the low-weight Pauli ball. Fixed-locality or polynomial-sized known observable families can have different costs. The lower bound uses ordinary memoryless channel access and the stated total width budget; the upper protocols assume ideal controls and reference qubits.

The precise finite bounds distinguish coherent and fresh experiments. Their accuracy factors and exponential constants should not be interchanged. In particular, the weighted inequality proved here is weaker than the exact extremal formula proposed in Kim–Oh's Eq. S85. Resolving that formula or the optimal coherent accuracy dependence would refine the rates, but neither is needed for the polynomial frontier proved in this account.
