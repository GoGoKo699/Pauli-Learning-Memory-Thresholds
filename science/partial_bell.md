# An explicit partial-Bell learning protocol

A channel call can reveal a complete local Pauli error label at each site paired with a reference qubit. At an unpaired site, a local Pauli preparation and measurement reveal one commutation bit. Randomizing the paired sites spreads the reference budget across the possible targets.

This page gives the construction, its exact usability probability, and its finite confidence bound. It uses fresh experiments and is therefore also allowed in the broader [coherent-memory model](coherent_memory.md). The unknown channel and the late-target contract are defined in [Model and tasks](model.md).

## What one experiment records

Write the Pauli channel as

```math
\Lambda(\rho)=\sum_v p(v)P_v\rho P_v,\qquad
\lambda_e=\sum_v p(v)(-1)^{[e,v]}.
```

For purposes of analyzing this protocol, a call is a draw of a Pauli error label $`v`$ from the unknown distribution $`p`$. Errors at different sites of that draw may be arbitrarily correlated.

Perform each experiment as follows.

1. Choose a uniformly random $`k`$-element subset $`K`$ of the $`n`$ system sites.
2. At each site in $`K`$, prepare a Bell pair between the system qubit and one reference qubit. At every other site $`i`$, choose an independent, uniform axis $`a_i\in\{X,Y,Z\}`$ and prepare its $`+1`$ eigenstate.
3. Apply the unknown channel once to all $`n`$ system qubits.
4. Measure each paired system-reference pair in the Bell basis. Measure every unpaired output qubit along its preparation axis.
5. Store $`K`$, the unpaired axes, the Bell labels, and the unpaired measurement signs.

The Bell label identifies $`v_i`$ on a paired site, with the labels fixed by the convention $`(P_{v_i}\otimes I)|\Phi^+\rangle`$. Overall Pauli phases do not affect that label. At an unpaired site the recorded sign is exactly

```math
b_i=(-1)^{[a_i,v_i]}.
```

Indeed, applying a Pauli error to an eigenstate of the chosen axis either preserves or flips its eigenvalue according to commutation. These observations hold conditional on the complete error label, so they require no spatial independence assumption.

The primitive Bell and local-Pauli measurements are established channel-learning tools; see [ChenZhouSeifJiang2022](../references/RELATED_WORK.md#chenzhouseifjiang2022) and [KimOh2026](../references/RELATED_WORK.md#kimoh2026). The random partial-Bell construction here is stated explicitly so that its resource count and performance can be assessed without assuming a more powerful oracle.

## Compatibility with a requested target

Let the later request be a Pauli $`P_e`$ of weight $`u`$. A record is usable for this target if every nonidentity target factor at an unpaired site agrees with that site's chosen axis. Write

```math
H_e=
\mathbf 1\{a_i=e_i
\text{ for every }i\in\mathrm{supp}(e)\setminus K\}.
```

On a usable record, multiply the relevant Bell-label commutation characters and the unpaired signs:

```math
Y_e=
\prod_{i\in K\cap\mathrm{supp}(e)}
 (-1)^{[e_i,v_i]}
\prod_{i\in\mathrm{supp}(e)\setminus K}b_i.
```

The result is the complete error character,

```math
Y_e=(-1)^{[e,v]}\in\{-1,+1\}.
```

On an unusable record, the algorithm does not need to reconstruct this character. For expectation calculations one can still use the underlying character of the actual error, multiplied by the zero indicator $`H_e`$.

### Exact usability probability

Put $`D=n-k`$. Conditional on $`K`$, let $`M=|\mathrm{supp}(e)\setminus K|`$ be the number of unpaired target sites. All required axes agree with probability $`3^{-M}`$. Thus usability depends only on the target weight:

```math
p_u=\Pr(H_e=1)=\mathbb E_K\,3^{-M}.
```

The exact expression is

```math
\boxed{
p_u=
\frac{1}{\binom nk}
\sum_{j=0}^{u}
\binom uj\binom{n-u}{k-j}\,3^{-(u-j)}.
}
```

Here an out-of-range binomial coefficient is zero, and $`j`$ is the number of paired target sites. Equivalently,

```math
p_u=
\frac{1}{\binom nu}
\sum_{m=0}^{u}
\binom Dm\binom{k}{u-m}\,3^{-m}.
```

These formulas also cover $`u=0`$, for which $`p_0=1`$. The settings are selected independently of the channel, so $`H_e`$ is independent of its Pauli error draw.

Since $`\mathbb E M=uD/n`$ and the function $`3^{-m}`$ is convex,

```math
p_u\geq3^{-uD/n}.
```

Moreover, $`p_u`$ is nonincreasing in $`u`$. To see this, choose nested supports of sizes $`u`$ and $`u+1`$ and use the same random subset $`K`$. Adding one target site multiplies $`3^{-M}`$ by either $`1`$ or $`1/3`$. Permutation symmetry makes this expectation depend only on the support size. Therefore,

```math
\min_{0\leq u\leq w}p_u=p_w\geq3^{-wD/n}.
```

## Unbiased estimation and its variance

For a weight-$`u`$ request, define the one-record estimator

```math
X_e=\frac{H_eY_e}{p_u}.
```

It is implemented as zero on unusable records and as the decoded sign divided by $`p_u`$ on usable records. Independence of the settings and the error gives the exact moments

```math
\mathbb E X_e=\lambda_e,\qquad
\mathbb E X_e^2=\frac1{p_u},\qquad
\mathrm{Var}(X_e)=\frac1{p_u}-\lambda_e^2
\leq\frac1{p_u}.
```

Because $`p_u\leq1`$ and $`|\lambda_e|\leq1`$,

```math
|X_e-\lambda_e|
\leq\frac1{p_u}+1
\leq\frac2{p_u}.
```

Run the experiment with independent settings on $`N`$ independent calls and use

```math
\widehat\lambda_e=\frac1N\sum_{\ell=1}^{N}X_{e,\ell}.
```

Bernstein's inequality for independent, centered random variables with variance at most $`\sigma^2`$ and absolute value at most $`b`$ states

```math
\Pr\!\left(
\left|\frac1N\sum_{\ell=1}^{N}Z_\ell\right|\geq\epsilon
\right)
\leq
2\exp\!\left[
-\frac{N\epsilon^2}{2\sigma^2+2b\epsilon/3}
\right].
```

Substituting the preceding moments yields

```math
\Pr(|\widehat\lambda_e-\lambda_e|\geq\epsilon)
\leq
2\exp\!\left[
-\frac{N\epsilon^2p_u}{2+4\epsilon/3}
\right].
```

For $`0<\epsilon\leq1`$, the denominator is smaller than $`4`$. The sample cost is thus proportional to $`p_u^{-1}`$. A range-only Hoeffding estimate would lose the variance information and give an unnecessary factor $`p_u^{-2}`$.

## Simultaneous guarantee

Let

```math
M_w=\sum_{u=0}^{w}\binom nu3^u.
```

The identity eigenvalue is known to be $`1`$ and can be returned exactly. Including it in $`M_w`$ is a harmless counting convenience. A union bound over the remaining targets shows that, for $`0<\delta<1`$,

```math
N=
\left\lceil
4\epsilon^{-2}p_w^{-1}
\log\!\left(\frac{2M_w}{\delta}\right)
\right\rceil
```

is sufficient to ensure

```math
\Pr\!\left(
\max_{1\leq|e|\leq w}
|\widehat\lambda_e-\lambda_e|\leq\epsilon
\right)\geq1-\delta.
```

All logarithms in confidence bounds are natural. Replacing the exact usability probability by its lower bound gives the convenient uniform guarantee

```math
\boxed{
N=
\left\lceil
4\epsilon^{-2}
3^{\,w(n-k)/n}
\log\!\left(\frac{2M_w}{\delta}\right)
\right\rceil
\quad\text{is sufficient.}
}
```

No simultaneous independence between different target estimators is assumed. They can use the same records and be strongly correlated; the union bound still applies.

## Physical and classical resources

Every experiment uses exactly $`n`$ channel-input qubits, at most $`k`$ reference qubits, one ordinary channel call, and $`O(n)`$ local or Bell preparation and measurement operations. A fixed ordering of the sites in $`K`$ fixes the assignment to reference qubits. No purification of the channel, controlled call, inverse call, or QRAM is used.

A record can be stored in $`O(n)`$ bits: an $`n`$-bit subset mask, one axis label and measurement sign per unpaired site, and one two-bit Bell label per paired site. The complete record therefore occupies $`O(nN)`$ bits. The exact probabilities $`p_u`$ are rational numbers obtainable by polynomial-time integer arithmetic from the binomial formula.

After acquisition, one requested coefficient is evaluated by scanning the records, checking compatibility, and multiplying the available signs. This requires $`O(nN)`$ elementary bit inspections and sign operations, plus polynomial arithmetic for the normalization. The protocol returns the record and its evaluation rule; it does not print an exponentially long list of coefficients.

The simultaneous event above supports every later request, including requests selected using the record. Its acquisition cost includes only a logarithmic target-count factor. Since $`M_w\leq4^n`$, that factor is $`O(n+\log(1/\delta))`$.

## Endpoints and related tasks

With $`k=n`$, every record is usable and $`p_u=1`$: the procedure is ordinary Bell sampling. With $`k=0`$, one has $`p_u=3^{-u}`$: the procedure is random local-Pauli sampling. Intermediate reference budgets give the exponent $`w(n-k)/n`$ up to constants. The exact expression for $`p_u`$ can improve finite-parameter performance relative to the Jensen estimate; this construction does not assert an optimal exponential constant.

Together with the [fresh-experiment lower bound](fresh_experiments.md), this proves the polynomial-query frontier in that model. The [coherent lower bound](coherent_memory.md) shows that retaining and reusing a bounded coherent register does not change that frontier.

For a weak channel, subtracting the known identity baseline reduces the estimator's variance; see [Weak channels](weak_noise.md#an-estimator-centered-at-the-identity). Repeating a fixed partial-Bell setting also produces the linear syndromes used by the efficient [preserved-correlation detector](correlation_detection.md).
