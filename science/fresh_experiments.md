# Learning with fresh experiments

Each fresh experiment prepares an arbitrary state of the $`n`$ system qubits and at most $`k`$ reference qubits, uses the unknown channel once, and converts its output into a classical outcome. The next preparation and measurement may depend on the entire classical record. Under this contract, the number of channel calls has a quadratic dependence on the required inverse accuracy.

The [resource model](model.md) specifies the learning task and its late target: data acquisition must finish before the requested Pauli label is supplied. The lower bound below needs only a pointwise guarantee for every allowed channel and every requested label. It therefore also applies to a record that estimates all requested coefficients simultaneously.

## Finite lower bound

Let $`n\geq 1`$, $`0\leq k\leq n`$, and $`1\leq w\leq n`$ be integers. Write

```math
D=n-k,\qquad R=\frac{wD}{n},\qquad
\kappa=\frac{w}{3n-w}.
```

Suppose a fresh-experiment learner uses at most $`N`$ channel calls and estimates each requested Pauli eigenvalue of weight from $`1`$ to $`w`$ to additive error $`\epsilon`$, with failure probability at most $`\delta`$, for every Pauli channel. For

```math
0<\epsilon<\frac13,\qquad 0<\delta<\frac12,
```

it must satisfy

```math
\boxed{
N\geq
\frac{1-2\delta}{36\epsilon^2}\,
2^{\,w(n-k)/(3n-w)}.
}
```

The proof uses the rank-constrained response bound in [Weighted Pauli bounds](weighted_bounds.md#complex-response-bound). Its likelihood reduction and sign averaging follow the framework of [KimOh2026](../references/RELATED_WORK.md#kimoh2026); the weighted bound supplies the dependence on the joint weight and reference budget.

### Valid channel hypotheses and the target prior

Let $`d=2^n`$, let $`P_e`$ be the Hermitian representative of a Pauli label, and write its commutation character as

```math
\chi_e(v)=(-1)^{[e,v]}.
```

The reference channel is complete depolarization,

```math
\mathcal D(X)=\frac{\operatorname{Tr}(X)}{d}I.
```

For a **nonidentity** label $`e`$, a sign $`s\in\{-1,+1\}`$, and an amplitude $`0<a<1`$, define

```math
\Lambda_{e,s}(X)
=\frac{\operatorname{Tr}(X)}{d}I
 +\frac{s a\,\operatorname{Tr}(P_eX)}{d}P_e.
```

These are physical Pauli channels. Their error distributions are

```math
p_{e,s}(v)=\frac{1+s a\,\chi_e(v)}{d^2}.
```

Nonnegativity follows from $`a<1`$. Normalization follows from $`\sum_v\chi_e(v)=0`$ for every nonidentity $`e`$. The identity eigenvalue is $`1`$, the eigenvalue at $`P_e`$ is $`s a`$, and every other nonidentity eigenvalue is zero. The sign and label are selected once and remain fixed throughout all channel calls.

For the algebraic averaging, use the product distribution

```math
\nu_x(e)=\frac{x^{|e|}}{(1+3x)^n}.
```

The actual hidden-label distribution is this law conditioned on the required, nonidentity target set:

```math
A_w=\{e:1\leq |e|\leq w\},\qquad
p_A=\nu_x(A_w),\qquad
\nu_{x,A}(e)=\frac{\nu_x(e)\mathbf 1_{A_w}(e)}{p_A}.
```

Thus the identity is used only in the algebraic product average, never as a channel hypothesis. The [prior-mass lemma](weighted_bounds.md#conditioning-on-required-nonidentity-targets) gives, for

```math
x=\frac{w}{3(2n-w)},
```

the uniform estimates

```math
p_A\geq\frac14,\qquad
B_x=2^{-D\,2x/(1+x)}=2^{-\kappa D}.
```

In particular, conditioning costs exactly the factor $`1/p_A`$. No unnormalized hypothesis distribution is used.

## The one-experiment likelihood

Fix a classical history, so that the preparation and POVM for the next experiment are determined. First take a pure preparation and a rank-one POVM effect. Let $`r\leq 2^k`$ be the reference dimension, and write their system-by-reference coefficient matrices as

```math
|\psi\rangle=\sum_{i=1}^{d}\sum_{\alpha=1}^{r}
\Psi_{i\alpha}|i\rangle|\alpha\rangle,\qquad
|m\rangle=\sum_{i=1}^{d}\sum_{\alpha=1}^{r}
M_{i\alpha}|i\rangle|\alpha\rangle.
```

Here $`\|\Psi\|_F=1`$, whereas the vector $`|m\rangle`$ defining the effect $`|m\rangle\langle m|`$ need not be normalized. Define

```math
C=M\Psi^\dagger.
```

This is an arbitrary complex $`d`$-by-$`d`$ matrix with rank at most $`r`$. The null outcome probability is

```math
q_{\mathcal D}
=\langle m|(\mathcal D\otimes\operatorname{id})
 (|\psi\rangle\langle\psi|)|m\rangle
=\frac{\|C\|_F^2}{d}.
```

To check the signal term without a transpose convention, the reference operators satisfy

```math
\rho_A^{\mathsf T}=\Psi^\dagger\Psi,\qquad
\left(
\operatorname{Tr}_S[(P_e\otimes I)|\psi\rangle\langle\psi|]
\right)^{\mathsf T}
=\Psi^\dagger P_e\Psi,
```

and

```math
\langle m|A\otimes B|m\rangle
=\operatorname{Tr}(M^\dagger A M B^{\mathsf T}).
```

Consequently,

```math
q_{e,s}
=q_{\mathcal D}
 +\frac{s a}{d}\operatorname{Tr}(P_e C P_e C^\dagger).
```

At any outcome with $`q_{\mathcal D}>0`$, its likelihood ratio is therefore

```math
\frac{q_{e,s}}{q_{\mathcal D}}
=1+s a\,G_e(C),\qquad
G_e(C)=
\frac{\operatorname{Tr}(P_e C P_e C^\dagger)}
     {\operatorname{Tr}(CC^\dagger)}.
```

The [complex response lemma](weighted_bounds.md#complex-response-bound) proves that $`G_e(C)`$ is real, that $`|G_e(C)|\leq 1`$, and that

```math
\mathbb E_{e\sim\nu_x}G_e(C)^2\leq B_x.
```

### Mixed preparations and arbitrary POVMs

For a mixed preparation, take a pure-state decomposition with weights $`\eta_j`$. For an arbitrary effect, take a sum of rank-one effects and absorb their nonnegative spectral weights into their vectors. Let $`q_{j\ell}`$ and $`G_e(C_{j\ell})`$ be the null probabilities and responses of the resulting elementary pairs. The full null probability and response are

```math
q_{\mathcal D}
=\sum_{j,\ell}\eta_j q_{j\ell},\qquad
g_e=
\sum_{j,\ell}
\frac{\eta_j q_{j\ell}}{q_{\mathcal D}}\,G_e(C_{j\ell}).
```

The weights in this convex combination depend on the preparation, effect, and null channel; they do not depend on the hidden label or sign. Jensen's inequality gives

```math
|g_e|\leq1,\qquad
\mathbb E_{e\sim\nu_x}g_e^2\leq B_x,\qquad
\mathbb E_{e\sim\nu_{x,A}}g_e^2\leq\frac{B_x}{p_A}.
```

Each matrix $`C_{j\ell}`$ has rank at most $`2^k`$. Decomposing a mixed state in the declared system-reference space does not supply an additional purifying register.

If $`q_{\mathcal D}=0`$, every elementary term with positive preparation weight has $`C_{j\ell}=0`$. Its signal term is then also zero. Hence every alternative outcome probability is zero as well. Such outcomes may be omitted, and there is no absolute-continuity gap in the likelihood calculation.

## The signed transcript bound

Include the learner's ordinary classical randomness in its transcript. A protocol with a worst-case budget of at most $`N`$ calls can be padded with ignored fresh experiments, so take the length to be exactly $`N`$.

For a complete transcript $`z=(z_1,\ldots,z_N)`$ with positive null probability, let $`g_{e,\ell}(z_{\leq\ell})`$ denote the response at its $`\ell`$th outcome. The preparation and POVM at that node depend on the preceding transcript. The likelihood of the full execution with the fixed channel $`\Lambda_{e,s}`$, relative to the all-depolarizing execution, is

```math
L_{e,s}(z)=\prod_{\ell=1}^{N}
\left(1+s a\,g_{e,\ell}(z_{\leq\ell})\right).
```

Let $`Q_0`$ be the null transcript law and $`Q_{e,s}`$ the alternative transcript law. Averaging over the one sign chosen at the beginning gives

```math
\overline Q_e=\frac{Q_{e,+}+Q_{e,-}}2,\qquad
\overline L_e=\frac{L_{e,+}+L_{e,-}}2.
```

This is a mixture of two complete executions. It does not replace each channel call by its sign-averaged channel.

Because all likelihood factors are nonnegative, arithmetic-geometric mean gives

```math
\overline L_e(z)
\geq\sqrt{L_{e,+}(z)L_{e,-}(z)}
=\prod_{\ell=1}^{N}
 \sqrt{1-a^2g_{e,\ell}(z_{\leq\ell})^2}.
```

For numbers $`0\leq u_\ell\leq1`$, one has $`\sqrt{1-u_\ell}\geq1-u_\ell`$ and $`\prod_\ell(1-u_\ell)\geq1-\sum_\ell u_\ell`$. It follows that

```math
\left[1-\overline L_e(z)\right]_+
\leq a^2\sum_{\ell=1}^{N}g_{e,\ell}(z_{\leq\ell})^2,
```

where $`[u]_+=\max\{u,0\}`$. With total variation normalized as one half of the $`L^1`$ distance,

```math
\operatorname{TV}(Q_0,\overline Q_e)
=\mathbb E_{z\sim Q_0}
 \left[1-\overline L_e(z)\right]_+.
```

Under $`Q_0`$, every history and every adaptively selected experiment is independent of the hidden label. We may therefore average the uniform node bound against the original conditioned prior at each null history:

```math
\begin{aligned}
\mathbb E_{e\sim\nu_{x,A}}
\operatorname{TV}(Q_0,\overline Q_e)
&\leq
a^2\sum_{\ell=1}^{N}
\mathbb E_{z\sim Q_0}
\mathbb E_{e\sim\nu_{x,A}}
g_{e,\ell}(z_{\leq\ell})^2\\
&\leq \frac{N a^2 B_x}{p_A}.
\end{aligned}
```

This is the point that handles arbitrary classical adaptivity. The proof averages histories generated by the null channel; it never substitutes an unchanged prior for the posterior of a spike execution. Sums over outcomes can be replaced by integrals for general POVMs.

## From learning to a decision

Set $`a=3\epsilon`$. After acquisition, supply the hidden target $`e\in A_w`$ to the estimator and declare an alternative when

```math
|\widehat\lambda_e|>\frac{3\epsilon}{2}.
```

Under the null, successful estimation gives $`|\widehat\lambda_e|\leq\epsilon`$. Under either signed alternative, it gives $`|\widehat\lambda_e|\geq2\epsilon`$. The closed error intervals are strictly separated from the decision threshold.

For each $`e`$, the decision has false-positive and false-negative probabilities at most $`\delta`$, including after averaging the sign. Its success implies

```math
\operatorname{TV}(Q_0,\overline Q_e)\geq1-2\delta.
```

Any randomized final decoder is simply a statistical postprocessing and obeys the same total-variation bound. Combining the last two inequalities yields

```math
N\geq
\frac{(1-2\delta)p_A}{9\epsilon^2 B_x}
\geq
\frac{1-2\delta}{36\epsilon^2}2^{\kappa D}.
```

This completes the lower bound.

## Consequences and model boundary

The [partial-Bell construction](partial_bell.md) supplies a simultaneous upper bound of order $`\epsilon^{-2}3^R\log(M_w/\delta)`$, where $`M_w`$ counts the Pauli targets including the known identity. Since $`\kappa D\geq R/3`$, the upper and lower exponents are both proportional to $`R`$. At fixed nontrivial accuracy and confidence, polynomially many calls are possible precisely when $`R=O(\log n)`$.

The argument on this page requires a classical transcript between fresh experiments. Arbitrary persistent coherent memory is treated separately in [Coherent memory](coherent_memory.md), which obtains the same polynomial frontier through a different trace-distance argument. The stronger $`\epsilon^{-2}`$ lower prefactor proved here is not inferred from that coherent argument.

For a known weak-noise scale, the outcome-weighted version of the same likelihood calculation improves the fresh-experiment prefactor to $`\tau/\epsilon^2`$; see [Weak channels](weak_noise.md).
