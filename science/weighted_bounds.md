# Weighted Pauli response bounds

The lower bounds use a prior that favors Pauli operators of small weight. This page proves two estimates under that prior. The first controls the likelihood response of an arbitrary fresh experiment. The second controls the trace distance produced by one channel call with a bounded quantum reference. Both turn a rank constraint into an exponential suppression with the same parameter.

The channel and resource conventions are in [the model](model.md). The two operational applications are [fresh experiments](fresh_experiments.md) and [coherent memory](coherent_memory.md).

## Pauli notation and the product prior

Let $`d=2^n`$. Label Hermitian Pauli representatives by $`b\in\mathbb F_2^{2n}`$, with $`P_0=I_d`$. A label consists of one of four local Pauli labels at each site. The weight $`|b|`$ is the number of nonidentity sites. Addition of labels is binary addition; phases in Pauli multiplication do not affect this labeling. Write $`[e,b]\in\mathbb F_2`$ for the binary symplectic form. Then

```math
\mathrm{Tr}(P_bP_c)=d\,\mathbf 1_{b=c},
\qquad
P_eP_bP_e=(-1)^{[e,b]}P_b.
```

For $`0\le x\le1`$, define

```math
\nu_x(e)=\frac{x^{|e|}}{(1+3x)^n},
\qquad
t=\frac{1-x}{1+3x},
\qquad
\gamma=\frac{1-t}{1+t}=\frac{2x}{1+x}.
```

At $`x=0`$, the prior is concentrated on the identity label. At each site, the probabilities of the identity and each of the three nonidentity labels are $`1/(1+3x)`$ and $`x/(1+3x)`$, respectively. For a fixed nonzero local label, its character is positive on the identity and on itself, and negative on the other two labels. Consequently,

```math
\mathbb E_{e\sim\nu_x}(-1)^{[e,b]}=t^{|b|}.
```

Define the qubit depolarizing map and its tensor power by

```math
\Delta_s(A)=sA+(1-s)\frac{\mathrm{Tr}(A)}2I_2,
\qquad
\mathcal T_s=\Delta_s^{\otimes n},
\qquad 0\le s\le1.
```

They satisfy

```math
\mathcal T_s(P_b)=s^{|b|}P_b,
\qquad
\mathcal T_s\mathcal T_u=\mathcal T_{su},
\qquad
\mathbb E_{e\sim\nu_x}P_eAP_e=\mathcal T_t(A).
```

Each $`\mathcal T_s`$ is self-adjoint for the Hilbert–Schmidt inner product. The product prior is an analytical device. The physical channel hypotheses will use its restriction to required nonidentity labels, as described below.

## Hypercontractivity and the rank comparison

For a $`d\times d`$ complex matrix $`A`$, we distinguish the ordinary Schatten norms from their normalized versions. Here $`|A|=\sqrt{A^\dagger A}`$, whose eigenvalues are the singular values of $`A`$:

```math
\|A\|_p=\bigl(\mathrm{Tr}|A|^p\bigr)^{1/p},
\qquad
\tau_d(A)=\frac{\mathrm{Tr}(A)}d,
\qquad
\|A\|_{p,\mathrm{av}}=\bigl(\tau_d(|A|^p)\bigr)^{1/p}.
```

The indices $`p`$ and $`q`$ are real norm parameters. Normalization makes the identity matrix have norm one for every $`p`$. For a rank-$`r`$ matrix, the ratio $`r/d`$ compares the number of nonzero singular values with the full system dimension. A pure probe with at most $`k`$ reference qubits has a system marginal of rank at most $`2^k`$; the coherent argument below will use this connection between reference width and rank.

**Imported hypercontractivity theorem.** King's Corollary 2 states that, for $`1<p\le q`$,

```math
\|\mathcal T_s(A)\|_{q,\mathrm{av}}
\le \|A\|_{p,\mathrm{av}}
\quad\text{if}\quad
s\le\sqrt{\frac{p-1}{q-1}}.
```

The induced norm in King's Eq. (6) ranges over all complex matrices, so this inequality applies to non-Hermitian matrices. We use $`q=2`$, $`p=1+t`$, and $`s=\sqrt t`$. This is the established input to the arguments below; the weighted response estimates are its applications here. See [King2014](../references/RELATED_WORK.md#king2014), Corollary 2, Eq. (17), and Remark 2.

The endpoint $`t=0`$, where $`p=1`$, follows directly rather than requiring the theorem to be stated outside its range:

```math
\|\mathcal T_0(A)\|_{2,\mathrm{av}}
=|\tau_d(A)|
\le\tau_d(|A|)
=\|A\|_{1,\mathrm{av}}.
```

For a nonzero matrix $`A`$ of rank $`r`$ and $`1\le p\le2`$, Hölder's inequality for its $`r`$ nonzero singular values gives

```math
\sum_{i=1}^r\sigma_i^p
\le r^{1-p/2}\left(\sum_{i=1}^r\sigma_i^2\right)^{p/2}.
```

After including the normalization by $`d`$, this becomes

```math
\|A\|_{p,\mathrm{av}}
\le\left(\frac rd\right)^{1/p-1/2}
\|A\|_{2,\mathrm{av}}.
```

Combining the two inequalities and squaring yields the useful form

```math
\|\mathcal T_{\sqrt t}(A)\|_{2,\mathrm{av}}^2
\le\left(\frac rd\right)^{\gamma}
\|A\|_{2,\mathrm{av}}^2,
\qquad
\gamma=\frac{1-t}{1+t}.
```

At $`t=1`$, this statement is the identity with exponent zero. Thus it holds over the full interval needed here.

The depolarizing map damps high-weight Pauli components. Hypercontractivity controls the norm after damping, while the rank comparison controls the norm before damping. Together they turn $`r\le2^k`$ into the suppression factor $`2^{-(n-k)\gamma}`$ used by the response bounds.

## Complex response bound

**Lemma W1.** For every nonzero complex $`d\times d`$ matrix $`C`$ of rank $`r`$, define

```math
G_e(C)=
\frac{\mathrm{Tr}(P_eCP_eC^\dagger)}
{\mathrm{Tr}(CC^\dagger)}.
```

Then $`G_e(C)`$ is real, $`|G_e(C)|\le1`$, and

```math
F_x(C):=\mathbb E_{e\sim\nu_x}G_e(C)^2
\le\left(\frac rd\right)^{\gamma}.
```

In particular, if $`r\le2^k`$ and $`D=n-k`$,

```math
F_x(C)\le B_x,
\qquad
B_x:=2^{-D\gamma}
=2^{-(n-k)2x/(1+x)}.
```

### Proof

Let $`c_b=\mathrm{Tr}(P_bC)`$ and

```math
q_b=\frac{|c_b|^2}{d\mathrm{Tr}(CC^\dagger)}.
```

Pauli Parseval gives

```math
C=\frac1d\sum_b c_bP_b,
\qquad
\sum_b|c_b|^2=d\mathrm{Tr}(CC^\dagger).
```

Thus $`q`$ is a probability distribution describing how the squared matrix norm is distributed among Pauli components. It is separate from the physical channel's error distribution. Nuclear norm duality and the singular-value rank bound give

```math
|c_b|\le\|C\|_1\le\sqrt r\,\|C\|_2,
\qquad
q_b\le\frac rd.
```

Conjugating the Pauli expansion and using orthogonality shows that

```math
G_e(C)=\sum_bq_b(-1)^{[e,b]}.
```

This establishes reality and the bound by one without any Hermiticity assumption on $`C`$. Averaging the square under the product prior gives

```math
F_x(C)=\sum_{b,c}q_bq_c\,t^{|b+c|}.
```

For fixed $`c`$, the inner sum weights components by the number of local labels on which they differ from $`c`$. Let $`A=P_cC`$. Left multiplication by $`P_c`$ preserves rank and singular values and shifts that center to the identity, up to phases of modulus one:

```math
\left|\mathrm{Tr}(P_aA)\right|
=\left|\mathrm{Tr}(P_{a+c}C)\right|.
```

Since $`\mathcal T_{\sqrt t}`$ multiplies a coefficient of weight $`|a|`$ by $`t^{|a|/2}`$, Parseval gives the exact row identity

```math
\sum_bq_b\,t^{|b+c|}
=\frac{\|\mathcal T_{\sqrt t}(P_cC)\|_{2,\mathrm{av}}^2}
{\|C\|_{2,\mathrm{av}}^2}.
```

The preceding hypercontractive rank estimate bounds every row by $`(r/d)^\gamma`$. Averaging those rows with the probability weights $`q_c`$ proves W1.

There is also a direct check at $`x=1`$: then $`t=0`$ and

```math
F_1(C)=\sum_bq_b^2\le\max_bq_b\le\frac rd.
```

At $`x=0`$, only $`e=0`$ is sampled and $`F_0(C)=1`$. This completes the endpoints as well as the interior. ∎

### Relation to a stronger weighted inequality

For rank at most $`2^k`$, Kim–Oh's Eq. (S85) proposes the stronger inequality

```math
F_x(C)\le
\left(\frac{1+x}{1+3x}\right)^{n-k}.
```

That inequality is not assumed or proved here. For $`0<x<1`$, its exponent in base two is stronger than the exponent in W1. A tensor projector

```math
C=(|0\rangle\langle0|)^{\otimes(n-k)}\otimes I_{2^k}
```

has $`G_e(C)^2=1`$ precisely when each of its first $`n-k`$ local labels is identity or $`Z`$, and zero otherwise. It therefore attains the displayed proposed value. W1 suffices for the polynomial query frontier without establishing this sharper extremal statement. See [KimOh2026](../references/RELATED_WORK.md#kimoh2026).

## Root-fidelity bound

**Lemma W2.** Let $`\rho`$ be a density operator on $`\mathbb C^d`$ of rank $`r`$. Define

```math
f_e(\rho)=\|\sqrt\rho\,P_e\sqrt\rho\|_1.
```

This is the root fidelity between $`\rho`$ and $`P_e\rho P_e`$. It satisfies

```math
\mathbb E_{e\sim\nu_x} f_e(\rho)^2
\le\left(\frac rd\right)^\gamma.
```

In particular, the right side is at most $`B_x`$ whenever $`r\le2^k`$.

For a pure probe, [the one-call identity](coherent_memory.md#pure-inputs) will show that $`a f_e(\rho)`$ is the trace norm of the change from depolarization to a spike of amplitude $`a`$. This is why the coherent argument needs a response bound that remains valid before measurement. The following factorization converts its trace norm into a quadratic expression that the Pauli averaging map can evaluate.

### Proof

First use the ordinary, unnormalized Schatten norms. Factor the matrix in the trace norm as

```math
\sqrt\rho\,P_e\sqrt\rho
=\rho^{1/4}\bigl(\rho^{1/4}P_e\rho^{1/4}\bigr)\rho^{1/4}.
```

Schatten Hölder with exponents $`(4,2,4)`$ gives

```math
f_e(\rho)
\le\|\rho^{1/4}\|_4^2
\|\rho^{1/4}P_e\rho^{1/4}\|_2
=\|\rho^{1/4}P_e\rho^{1/4}\|_2,
```

because $`\mathrm{Tr}\rho=1`$. The middle matrix is Hermitian, and cyclicity of the trace gives

```math
f_e(\rho)^2
\le\mathrm{Tr}(\sqrt\rho\,P_e\sqrt\rho\,P_e).
```

The trace on the right is nonnegative because it equals the squared Hilbert–Schmidt norm in the preceding display. Average over the product prior and set $`A=\sqrt\rho`$. The Pauli averaging identity, self-adjointness, and semigroup property give

```math
\begin{aligned}
\mathbb E_{e\sim\nu_x}f_e(\rho)^2
&\le\mathrm{Tr}\bigl(A\mathcal T_t(A)\bigr)\\
&=\mathrm{Tr}\bigl(\mathcal T_{\sqrt t}(A)^\dagger
\mathcal T_{\sqrt t}(A)\bigr)\\
&=d\,\|\mathcal T_{\sqrt t}(A)\|_{2,\mathrm{av}}^2\\
&\le d\left(\frac rd\right)^\gamma
\|A\|_{2,\mathrm{av}}^2\\
&=\left(\frac rd\right)^\gamma.
\end{aligned}
```

The last equality uses $`\mathrm{Tr}(A^\dagger A)=\mathrm{Tr}\rho=1`$. This proves W2. At $`x=1`$, the same argument reduces directly to

```math
\mathbb E_{e\sim\nu_1}f_e(\rho)^2
\le\frac{(\mathrm{Tr}\sqrt\rho)^2}{d}
\le\frac rd,
```

so this endpoint does not require a limiting argument. ∎

## Conditioning on required nonidentity targets

Define the required family and its prior mass by

```math
\mathcal A_w=\{e:1\le|e|\le w\},
\qquad
p_A(x)=\nu_x(\mathcal A_w),
\qquad 1\le w\le n.
```

The number of nonidentity sites under $`\nu_x`$ has distribution

```math
W\sim\mathrm{Bin}\left(n,\frac{3x}{1+3x}\right),
\qquad
p_A(x)=\Pr(1\le W\le w).
```

For $`0<x\le1`$, this event has positive probability and conditioning rescales its remaining probabilities by $`1/p_A(x)`$. At $`x=0`$ all mass is on the excluded identity, so the conditioned law is undefined. If a function $`g_e`$ obeys $`\mathbb E_{\nu_x}|g_e|^2\le B_x`$, then

```math
\mathbb E_{\nu_x(\cdot\mid\mathcal A_w)}|g_e|^2
\le\frac{B_x}{p_A(x)},
\qquad
\mathbb E_{\nu_x(\cdot\mid\mathcal A_w)}|g_e|
\le\sqrt{\frac{B_x}{p_A(x)}}.
```

The first statement discards nonnegative contributions outside the event; the second is Cauchy–Schwarz under the conditional probability measure. It applies to W1 and W2. The identity label is excluded here because the spike-channel formula used for learning would otherwise fail to preserve trace; see [the coherent hard family](coherent_memory.md#physical-hard-family).

**Lemma W3: uniform mass choice.** For every integer $`n\ge1`$ and $`1\le w\le n`$, choose

```math
x_* = \frac{w}{3(2n-w)}.
```

Then

```math
W\sim\mathrm{Bin}\left(n,\frac{w}{2n}\right),
\qquad
\gamma_* = \frac{w}{3n-w},
\qquad
p_A(x_*)\ge\frac14.
```

**Proof.** The binomial parameter and the value of $`\gamma_*`$ follow by substitution. Its mean is $`w/2`$. Three elementary bounds cover all weights.

For $`w=1`$, Bernoulli's inequality gives

```math
p_A(x_*)=\Pr(W=1)
=\frac12\left(1-\frac1{2n}\right)^{n-1}
\ge\frac12\left(1-\frac{n-1}{2n}\right)
=\frac{n+1}{4n}\ge\frac14.
```

For $`w=2`$, the mean is one. The zero probability is at most $`e^{-1}`$, and Markov's inequality gives $`\Pr(W\ge3)\le1/3`$. Hence

```math
p_A(x_*)\ge1-e^{-1}-\frac13
=\frac23-e^{-1}>\frac14.
```

For $`w\ge3`$, the zero probability is at most $`e^{-w/2}\le e^{-3/2}`$, while

```math
\Pr(W>w)=\Pr(W\ge w+1)
\le\frac{w}{2(w+1)}\le\frac12.
```

It follows that $`p_A(x_*)\ge1/2-e^{-3/2}>1/4`$. ∎

For the full family $`w=n`$, a stronger endpoint follows by choosing $`x=1`$ instead:

```math
p_A(1)=1-4^{-n},
\qquad
\gamma=1,
\qquad
B_1=2^{-(n-k)}.
```

These conditional estimates supply all prior factors in the [fresh likelihood bound](fresh_experiments.md) and the [coherent hybrid bound](coherent_memory.md). Neither application uses an unphysical identity spike.
