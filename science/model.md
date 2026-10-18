# The channel, the memory budget, and the task

A device may retain one unknown Pauli correlation while erasing every other nonidentity component of its input. Finding that correlation is a small-output task, but the experiment must first couple to its unknown support and axes. This project asks how the number of channel calls depends jointly on the correlation's weight and the coherent memory available beside the device.

The central resource parameter is

```math
R=\frac{w(n-k)}{n}.
```

Here $`n`$ is the number of qubits acted on by the unknown channel, $`w`$ is the largest Pauli weight in the target family, and $`k`$ is the total coherent width outside the queried register at every invocation. At fixed nontrivial accuracy and confidence, polynomial query complexity is possible exactly when $`R=O(\log n)`$. The conclusion allows arbitrary coherent processing and reuse between calls. The [coherent lower bound](coherent_memory.md) and [partial-Bell construction](partial_bell.md) establish its two directions.

## Pauli channels and the target family

Let $`n\ge1`$, $`d=2^n`$, and label the Hermitian Pauli representatives by $`v=(x,z)\in\mathbb F_2^{2n}`$. One convention is

```math
P_v=i^{\sum_j x_jz_j}\bigotimes_{j=1}^n X^{x_j}Z^{z_j}.
```

The weight $`|v|`$ counts sites where $`(x_j,z_j)\ne(0,0)`$. Define the symplectic pairing

```math
[u,v]=x_u\cdot z_v+z_u\cdot x_v\pmod2.
```

Then $`P_uP_v=(-1)^{[u,v]}P_vP_u`$ and $`\operatorname{Tr}(P_uP_v)=d\,\mathbf1_{u=v}`$. A memoryless Pauli channel has the form

```math
\Lambda(X)=\sum_v p_vP_vXP_v,\qquad
p_v\ge0,\qquad \sum_vp_v=1.
```

Its eigenvalues in the Pauli basis are

```math
\Lambda(P_e)=\lambda_eP_e,\qquad
\lambda_e=\sum_vp_v(-1)^{[e,v]}.
```

Thus a coefficient is the mean commutation sign of an unknown Pauli error. The error distribution may contain correlations across the entire device. Memorylessness means that the same CPTP map is used at every call, with no retained unknown environment linking different calls.

Fix integers $`0\le k\le n`$ and $`1\le w\le n`$. The required family is

```math
\mathcal A_w=\{e:1\le |e|\le w\},\qquad
M_w=\sum_{u=0}^w\binom nu3^u.
```

The identity eigenvalue is known to be one. It is included in $`M_w`$ only to simplify upper-bound notation and is excluded from every physical hard prior.

## Coherent access

At each actual invocation, the channel acts on an $`n`$-qubit register $`S`$. All other accessible coherent registers together form $`A`$, with

```math
\dim A\le2^k.
```

An unrestricted classical history $`H`$ may be retained. The state at a query has the form

```math
\sum_h q_h |h\rangle\langle h|_H\otimes \rho_{SA}^{\,h}.
```

Known processing may act jointly on $`S`$ and $`A`$, move quantum information between them, produce measurement outcomes, reset registers, and adapt to the classical history. The system register itself may retain coherence between calls. Temporary implementation registers may be used between invocations; any register still coherent at an invocation belongs to $`A`$ and is counted.

The channel oracle is the ordinary map $`\Lambda\otimes\operatorname{Id}_A`$. Its environment, a purification of its action, an inverse, and controlled-channel access are not provided. An unlimited classical record cannot be reinterpreted as an uncounted coherent register. These distinctions are necessary for the width constraint to have an operational meaning.

The resource $`N`$ is a worst-case upper bound on the number of channel invocations. A long coherent block pays for every call it contains. An adaptive strategy may stop early. The hybrid proof treats halted classical branches as inactive, so it also covers this case without adding uncounted quantum storage. No claim about an expected-only query budget is needed.

The lower bound allows unlimited classical computation and arbitrary known operations. The constructive upper bound uses ideal local Clifford operations, Bell preparation and readout, and classical processing whose cost is given below. Imperfect reference qubits and general preparation or readout errors are not part of the upper-bound model.

## Learning a reusable record

The family $`\mathcal A_w`$ is known before data acquisition. A learner produces a classical record $`Z`$ and a decoding function $`\widehat\lambda_e(Z)`$. For every allowed channel and every $`e\in\mathcal A_w`$, the requirement is

```math
\Pr_\Lambda\!\left[
  |\widehat\lambda_e(Z)-\lambda_e|\le\varepsilon
\right]\ge1-\delta.
```

The particular index $`e`$ may be supplied after acquisition. The [upper construction](partial_bell.md) satisfies the stronger simultaneous guarantee for every index in the family. The [lower bound](coherent_memory.md) needs only the pointwise guarantee above and remains valid if the final decoder may measure a bounded retained quantum output after receiving $`e`$.

The timing of the index matters. If one Pauli is supplied before the experiment, its eigenvalue can be estimated directly with no reference qubits and $`O(\varepsilon^{-2}\log(1/\delta))`$ calls. Likewise, a polynomial-sized known list can be measured one observable at a time. The necessity result concerns the complete support-and-axis family $`\mathcal A_w`$, not every list whose observables happen to have weight at most $`w`$.

## Fresh experiments

The fresh-experiment model is a subclass of coherent access. At each round the learner prepares an arbitrary state on $`S A`$, applies the channel once, and completely measures the quantum output. Only classical information survives into the next round. Both the probe and the joint POVM may depend on the preceding classical history.

This restriction gives a stronger lower bound in [fresh experiments](fresh_experiments.md), including an $`\varepsilon^{-2}`$ accuracy factor. The general coherent proof has an $`\varepsilon^{-1}`$ factor. Both lower bounds lead to the same polynomial-versus-superpolynomial frontier, but their finite rates are distinct statements.

## A one-bit decision task

The [correlation detection theorem](correlation_detection.md) uses the promise

```math
\begin{aligned}
\Lambda_{\tau,0}
  &=(1-\tau)\operatorname{Id}+\tau\Lambda_{\rm dep},\\
\Lambda_{\tau,e}
  &=(1-\tau)\operatorname{Id}+\tau\Lambda_e,\\
\Lambda_{\rm dep}(X)
  &=\frac{I\,\operatorname{Tr}X}{d},\\
\Lambda_e(X)
  &=\frac{I\,\operatorname{Tr}X+P_e\operatorname{Tr}(P_eX)}{d}.
\end{aligned}
```

The strength $`0<\tau\le1`$ is known and the nonidentity index $`e\in\mathcal A_w`$ is hidden throughout the protocol. The output is one bit identifying the null or alternative, with error at most $`\delta`$ for every promised channel. Under the alternative, $`P_e`$ is exactly preserved; every other nonidentity Pauli has eigenvalue $`1-\tau`$. Under the null they all have eigenvalue $`1-\tau`$.

This task has polynomial query cost and a polynomial-time implementation exactly when

```math
R+\log(1/\tau)=O(\log n)
```

at fixed nontrivial confidence. The direct decision lower bound does not assume that detection is as hard as learning. The positive-spike family and the detection task originate in [Chen–Gong](../references/RELATED_WORK.md#chengong2025); the support-dependent width law is the conclusion developed here.

## Computation, storage, and precision

| Resource | Constructive accounting |
|---|---|
| Unknown-channel access | One ordinary invocation per fresh probe; all invocations are counted. |
| Coherent width at a call | $`n`$ channel-input qubits plus at most $`k`$ reference qubits. |
| Known quantum operations | $`O(n)`$ local Clifford and Bell operations per probe, with ideal preparation and readout. |
| Classical acquisition record | $`O(nN)`$ bits for settings and syndrome outcomes. No QRAM is used. |
| One requested coefficient | A scan of the record, using $`O(nN)`$ elementary operations and polynomial-bit arithmetic for the stated parameter regimes. |
| All coefficients as an explicit list | At least the list's output length; the query theorem does not promise polynomial time to print exponentially many entries. |
| Promised decision | Binary Gaussian elimination on $`n+k`$-bit records, polynomial in $`n`$ and $`N`$, without enumerating $`\mathcal A_w`$. |

The usability probability is an explicit hypergeometric sum depending only on $`n,k`$ and the requested weight. Its exact rational representation has polynomial bit length, so coefficient decoding does not hide a table of exponential size. Finite arithmetic precision may be chosen below the requested statistical error.

For asymptotic frontier statements, $`\varepsilon`$ and $`\delta`$ are fixed nontrivial constants, with $`0<\varepsilon<1/3`$ and $`0<\delta<1/2`$. The learning equivalence also holds for inverse-polynomial accuracy and inverse-polynomial failure probability. A superpolynomial precision demand is an additional resource requirement. For weak channels, [weak noise](weak_noise.md) states the absolute-error and relative-error regimes separately.

## Reading the argument

Start with the [weighted operator bounds](weighted_bounds.md). They lead to the [general coherent converse](coherent_memory.md) and the [sharper fresh-experiment converse](fresh_experiments.md). The [partial-Bell protocol](partial_bell.md) supplies the learning upper bound. The [one-bit detector](correlation_detection.md) and [weak-noise rates](weak_noise.md) give two operational consequences. Finally, [interpretation](interpretation.md) connects the parameter regimes and the limits of the conclusions.
