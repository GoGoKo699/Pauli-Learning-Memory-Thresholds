# Detecting one preserved Pauli correlation

This promise problem has a single-bit answer and an efficient constructive
algorithm at the same support–memory frontier as channel learning. The positive
Pauli-spike detection problem is established in
[ChenGong2025](../references/RELATED_WORK.md#chengong2025), Problem 3. Here the
hidden Pauli is restricted by weight, the lower bound permits the full coherent
processor in [the model](model.md), and the construction includes a known
identity-mixture strength.

## 1. Promise and finite theorem

Let $`n\geq1`$, $`0\leq k\leq n`$, $`1\leq w\leq n`$,
$`0<\tau\leq1`$, and $`0<\delta<1/2`$. Put $`d=2^n`$,
$`D=n-k`$, and $`R=wD/n`$. The unknown, memoryless channel is promised to be
either

```math
\Gamma_0=(1-\tau)\operatorname{Id}+\tau\operatorname{Dep},
\qquad \operatorname{Dep}(X)=\frac{I\operatorname{Tr}X}{d},
```

or

```math
\Gamma_P=(1-\tau)\operatorname{Id}+\tau\Lambda_P,
\qquad
\Lambda_P(X)=\frac{I\operatorname{Tr}X+P\operatorname{Tr}(PX)}{d},
\qquad 1\leq |P|\leq w.
```

The parameters, including $`\tau`$ and the allowed weight range, are known.
The nonidentity Pauli $`P`$ is hidden and is never supplied to the tester. The
tester must output 0 under $`\Gamma_0`$ and 1 under every allowed
$`\Gamma_P`$, with error at most $`\delta`$ for each promised channel.

Under the null, every nonidentity Pauli eigenvalue equals $`1-\tau`$. Under an
alternative, the eigenvalue of $`P`$ equals 1 and every other nonidentity Pauli
eigenvalue equals $`1-\tau`$. Thus the question is whether the specified
baseline contains one unknown, exactly preserved correlation. At $`\tau=1`$
the baseline is complete depolarization.

**Theorem D1.** Every tester allowed by the coherent model, using at most
$`k`$ qubits outside the queried $`n`$-qubit register at each invocation, obeys

```math
N\geq\frac{1-2\delta}{\tau}
  2^{\frac{w(n-k)}{2(3n-w)}}.
\tag{D1}
```

The bound allows arbitrary retained quantum states, intermediate quantum
operations, measurements, classical feedback, and channel concatenation. It
counts every channel call and allows unlimited classical computation.

Conversely, a protocol with fresh partial-Bell probes succeeds using $`N=JL`$
calls, where

```math
\begin{aligned}
m&=n+k,\\
J&=\left\lceil 3^R\ln\frac{2}{\delta}\right\rceil,\\
L&=\left\lceil\frac{2}{\tau}
    \left(m\ln2+\ln\frac{2J}{\delta}\right)\right\rceil.
\end{aligned}
\tag{D2}
```

Its classical processing is polynomial in $`N`$ and $`n`$. For fixed error
probability in $`(0,1/2)`$, polynomially many calls and polynomial total
computation are therefore achievable if and only if

```math
\boxed{\frac{w(n-k)}{n}+\ln\frac1\tau=O(\log n).}
\tag{D3}
```

This is an asymptotic statement for parameter sequences as $`n\to\infty`$.
The same sufficient condition holds for inverse-polynomial failure probability.
The finite bounds (D1)–(D2) state the confidence dependence explicitly.

## 2. A succinct physical channel family

Use binary symplectic labels $`e,v\in\mathbb F_2^{2n}`$ for Hermitian Pauli
operators, and let $`[e,v]`$ be their commutation parity. For the alternative
$`P=P_e`$, the Pauli-error distributions are

```math
p_0(v)=\frac1{4^n},
\qquad
p_e(v)=\frac{1+(-1)^{[e,v]}}{4^n}.
\tag{D4}
```

Since $`e\neq0`$, its symplectic functional is nonzero. Consequently
$`p_e`$ is the uniform distribution on the linear hyperplane
$`H_e=\{v:[e,v]=0\}`$, which has $`2^{2n-1}`$ elements. This proves
complete positivity and trace preservation of $`\Lambda_P`$ directly.
Its Fourier coefficients are 1 at the identity and at $`P`$, and zero at
every other Pauli.

To sample an error from $`\Gamma_P`$, first choose the identity branch with
probability $`1-\tau`$. Otherwise choose $`2n-1`$ independent uniform bits
and solve for one remaining bit with nonzero coefficient in $`[e,v]`$.
Apply the resulting tensor product of local Pauli gates. The null uses a
uniform $`2n`$-bit error label in the second branch. Beyond the single
Bernoulli branch draw, both samplers take $`O(n)`$ classical bit operations
and at most $`n`$ single-qubit Pauli gates per use. The hidden label has an
$`O(n)`$-bit full description, or a support
and axis description of length $`O(w\log n)`$. The learner receives ordinary
channel access, not the hidden label, sampled error, or branch flag.

At $`\tau=1`$, the alternative also has the measure-and-prepare form

```math
\Lambda_P(X)=\sum_{b\in\{+1,-1\}}
       \operatorname{Tr}(E_bX)\sigma_b,
\qquad
E_b=\frac{I+bP}{2},\quad
\sigma_b=\frac{I+bP}{d}.
\tag{D5}
```

It is therefore entanglement breaking: it records one parity and randomizes
within its eigenspaces. The identity mixtures for smaller $`\tau`$ need
not be entanglement breaking. Both hypotheses satisfy

```math
\|\Gamma_i-\operatorname{Id}\|_\diamond\leq2\tau,
\qquad
\|\Gamma_P-\Gamma_0\|_\diamond=\tau.
\tag{D6}
```

The first inequality follows from convexity and the distance bound 2 for
channels. For the equality, (D4) gives an $`\ell_1`$ distance of
$`\tau`$ between the error distributions. The triangle inequality for the
Pauli conjugation maps gives the same upper bound in diamond norm, and a
maximally entangled input attains it because the different Pauli errors
produce orthogonal Bell states. This witness establishes a channel norm;
it does not grant the tester uncounted reference qubits.

## 3. Direct coherent lower bound

This proof applies to the decision task itself. It does not infer testing
hardness from an eigenvalue-learning lower bound.

Use the product Pauli prior and its restriction from
[the weighted bounds](weighted_bounds.md):

```math
x=\frac{w}{3(2n-w)},\qquad
\nu_x(e)=\frac{x^{|e|}}{(1+3x)^n},\qquad
\mathcal A=\{e:1\leq|e|\leq w\},\qquad
p_{\mathcal A}=\nu_x(\mathcal A)\geq\frac14.
```

Write $`\pi=\nu_x(\,\cdot\mid\mathcal A)`$ and

```math
B=2^{-\frac{w(n-k)}{3n-w}}.
```

The coherent response lemma in [coherent_memory.md](coherent_memory.md)
states that every query-cut state $`\omega_{SA}`$, with
$`\dim A\leq2^k`$, satisfies

```math
g_e(\omega)=
\left\|\operatorname{Tr}_S[(P_e\otimes I)\omega]\right\|_1,
\qquad
\mathbb E_{e\sim\nu_x}g_e(\omega)^2\leq B.
\tag{D7}
```

It applies to mixed inputs without adding a purifying register outside the
budget. For classical histories, it applies separately to each conditional
quantum state. Conditioning the prior and using Cauchy–Schwarz gives

```math
\mathbb E_{e\sim\pi}g_e(\omega)
\leq\sqrt{B/p_{\mathcal A}}.
\tag{D8}
```

For any such input, the single-call difference is

```math
[(\Gamma_{P_e}-\Gamma_0)\otimes\operatorname{id}_A](\omega)
=\tau\frac{P_e}{d}\otimes
  \operatorname{Tr}_S[(P_e\otimes I)\omega],
```

and has trace norm $`\tau g_e(\omega)`$. Compare the actual protocol by
hybrids with the first $`j`$ calls equal to $`\Gamma_0`$ and all remaining
calls equal to $`\Gamma_{P_e}`$. At the differing invocation, the preceding
null calls have produced a classical–quantum state independent of $`e`$.
The following operations, including all feedback, form the same
$`e`$-dependent trace-preserving quantum map on each side of that replacement.
Trace-distance contraction, (D8), and the triangle inequality imply

```math
\mathbb E_{e\sim\pi}\operatorname{TV}(Q_e,Q_0)
\leq\frac{N\tau}{2}\sqrt{B/p_{\mathcal A}},
\tag{D9}
```

where $`Q_e,Q_0`$ are the final record distributions. The processor may keep
quantum memory throughout; the final decision measurement is part of the
protocol.

Let $`T=1`$ denote the tester's alternative decision. Success for every
promised channel requires

```math
\Pr_{Q_0}(T=1)\leq\delta,
\qquad
\Pr_{Q_e}(T=1)\geq1-\delta
\quad(e\in\mathcal A).
```

Thus $`\operatorname{TV}(Q_e,Q_0)\geq1-2\delta`$ for every allowed
$`e`$. Combining with (D9) yields

```math
N\geq
\frac{2(1-2\delta)\sqrt{p_{\mathcal A}}}{\tau\sqrt B}
\geq\frac{1-2\delta}{\tau}
   2^{\frac{w(n-k)}{2(3n-w)}},
```

which proves (D1). No random sign and no revelation of the hidden label
are needed.

For the full family $`w=n`$, the same proof can instead use the uniform
Pauli prior $`x=1`$. Then $`B=2^{-D}`$ and
$`p_{\mathcal A}=1-4^{-n}`$, giving the stronger endpoint bound

```math
N\geq\frac{2(1-2\delta)\sqrt{1-4^{-n}}}{\tau}
  2^{(n-k)/2}.
\tag{D1a}
```

The weight-dependent choice above gives one explicit formula valid over
the entire allowed range of $`w`$.

## 4. Partial-Bell settings expose a linear syndrome

Choose a uniform $`k`$-site subset $`K`$. On those sites, prepare Bell pairs
with the $`k`$ reference qubits and measure each pair in the Bell basis after
the call. On each remaining site choose an independent, uniform axis from
$`\{X,Y,Z\}`$, prepare its positive eigenstate, and measure in the same
basis afterward. These are the probes in
[partial_bell.md](partial_bell.md).

For a Pauli error labelled $`v`$, a Bell outcome gives its two local error
bits; a local-axis outcome gives its commutation bit with that axis.
Therefore the complete record is a linear syndrome

```math
y=Av\in\mathbb F_2^m,\qquad m=n+k,
\tag{D10}
```

where $`A`$ has full row rank. The rows have disjoint site support, except
for the two independent coordinate rows at each Bell site.

Let $`\ell_e`$ be the row vector representing $`v\mapsto[e,v]`$ in
ordinary binary coordinates. The setting is **compatible** with the hidden
Pauli if and only if $`\ell_e\in\operatorname{row}(A)`$. This is equivalent
to every nonidentity local axis of $`P_e`$ outside $`K`$ agreeing with the
chosen measurement axis.

For $`u=|e|`$, the compatibility probability is

```math
q_e=\mathbb E_K 3^{-|\operatorname{supp}(e)\setminus K|}
\geq 3^{-u(n-k)/n}\geq3^{-R}.
\tag{D11}
```

The first inequality is Jensen's inequality. The exact hypergeometric sum
is given in [partial_bell.md](partial_bell.md).

Two elementary projection facts determine the test:

1. Under $`\Gamma_0`$, the syndrome law is
   $`(1-\tau)\delta_0+\tau\operatorname{Uniform}(\mathbb F_2^m)`$.
2. Under $`\Gamma_{P_e}`$ in a compatible setting, there is a unique
   nonzero row $`c`$ with $`cA=\ell_e`$. Every syndrome obeys $`cy=0`$,
   including the identity-branch syndrome. In an incompatible setting the
   syndrome law equals the null law.

For completeness, the restriction of $`A`$ to $`H_e`$ has image
$`\ker c`$ in the compatible case. Otherwise the stacked matrix with rows
$`A`$ and $`\ell_e`$ has rank $`m+1`$, so restricting to $`H_e`$ still
maps onto all of $`\mathbb F_2^m`$. Uniform inputs project uniformly because
all fibers of a linear map have the same cardinality.

## 5. The linear-rank algorithm

Choose $`J,L`$ as in (D2). Draw $`J`$ independent settings. For each one,
hold the setting fixed for $`L`$ independent fresh channel calls and form
the binary matrix whose rows are the **raw** syndrome vectors. Output 1
if any block has rank less than $`m`$; otherwise output 0. No hidden-label
search or enumeration of the allowed Paulis is performed.

Under an alternative, a compatible block always has deficient rank.
Equation (D11) bounds the probability that none of the settings is compatible:

```math
(1-q_e)^J\leq e^{-Jq_e}\leq\delta/2.
\tag{D12}
```

Under the null, for each nonzero linear form $`c`$,

```math
\Pr(cy=0)=1-\tau/2.
```

A block has deficient rank only if all its rows lie in the kernel of at
least one such form. Independence within the block gives

```math
\begin{aligned}
\Pr(\operatorname{rank}<m)
&\leq(2^m-1)(1-\tau/2)^L\\
&\leq2^m e^{-\tau L/2}
\leq\frac{\delta}{2J}.
\end{aligned}
\tag{D13}
```

A union bound over blocks makes the false-positive probability at most
$`\delta/2`$. Equation (D12) bounds the false-negative probability by the
same amount. This proves (D2), with spare error probability.

Streaming Gaussian elimination processes each syndrome in $`O(m^2)`$ bit
operations and keeps an $`O(m^2)`$-bit basis. The quantum operations per call
are local preparations, Bell operations, and local measurements. In particular,

```math
N=O\!\left(\tau^{-1}3^R
       [n+R+\log(1/\delta)]\log(1/\delta)\right).
\tag{D14}
```

Since $`w(n-k)/[2(3n-w)]`$ lies between $`R/6`$ and $`R/4`$,
(D1) gives necessity in (D3), and (D14) gives sufficiency. The identity
mixture preserves a zero parity exactly, so raw linear rank suffices;
affine differences are unnecessary.

## 6. Scope and verification

The promise is exact preservation of one Pauli correlation against the specified
null family. It is not a test for every nondepolarizing channel, and the
algorithm does not identify the hidden Pauli. If the distinguished eigenvalue
is less than 1, the projected parity is noisy and the rank test is no longer
valid. The theorem does not establish an efficient generic noisy-parity search
algorithm or resilience to arbitrary preparation, measurement, or reference
noise.

The weak-noise family contains rare, potentially global, correlated error
events. Closeness to the identity does not make those events independent,
geometrically local, or generated by a sparse local noise model. The promise
includes every support and axis of weight at most $`w`$; the lower bound does
not apply to every smaller known family of the same maximal weight.

[verify_syndromes.py](../verification/verify_syndromes.py) exhausts all 84
partial-Bell/local-axis settings and 4,284 setting–hidden-label pairs for
$`1\leq n\leq3`$. It checks the exact projection distributions,
compatibility probabilities, preserved weak-noise constraints, and finite
$`J,L`$ choices. It also compares the exact weak-null rank recurrence with
37,802 explicitly enumerated sample sequences and checks its union bound.
The deterministic output is retained in
[verify_syndromes.json](../verification/expected/verify_syndromes.json).
These are checks of the finite algebra and implementation; the general
lower and upper bounds are proved above and in the linked proof homes.
