# Learning with persistent coherent memory

The weight–memory threshold remains valid when the learner preserves quantum information between calls, concatenates calls, and uses arbitrary adaptive quantum processing. The lower bound counts every invocation of the unknown channel. Its memory restriction applies at each invocation: all coherent registers outside the $`n`$-qubit input register together have dimension at most $`2^k`$.

This page proves the lower bound. The [partial-Bell protocol](partial_bell.md), which uses one call per fresh experiment, supplies the upper bound in this larger model. Definitions of the learning task and its classical output are collected in [the model](model.md).

## Statement and resource contract

Let $`n,k,w`$ be integers with $`n\ge1`$, $`0\le k\le n`$, and $`1\le w\le n`$. Let $`0<\epsilon<1/3`$ and $`0<\delta<1/2`$. Put

```math
D=n-k,
\qquad
R=\frac{wD}{n}.
```

The target family $`\mathcal A_w=\{e:1\le|e|\le w\}`$ is known before acquisition. The particular index $`e`$ is supplied after all calls. The required pointwise guarantee is

```math
\Pr\bigl(|\widehat\lambda_e-\lambda_e|\le\epsilon\bigr)
\ge1-\delta
\quad\text{for every allowed channel and every }e\in\mathcal A_w.
```

A guarantee that holds simultaneously for the whole family is stronger and is therefore also covered by the lower bound.

**Theorem C1.** Every learner satisfying this guarantee with at most $`N`$ channel calls on every execution branch obeys

```math
N\ge\frac{1-2\delta}{3\epsilon}
\,2^{\frac{w(n-k)}{2(3n-w)}}.
```

The allowed protocols have the following precise features. At a channel call, the active input has a classical–quantum form

```math
\sum_h q_h|h\rangle\langle h|_H\otimes\omega_{h,SA},
\qquad
\dim S=2^n,
\qquad
\dim A\le2^k.
```

The classical register $`H`$ may contain all earlier outcomes and random seeds. Its size and the classical computation are unrestricted. Known quantum channels and instruments between invocations may depend on this record. The register $`S`$ may retain information from previous invocations; the protocol need not reset it. Ancillas used to implement a known operation may be discarded before the next call. Every coherent register present outside $`S`$ at a call belongs to $`A`$ and is charged to its dimension bound.

An uncounted coherent controller, retained channel environment, or quantum copy of an unlimited classical record is therefore outside the contract. Access consists of ordinary uses of the unknown memoryless channel. A controlled channel, inverse, or Stinespring oracle is not supplied.

The ordinary required output is a classical record. The lower-bound proof also permits the learner to retain its bounded quantum state until the requested index is revealed and then apply an index-dependent final measurement. This extra power does not affect the result.

## Physical hard family

Let $`d=2^n`$ and let $`\mathcal D`$ be the completely depolarizing channel. For a nonidentity Pauli label $`e`$ and $`0<a\le1`$, define a positive spike by

```math
\mathcal D(X)=\frac{\mathrm{Tr}(X)}dI_d,
\qquad
\Lambda_e^{(a)}(X)
=\mathcal D(X)+\frac a d\mathrm{Tr}(P_eX)P_e.
```

This is a Pauli channel with error probabilities

```math
p_v^{(e,a)}=\frac{1+a(-1)^{[e,v]}}{d^2}.
```

They are nonnegative. Since $`e\ne0`$, its nontrivial symplectic character sums to zero, so the probabilities sum to one. Their Pauli eigenvalues are $`1`$ at the identity, $`a`$ at $`P_e`$, and zero at every other nonidentity label. This proves the claimed channel formula and complete positivity. No random choice of spike sign is needed for the coherent lower bound.

The hidden label will be drawn from the prior $`\nu_x`$ conditioned on $`\mathcal A_w`$. Its mass $`p_A(x)>0`$, the exponent $`\gamma=2x/(1+x)`$, and $`B_x=2^{-D\gamma}`$ are defined and bounded in [the weighted estimates](weighted_bounds.md#conditioning-on-required-nonidentity-targets).

## One call with a bounded reference

For a state $`\omega_{SA}`$, define the Hermitian operator on $`A`$

```math
B_e(\omega)=\mathrm{Tr}_S\bigl[(P_e\otimes I_A)\omega\bigr].
```

Hermiticity follows from cyclicity of the partial trace with respect to operators on $`S`$. The two channel outputs differ by

```math
\bigl[(\Lambda_e^{(a)}-\mathcal D)\otimes\mathrm{id}_A\bigr](\omega)
=\frac a d P_e\otimes B_e(\omega).
```

Because $`\|P_e\|_1=d`$ and the trace norm is multiplicative on tensor products,

```math
\left\|\bigl[(\Lambda_e^{(a)}-\mathcal D)\otimes\mathrm{id}_A\bigr](\omega)\right\|_1
=a\,\|B_e(\omega)\|_1.
```

### Pure inputs

Suppose first that $`\omega=|\psi\rangle\langle\psi|`$ is pure and let $`\rho=\mathrm{Tr}_A\omega`$. In a Schmidt decomposition,

```math
|\psi\rangle=\sum_{i=1}^r\sqrt{\lambda_i}\,|u_i\rangle_S|v_i\rangle_A,
\qquad r\le\dim A\le2^k.
```

In the indicated bases, the nonzero block of $`B_e(\omega)`$ has entries $`\sqrt{\lambda_i\lambda_j}\langle u_j|P_e|u_i\rangle`$. It is the transpose of the corresponding block of $`\sqrt\rho P_e\sqrt\rho`$. Transposition and the addition of zero blocks preserve singular values. Therefore

```math
\|B_e(\omega)\|_1
=\|\sqrt\rho\,P_e\sqrt\rho\|_1.
```

Lemma W2 of [the weighted bounds](weighted_bounds.md#root-fidelity-bound) gives

```math
\mathbb E_{e\sim\nu_x}\|B_e(\omega)\|_1^2\le B_x.
```

### Mixed inputs and classical histories

A mixed input need not have a rank-$`2^k`$ system marginal, so the pure-state conclusion cannot be applied directly to that marginal. Instead, decompose the actual input within its existing registers:

```math
\omega_{SA}=\sum_j u_j|\psi_j\rangle\langle\psi_j|,
\qquad
u_j\ge0,
\qquad
\sum_j u_j=1.
```

Every pure component is a state on the same $`S\otimes A`$. Trace-norm convexity and Jensen's inequality imply

```math
\begin{aligned}
\|B_e(\omega)\|_1^2
&\le\left(\sum_j u_j\|B_e(|\psi_j\rangle\langle\psi_j|)\|_1\right)^2\\
&\le\sum_j u_j\|B_e(|\psi_j\rangle\langle\psi_j|)\|_1^2.
\end{aligned}
```

Averaging proves the same second-moment bound. This is an algebraic decomposition, not an assumption that a purification in an additional memory register is available.

For a fixed classical–quantum input, define

```math
g_e=\sum_hq_h\|B_e(\omega_{h,SA})\|_1.
```

The norm of the output difference is $`a g_e`$, since the classical blocks are orthogonal. A second application of Jensen gives $`\mathbb E_{\nu_x}g_e^2\le B_x`$. These statements require the input state, including the probabilities $`q_h`$, to be independent of the hidden label being averaged. After conditioning on the required family, Cauchy–Schwarz gives

```math
\mathbb E_{e\sim\nu_x(\cdot\mid\mathcal A_w)}g_e
\le\sqrt{\frac{B_x}{p_A(x)}}.
```

Thus the mean trace distance from one changed channel call is at most

```math
\frac a2\sqrt{\frac{B_x}{p_A(x)}}.
```

The bound is independent of the number of classical histories. For continuous outcomes, the same calculation uses integrals against the history measure; convexity and Cauchy–Schwarz give the identical result.

## Forward hybrid for adaptive coherent protocols

Write $`\mathrm{TD}(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. Fix a hidden label $`e`$ temporarily. For $`j=0,\ldots,N`$, let $`\sigma_j^{(e)}`$ be the acquisition output of the protocol whose first $`j`$ invocations use $`\mathcal D`$ and whose subsequent invocations use $`\Lambda_e^{(a)}`$. This output is taken before the target index is revealed and before any index-dependent decoding. Thus $`\sigma_0^{(e)}`$ is the all-spike output, whereas the all-depolarizing output $`\sigma_N`$ is independent of $`e`$.

For an at-most-$`N`$ worst-case budget, view the procedure as $`N`$ successive possible query slots. A classical halt branch is inactive in every later slot and is left unchanged. At slot $`j`$, only the active branches invoke the channel. They satisfy the width constraint above. In the one-call norm estimate, their probabilities have sum at most one; adjoining a zero response for the inactive mass preserves Jensen's inequality. This handles early stopping without adding a register for dummy queries. No bound on expected calls is substituted for the worst-case budget.

The executions producing $`\sigma_{j-1}^{(e)}`$ and $`\sigma_j^{(e)}`$ have an identical prefix: their first $`j-1`$ active calls are depolarizing. Hence their state immediately before slot $`j`$, including all classical history probabilities, is independent of $`e`$. This is the fixed input required by the weighted estimate.

At slot $`j`$, one execution uses the spike and the other uses the depolarizing channel. Their suffixes are identical for this fixed $`e`$: all later active calls use the spike and all known adaptive controls are the same. Including the retained classical outcomes, that suffix is one common completely positive trace-preserving map. Trace-distance contraction therefore gives

```math
\mathrm{TD}\bigl(\sigma_{j-1}^{(e)},\sigma_j^{(e)}\bigr)
\le\frac a2 g_{e,j},
```

where $`g_{e,j}`$ is computed on the common, label-independent input at slot $`j`$. Average over $`e\sim\nu_x(\cdot\mid\mathcal A_w)`$ and sum the triangle inequality over all slots:

```math
\mathbb E_e\mathrm{TD}\bigl(\sigma_0^{(e)},\sigma_N\bigr)
\le\frac{Na}{2}\sqrt{\frac{B_x}{p_A(x)}}.
```

This comparison permits intermediate measurements, adaptive controls, and coherent states surviving arbitrarily many invocations. The direction of the hybrid supplies a depolarizing prefix, so the prior is never applied to a label-dependent input state. The suffix may depend on the fixed hidden label; contraction only needs that suffix to be common to the two adjacent executions.

## Learning-to-testing reduction and finite constants

Set $`a=3\epsilon<1`$. For each revealed target $`e\in\mathcal A_w`$, threshold the learner's estimate at $`a/2`$. Under $`\mathcal D`$, an accurate estimate lies in $`[-\epsilon,\epsilon]`$ and the test returns the null hypothesis. Under $`\Lambda_e^{(a)}`$, an accurate estimate lies in $`[2\epsilon,4\epsilon]`$ and the test returns the spike hypothesis. The closed accuracy intervals are separated, so no tie convention is required for successful estimates.

This is an $`e`$-dependent final test on two acquisition outputs. It does not make $`e`$ available during acquisition. Its probability of declaring a spike differs by at least $`1-2\delta`$ between those outputs. The variational characterization of trace distance implies, for each required label,

```math
\mathrm{TD}\bigl(\sigma_0^{(e)},\sigma_N\bigr)\ge1-2\delta.
```

This reasoning also covers an index-dependent quantum decoder applied to a retained output state, because any such test is a measurement effect on that state. Combining with the hybrid proves the general-prior bound

```math
N\ge
\frac{2(1-2\delta)\sqrt{p_A(x)}}{3\epsilon}
\,2^{D x/(1+x)},
\qquad 0<x\le1.
```

Choose $`x=w/[3(2n-w)]`$. Lemma W3 gives $`p_A(x)\ge1/4`$ and $`2x/(1+x)=w/(3n-w)`$. Substitution proves C1:

```math
N\ge\frac{1-2\delta}{3\epsilon}
\,2^{\frac{w(n-k)}{2(3n-w)}}.
```

For $`w=n`$, choosing $`x=1`$ gives the stronger endpoint

```math
N\ge\frac{2(1-2\delta)\sqrt{1-4^{-n}}}{3\epsilon}
\,2^{(n-k)/2}.
```

These are lower bounds with explicit constants, not optimal finite-sample formulas. In particular, this trace-distance hybrid gives an inverse first power of the accuracy. It does not establish a multiplicative $`\epsilon^{-2}`$ factor in the coherent exponential lower bound. The stronger accuracy dependence in [fresh experiments](fresh_experiments.md) uses a different likelihood argument and the additional reset condition.

## Polynomial query frontier

The exponent in C1 obeys

```math
\frac{w(n-k)}{2(3n-w)}
=\frac{R}{2(3-w/n)}\ge\frac R6.
```

The [partial-Bell construction](partial_bell.md) is admissible under the coherent resource contract and gives simultaneous estimates using

```math
N\le\left\lceil
4\epsilon^{-2}\ln\left(\frac{2M_w}{\delta}\right)3^R
\right\rceil,
\qquad
M_w=\sum_{u=0}^w\binom nu3^u\le4^n.
```

For fixed $`\epsilon\in(0,1/3)`$ and $`\delta\in(0,1/2)`$, these bounds imply

```math
\text{polynomial query complexity in }n
\quad\Longleftrightarrow\quad
\frac{w(n-k)}n=O(\log n).
```

This holds both for pointwise late-index learning and for simultaneous learning. A polynomial upper bound on the optimal query count forces $`R=O(\log n)`$ through C1. Conversely, $`R=O(\log n)`$ makes the explicit upper bound polynomial. If $`R/\log n`$ tends to infinity, the lower bound is superpolynomial. The same equivalence holds when $`1/\epsilon`$ and $`\ln(1/\delta)`$ are polynomially bounded and the success margin $`1-2\delta`$ is at least inverse polynomial.

Coherent concatenation can change how many final measurements are made. The result concerns total channel calls, including calls within long coherent blocks. Chen–Gong explicitly distinguishes these two costs and proves a general coherent full-family lower bound [ChenGong2025](../references/RELATED_WORK.md#chengong2025). The present result supplies the joint dependence on weight and charged coherent width. The one-sided coherent restrictions used in [KangJeonOh2026](../references/RELATED_WORK.md#kangjeonoh2026) are different from the arbitrary feedback allowed here; the comparison is detailed in [related work](../references/RELATED_WORK.md).

## Detection and weak noise

The hybrid bound holds for any amplitude $`0<a\le1`$ before choosing an estimation accuracy. A binary test distinguishing $`\mathcal D`$ from every unknown $`\Lambda_e^{(a)}`$, $`e\in\mathcal A_w`$, with error at most $`\delta`$ therefore requires

```math
N\ge
\frac{2(1-2\delta)\sqrt{p_A(x)}}a
\,2^{D x/(1+x)}.
```

The test need not be given the label: a single valid decision rule is a special case of the label-dependent tests permitted in the argument. At $`a=1`$, the alternative preserves one hidden Pauli correlation exactly. The [correlation-detection account](correlation_detection.md) gives an efficient algorithm for this one-bit task and establishes the same polynomial frontier.

For known $`0<\tau\le1`$, replace the two channels by

```math
\widetilde\Lambda_0=(1-\tau)\mathrm{id}+\tau\mathcal D,
\qquad
\widetilde\Lambda_e=(1-\tau)\mathrm{id}+\tau\Lambda_e^{(a)}.
```

Their one-call difference is multiplied by $`\tau`$. A hybrid whose prefix uses the known channel $`\widetilde\Lambda_0`$ still has a label-independent query state, so the preceding proof applies with $`a`$ replaced by $`\tau a`$. The resulting bound is

```math
N\ge
\frac{2(1-2\delta)\sqrt{p_A(x)}}{\tau a}
\,2^{D x/(1+x)}.
```

The [weak-noise account](weak_noise.md) relates this formula to absolute and relative estimation accuracy and supplies the matching polynomial frontier. Near-identity channels in this construction may still contain rare spatially correlated Pauli errors; no local or sparse noise promise is imposed.
