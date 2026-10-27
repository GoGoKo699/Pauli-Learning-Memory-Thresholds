# Learning weak Pauli channels

The weight-memory threshold also holds for channels close to the identity, provided the requested precision resolves their noise. In the fresh-experiment model, centering the estimator at the known identity response gives a variance proportional to the noise scale. A matching likelihood argument gives the same scale in the lower prefactor.

The references on this page are ideal. The additional promise concerns the unknown system channel.

## Channel class and finite bounds

Fix a known $`0<\tau\leq1`$. The unknown channel belongs to the class

```math
\widetilde\Lambda=(1-\tau)\mathrm{id}+\tau\Lambda,
```

where $`\Lambda`$ is an otherwise arbitrary memoryless Pauli channel. Equivalently, the Pauli-error distribution of $`\widetilde\Lambda`$ assigns probability at least $`1-\tau`$ to the identity error. Its eigenvalues are

```math
\widetilde\lambda_e=1-\tau+\tau\lambda_e
\in[1-2\tau,1]
```

for each nonidentity target, and

```math
\|\widetilde\Lambda-\mathrm{id}\|_\diamond
=\tau\|\Lambda-\mathrm{id}\|_\diamond
\leq2\tau.
```

The diamond norm here is the full norm, without the factor of one half. The identity coefficient is known exactly.

One realization leaves the input unchanged with probability $`1-\tau`$ and applies $`\Lambda`$ with probability $`\tau`$, without revealing which happened. Since $`\Lambda`$ may itself apply identity, the actual probability of a nonidentity error can be smaller than $`\tau`$. The known parameter specifies the allowed noise scale.

Use the [fresh-experiment and late-target contract](model.md), with $`n\geq1`$, $`0\leq k\leq n`$, and $`1\leq w\leq n`$. Let

```math
D=n-k,\qquad R=\frac{wD}{n},\qquad
\kappa=\frac{w}{3n-w},\qquad
M_w=\sum_{u=0}^{w}\binom nu3^u.
```

For $`0<\epsilon<\tau/3`$ and $`0<\delta<1/2`$, any learner with a pointwise failure guarantee of at most $`\delta`$ requires

```math
\boxed{
N_{\mathrm{fresh}}
\geq
\frac{(1-2\delta)\tau}{36\epsilon^2}
2^{\kappa D}.
}
```

An explicit learner achieves the stronger simultaneous guarantee with

```math
\boxed{
N_{\mathrm{fresh}}
\leq
\left\lceil
9\tau\epsilon^{-2}3^R
\log\!\left(\frac{2M_w}{\delta}\right)
\right\rceil.
}
```

The notation $`N_{\mathrm{fresh}}`$ in these two bounds denotes the optimal worst-case call count for the relevant learning guarantee. The upper bound also bounds the weaker pointwise task. The exponent constants are not asserted to coincide. The explicit dependence $`\tau/\epsilon^2`$ is shared by both bounds outside their exponential and confidence factors.

## A lower bound that counts the rare informative calls

Use the nonidentity spike channels of [Fresh experiments](fresh_experiments.md), but choose amplitude

```math
a=\frac{3\epsilon}{\tau}\in(0,1).
```

The reference and alternative weak channels are

```math
\widetilde\Lambda_0
=(1-\tau)\mathrm{id}+\tau\mathcal D,\qquad
\widetilde\Lambda_{e,s}
=(1-\tau)\mathrm{id}+\tau\Lambda_{e,s}.
```

At the hidden nonidentity target, their eigenvalues differ by $`s\tau a=s\,3\epsilon`$. Thus a successful estimate distinguishes the null value $`1-\tau`$ from either alternative using the decision rule

```math
|\widehat{\widetilde\lambda}_e-(1-\tau)|
>\frac{3\epsilon}{2}.
```

The error intervals are strictly separated for the stated range of $`\epsilon`$.

Take the same product prior and physical conditioning as in the [weighted prior lemma](weighted_bounds.md#conditioning-on-required-nonidentity-targets):

```math
x=\frac{w}{3(2n-w)},\qquad
e\sim\nu_x(\,\cdot\mid A_w),\qquad
p_A=\nu_x(A_w)\geq\frac14,\qquad
B_x=2^{-\kappa D}.
```

Fix a classical history under the weak null. Let $`q_{\mathrm{id}}(y)`$ and $`q_{\mathcal D}(y)`$ be the next-outcome probabilities for the preparation and POVM selected at that history. The weak null gives

```math
q_0(y)=(1-\tau)q_{\mathrm{id}}(y)
       +\tau q_{\mathcal D}(y).
```

The general input/effect reduction in [Fresh experiments](fresh_experiments.md#the-one-experiment-likelihood) gives a real response $`g_e(y)`$ with

```math
q_{e,s}(y)=q_{\mathcal D}(y)(1+s a g_e(y)),
\qquad
\mathbb E_{e\sim\nu_x(\cdot\mid A_w)}g_e(y)^2
\leq\frac{B_x}{p_A}.
```

Therefore the weak alternative has likelihood

```math
\frac{\widetilde q_{e,s}(y)}{q_0(y)}
=1+s a h_e(y),\qquad
h_e(y)=
\frac{\tau q_{\mathcal D}(y)}{q_0(y)}g_e(y).
```

When $`q_0(y)=0`$, all relevant alternative probabilities vanish and the outcome is omitted. When $`q_{\mathcal D}(y)=0<q_0(y)`$, set $`h_e(y)=0`$. Since $`q_0(y)\geq\tau q_{\mathcal D}(y)`$, the response satisfies $`|h_e(y)|\leq1`$.

The useful bound averages over the next null outcome as well as the hidden target:

```math
\begin{aligned}
\sum_y q_0(y)
\mathbb E_{e\sim\nu_x(\cdot\mid A_w)}h_e(y)^2
&=
\tau^2\sum_{y:q_0(y)>0}
\frac{q_{\mathcal D}(y)^2}{q_0(y)}
\mathbb E_e g_e(y)^2\\
&\leq
\tau\sum_yq_{\mathcal D}(y)
\mathbb E_e g_e(y)^2\\
&\leq\frac{\tau B_x}{p_A}.
\end{aligned}
```

The factor $`\tau`$ comes from this outcome-weighted second moment. Rescaling the eigenvalue displacement alone would miss it.

For a full transcript, the two signed likelihoods are products of factors $`1\pm a h_e`$. Apply the [signed transcript inequality](fresh_experiments.md#the-signed-transcript-bound), and at every step average the displayed node bound against the weak-null history. That history is independent of the hidden label. The resulting laws obey

```math
\mathbb E_e\mathrm{TV}
\left(
\widetilde Q_0,
\frac{\widetilde Q_{e,+}+\widetilde Q_{e,-}}2
\right)
\leq\frac{N a^2\tau B_x}{p_A}.
```

Successful estimation requires the left side to be at least $`1-2\delta`$. Substituting $`a=3\epsilon/\tau`$ gives

```math
N\geq
\frac{(1-2\delta)\tau p_A}{9\epsilon^2 B_x}
\geq
\frac{(1-2\delta)\tau}{36\epsilon^2}2^{\kappa D}.
```

This proof allows arbitrary classical adaptivity and counts every invocation of the weak channel. It does not assume access to a flag revealing which mixture branch occurred, nor does it apply a deterministic-budget lower bound to an unproved expected-query reduction.

## An estimator centered at the identity

Use the [partial-Bell records](partial_bell.md). For a target of weight $`u`$, let $`H_e`$ be the compatibility indicator, let $`p_u=\mathbb E H_e`$, and let $`Y_e`$ be the decoded error character on compatible records.

The appropriate one-record estimator is

```math
Z_e=1-\frac{H_e(1-Y_e)}{p_u}.
```

It is implemented as $`1`$ on an unusable record. Whenever the actual Pauli error is the identity, it is also exactly $`1`$, regardless of the selected settings.

For the [two-qubit example](../learning/WORKED_EXAMPLE.md), a weight-two target has $`p_u=1/3`$. Even on a noiseless identity channel, the original sample $`X_e`$ is three on compatible records and zero otherwise. Its mean is one but its variance is two. The centered sample $`Z_e`$ is always one on that channel, with zero variance.

Set

```math
\Delta_e=1-\widetilde\lambda_e
=\tau(1-\lambda_e)\in[0,2\tau].
```

Independence of compatibility and the error draw, together with $`(1-Y_e)^2=2(1-Y_e)`$, gives

```math
\mathbb E Z_e=\widetilde\lambda_e,\qquad
\mathrm{Var}(Z_e)
=\frac{2\Delta_e}{p_u}-\Delta_e^2
\leq\frac{4\tau}{p_u}.
```

At $`p_u=1/3`$, $`Z_e`$ equals $`-5`$ with probability $`\Delta_e/6`$ and one otherwise. Its mean is $`1-\Delta_e`$ and its variance is $`6\Delta_e-\Delta_e^2`$, exactly as in the general formula. Deviations become rare as the noise scale decreases.

The estimator takes values in $`\{1,\,1-2/p_u\}`$, so

```math
|Z_e-\widetilde\lambda_e|\leq\frac2{p_u}.
```

The Bernstein bound stated in [Partial-Bell estimation](partial_bell.md#unbiased-estimation-and-its-variance) now gives

```math
\Pr\!\left(
\left|
\frac1N\sum_{\ell=1}^{N}Z_{e,\ell}
-\widetilde\lambda_e
\right|\geq\epsilon
\right)
\leq
2\exp\!\left[
-\frac{N\epsilon^2p_u}{8\tau+4\epsilon/3}
\right].
```

For $`\epsilon<\tau/3`$, the denominator is smaller than $`9\tau`$. A union bound over the targets and $`p_u\geq3^{-wD/n}`$ prove the stated sufficient count. Using the exact $`p_w`$ gives the sharper sufficient expression

```math
N=
\left\lceil
9\tau\epsilon^{-2}p_w^{-1}
\log\!\left(\frac{2M_w}{\delta}\right)
\right\rceil.
```

The channel's mixture branch is never observed or inferred. The estimator merely uses the known response of an identity error to remove avoidable variance. Its quantum and classical resource costs are otherwise those of the partial-Bell protocol.

## Coherent processing and the polynomial frontier

The [coherent-memory theorem](coherent_memory.md) also applies to this weak channel class. At every call, count all coherent qubits outside the $`n`$-qubit channel-input register within the $`k`$-qubit budget. Intermediate quantum operations, persistent memory, adaptive measurement, and concatenated calls are allowed.

In the forward hybrid, the common prefix now uses $`\widetilde\Lambda_0`$. The query-cut state is still independent of the hidden target, and the one-call displacement is

```math
\widetilde\Lambda_{e,s}-\widetilde\Lambda_0
=\tau(\Lambda_{e,s}-\mathcal D).
```

Its trace-norm sensitivity has amplitude $`\tau a=3\epsilon`$. The same conditioned rank-fidelity bound therefore gives

```math
\boxed{
N_{\mathrm{coherent}}
\geq
\frac{1-2\delta}{3\epsilon}\,
2^{\kappa D/2}.
}
```

This is a linear inverse-accuracy lower bound. The sharper $`\tau/\epsilon^2`$ lower bound above belongs to the fresh-experiment model.

Now require a fixed relative accuracy

```math
\epsilon=\alpha\tau,\qquad 0<\alpha<\frac13,
```

and fix $`0<\delta<1/2`$. The fresh lower and upper bounds become

```math
\frac{1-2\delta}{36\alpha^2\tau}\,2^{\kappa D}
\leq N_{\mathrm{fresh}}
\leq
\left\lceil
\frac{9}{\alpha^2\tau}\,3^R
\log\!\left(\frac{2M_w}{\delta}\right)
\right\rceil.
```

The coherent lower bound becomes

```math
N_{\mathrm{coherent}}
\geq
\frac{1-2\delta}{3\alpha\tau}\,2^{\kappa D/2}.
```

Averaging independent records divides their variance by the number of calls. At fixed usability probability, the centered variance bound is proportional to $`\tau`$, whereas the required squared error $`\alpha^2\tau^2`$ is proportional to $`\tau^2`$. Their ratio explains the sufficient $`1/\tau`$ call factor; the lower bounds show that a uniformly cheaper dependence on $`\tau`$ cannot resolve fixed relative precision in these models.

The fresh upper protocol is also allowed in the coherent model. Since $`R/3\leq\kappa D\leq R/2`$ and $`\log M_w=O(n)`$, both models have the same joint criterion:

```math
\boxed{
\text{Polynomially many calls at fixed relative accuracy}
\quad\Longleftrightarrow\quad
\frac{w(n-k)}{n}+\log\frac1\tau=O(\log n).
}
```

This holds for arbitrary parameter sequences $`0<\tau(n)\leq1`$. Fixed or inverse-polynomial noise strengths reduce the criterion to the original weight-memory frontier. A superpolynomially small $`\tau`$ requires superpolynomially many calls to resolve a fixed fraction of the allowed noise, even with a full reference register.

If instead $`\epsilon\geq\tau`$, returning the known midpoint $`1-\tau`$ for each nonidentity target succeeds without acquiring any data. For example, absolute error $`1/4`$ with $`\tau=1/4`$ needs no calls, while fixed relative factor $`\alpha=1/4`$ requires error $`1/16`$. Relative precision is therefore essential to interpreting the weak-noise frontier. The finite bounds on this page apply in the explicitly stated range $`\epsilon<\tau/3`$.

## Physical meaning of the promise

The hard channels consist of frequent identity events and rare Pauli errors with a hidden global character bias. They may contain spatial correlations across the entire system. A small diamond distance from the identity does not imply independent local errors, bounded interaction range, sparse noise generators, or weak spatial correlations.

Each call applies the same memoryless channel, and every call is paid for. This construction addresses weak noise in that precise channel class. It supplies a rate refinement and a near-identity realization of the weight-memory law; it does not impose an additional local-noise model.

The [preserved-correlation decision problem](correlation_detection.md) gives a complementary one-bit formulation. Its positive-spike weak-channel family has an efficient detector with the same joint criterion involving weight, memory, and noise strength.
