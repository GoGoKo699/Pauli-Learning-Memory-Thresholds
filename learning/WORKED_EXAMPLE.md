# Two channel qubits and one reference

An unknown, memoryless two-qubit Pauli channel is available. One reference
qubit may remain outside the channel at each invocation. This example shows
what a partial-Bell experiment prepares and records, how the same record
estimates a later requested coefficient, and how an exact correlation becomes
a binary rank test.

The example connects [M07, M12, and M23–M29](MILESTONES.md) to the
[Watrous bridge](WATROUS_BRIDGE.md). The complete constructions and guarantees
are in [partial-Bell learning](../science/partial_bell.md) and
[correlation detection](../science/correlation_detection.md).

## The channel and the delayed question

Write an individual Pauli error as

```math
P_v=P_{(x_1,z_1)}\otimes P_{(x_2,z_2)},\qquad
P_{(x,z)}=i^{xz}X^xZ^z,\qquad
x_i,z_i\in\mathbb F_2.
```

Thus the pairs $`(0,0),(1,0),(0,1),(1,1)`$ represent $`I,X,Z,Y`$.
The channel draws an error label with probability $`p_v`$ and applies its
Pauli operator:

```math
\Lambda(\rho)=\sum_{v\in\mathbb F_2^4}p_vP_v\rho P_v.
```

The draws on separate invocations are independent. The errors on the two
qubits in one draw may be correlated.

Data are acquired before the particular coefficient is requested. Afterward,
suppose the request is for $`P=X\otimes Z`$. Conjugating this operator by
$`P_v`$ multiplies it by

```math
\chi_P(v)=(-1)^{z_1+x_2}.
```

The coefficient to estimate is consequently

```math
\Lambda(P)=\lambda_PP,\qquad
\lambda_P=\sum_v p_v(-1)^{z_1+x_2}.
```

This is the average sign of a commutation parity. The experiment does not
need to reconstruct the entire error distribution.

## One physical setting

At each invocation, independently choose which channel qubit receives the
Bell reference, with probability $`1/2`$ for each choice. Choose a uniformly
random Pauli axis on the other channel qubit. These choices are made without
the later requested label.

Consider the setting with the reference paired to channel qubit 1 and the
$`Z`$ axis on channel qubit 2. Prepare

```math
|\Phi^+\rangle_{S_1A}
=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad |0\rangle_{S_2}.
```

Send $`S_1S_2`$ through the channel once. Measure $`S_1A`$ in the Bell
basis, labeling the outcome by the Pauli error bits $`(x_1,z_1)`$.
Measure $`Z`$ on $`S_2`$ and record the bit $`b_2`$ for the outcome
$`(-1)^{b_2}`$. Because $`S_2`$ started in the positive $`Z`$ eigenstate,
$`b_2=x_2`$.

The three recorded bits are

```math
y=(x_1,z_1,x_2).
```

They determine the requested parity through $`z_1+x_2=y_2+y_3`$.
For instance, $`y=(1,1,1)`$ gives sign $`+1`$. The unobserved bit $`z_2`$
is unnecessary for this coefficient.

There are two queried qubits and one outside reference during the invocation.
The Bell pair therefore consumes the entire $`k=1`$ budget. The three outcome
bits, the paired-site choice, and the local axis are retained classically.
All quantum outputs are measured before the next fresh experiment.

## Usable settings and an unbiased estimate

For $`P=X\otimes Z`$, the setting is usable when the unpaired axis agrees
with the target on that site:

| Paired site | Required unpaired axis | Recorded bits in this setting | Recovered sign |
|---|---|---|---|
| 1 | $`Z`$ on site 2 | $`(x_1,z_1,x_2)`$ | $`(-1)^{z_1+x_2}`$ |
| 2 | $`X`$ on site 1 | $`(x_2,z_2,z_1)`$ | $`(-1)^{x_2+z_1}`$ |

Each paired-site choice has one matching axis out of three. Hence a weight-two
target has usability probability

```math
p_2=\frac12\frac13+\frac12\frac13=\frac13.
```

For a weight-one target, its active site is paired with probability $`1/2`$;
otherwise the local axis must match. Thus

```math
p_1=\frac12+\frac12\frac13=\frac23.
```

These are the exact probabilities for $`n=2,k=1`$. For our weight-two target,
assign each record the value

```math
T_P=
\begin{cases}
3\chi_P(v),&\text{if its setting is usable for }P,\\
0,&\text{otherwise}.
\end{cases}
```

The compatibility choice is independent of the channel error. Therefore

```math
\mathbb E T_P=\lambda_P,\qquad
\mathbb E T_P^2=3,\qquad
\mathrm{Var}(T_P)=3-\lambda_P^2.
```

The factor three compensates for using one third of the records. A sample
can have magnitude three even though the coefficient lies in $`[-1,1]`$.
The estimate is the average of the sample values, and its finite confidence
guarantee follows from the variance bound in the
[general construction](../science/partial_bell.md#unbiased-estimation-and-its-variance).

For illustration, these three possible records would give:

| Record | Paired site and unpaired axis | Syndrome in that setting's order | $`T_P`$ |
|---|---|---|---|
| 1 | Site 1; $`Z`$ on site 2 | $`(1,1,1)`$ | $`3`$ |
| 2 | Site 2; $`X`$ on site 1 | $`(0,0,1)`$ | $`-3`$ |
| 3 | Site 1; $`X`$ on site 2 | $`(0,0,1)`$ | $`0`$ |

The third setting does not reveal the needed $`x_2`$ bit and is assigned
zero. The displayed average happens to be zero; three illustrative records
do not establish a small error bar. The same stored data can be evaluated
for any of the 15 nonidentity two-qubit Paulis, using that target's matching
rule and $`p_1`$ or $`p_2`$. The identity coefficient is already known to be one.

## An exactly preserved correlation becomes a rank constraint

Now change the output task to one bit. The null channel is complete
depolarization, while the alternative preserves one hidden nonidentity Pauli:

```math
\mathrm{Dep}(Q)=\frac{I_4\mathrm{Tr}Q}{4},
\qquad
\Lambda_P^1(Q)=
\frac{I_4\mathrm{Tr}Q+P\mathrm{Tr}(PQ)}{4}.
```

The same tester must work for every allowed hidden $`P`$, which is not revealed
after acquisition. Here $`Q`$ denotes a matrix argument of the channel.
This is the [positive-spike promise](../science/correlation_detection.md#1-promise-and-finite-theorem).

Under the null, $`v`$ is uniform on $`\mathbb F_2^4`$. Under the alternative
with hidden $`P=X\otimes Z`$, it is uniform on

```math
\{v:z_1+x_2=0\}.
```

Return to the compatible setting with site 1 paired and $`Z`$ on site 2.
Its null syndrome is uniform on all eight vectors of $`\mathbb F_2^3`$.
Its alternative syndrome is uniform on the four vectors

```math
(0,0,0),\quad (1,0,0),\quad (0,1,1),\quad (1,1,1).
```

Every alternative row obeys $`y_2+y_3=0`$. Stacking any number of these rows
therefore gives a binary matrix of rank at most two. For example,

```math
Y=
\begin{pmatrix}
1&0&0\\
0&1&1\\
1&1&1
\end{pmatrix},
\qquad \mathrm{rank}_{\mathbb F_2}Y=2.
```

The third row is the sum of the first two over $`\mathbb F_2`$.
The algorithm only needs to find a rank deficiency. It can eliminate rows
without identifying which physical Pauli generated the constraint.

A null sample can also have deficient rank by chance. For $`L`$ independent
null rows and any fixed nonzero linear functional, all rows satisfy its
homogeneous equation with probability $`2^{-L}`$. There are seven nonzero
functionals on $`\mathbb F_2^3`$, so a union bound gives

```math
\Pr_{\mathrm{Dep}}\{\mathrm{rank}Y<3\}
\le 7\,2^{-L}.
```

Random settings handle the fact that the hidden Pauli is unknown. The
algorithm chooses $`J`$ settings, repeats each for $`L`$ invocations, and
outputs “alternative” if any block has rank below three. The chance that no
setting is compatible with a weight-two hidden Pauli is $`(2/3)^J`$.
The union bound controls false positives across all $`J`$ blocks.

## A complete finite choice and the weak-channel variant

Use the rank theorem's sufficient parameters with failure allowance
$`\delta=1/10`$. Here $`m=n+k=3`$ and $`R=w(n-k)/n=1`$. At full mixture
strength $`\tau=1`$,

```math
J=\left\lceil3\ln20\right\rceil=9,\qquad
L=\left\lceil2(3\ln2+\ln180)\right\rceil=15,\qquad
N=JL=135.
```

For a hidden weight-two Pauli, the missed-compatibility probability is
$`(2/3)^9<0.05`$. Under the null, the probability that any block is deficient
is at most $`9\cdot7\cdot2^{-15}<0.05`$. A hidden weight-one Pauli has higher
compatibility probability. These are sufficient finite bounds for the stated
promise, without a claim of optimal constants.

For known $`0<\tau\le1`$, replace the hypotheses by

```math
\Gamma_0=(1-\tau)\mathrm{Id}+\tau\mathrm{Dep},\qquad
\Gamma_P=(1-\tau)\mathrm{Id}+\tau\Lambda_P^1.
```

The identity branch emits the zero syndrome. It preserves every homogeneous
constraint, so the compatible alternative still has rank at most two.
The null syndrome law becomes

```math
q_0(y)=(1-\tau)\mathbf1_{\{y=0\}}+\frac{\tau}{8}.
```

A nonzero null parity is violated with probability $`\tau/2`$.
Consequently, its rank-deficiency bound is

```math
\Pr_{\Gamma_0}\{\mathrm{rank}Y<3\}
\le 7(1-\tau/2)^L.
```

At $`\tau=1/4`$, the same sufficient prescription gives $`J=9`$,
$`L=59`$, and $`N=531`$. More repetitions are needed because most invocations
produce the uninformative zero syndrome. The single-bit output and the
one-qubit reference budget are unchanged. The
[general theorem](../science/correlation_detection.md#5-the-linear-rank-algorithm)
accounts for these rare informative events for arbitrary $`n,k,w,\tau`$.

## What the example contributes to the full story

The example makes three operations concrete: references reveal additional
error bits, compatible settings support reusable coefficient estimates, and
an exact hidden parity can be detected through rank alone. The general
construction bounds the compatibility probability by
$`3^{-w(n-k)/n}`$. The [weighted inequalities](../science/weighted_bounds.md)
and [coherent hybrid](../science/coherent_memory.md) supply the complementary
universal lower bound.

The timing of the coefficient request is a load-bearing assumption. If a
single Pauli is known before acquisition, prepare positive eigenstates of its
local factors and measure their output parity on every call. That experiment
can estimate the known coefficient without a reference. The
[full learning task](../science/model.md#learning-a-reusable-record)
requires one acquisition record to support any later requested member of the
complete weight-bounded family.

The rank detector also uses a precise promise: the alternative correlation is
exactly preserved. Approximate parity preservation would replace the
homogeneous support condition with a different statistical problem. The
small example illustrates the implemented upper protocols; the asymptotic
memory threshold follows from their general analysis together with the
universal converse.
