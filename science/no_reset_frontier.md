# Coherent width and initial purity without resets

The weight–memory law in [the original model](model.md) counts coherent qubits beside each queried register while permitting new probe preparation, resets and a retained classical history. A fixed processor with no replenished purity has an additional obstruction. Already for weight one and a retained coefficient of one half, logarithmic initial purity cannot support a constant-error detector, for any finite query count.

This result connects this repository to its sister, [Quantum Learning Without Resets](https://github.com/GoGoKo699/Quantum-Learning-Without-Resets). The present page supplies the common task, resource comparison and width consequences. The [complete shared relative-entropy proof](https://github.com/GoGoKo699/Quantum-Learning-Without-Resets/blob/main/science/entropy_bound.md) has its authoritative home in that repository. The original weight–memory proofs and constructive protocols remain authoritative here.

## Common attenuated-spike task

Let $`n\geq1`$, $`d=2^n`$, and let $`\mathcal A_1=\{e:|e|=1\}`$ contain the $`M=3n`$ nonidentity weight-one Pauli operators. The unknown, memoryless channel is fixed throughout a run and is either

```math
\mathcal D(X)=\frac{I\mathrm{Tr}X}{d}
```

or, for one hidden $`e\in\mathcal A_1`$,

```math
\mathcal E_{e,\lambda}(X)
=\frac{I\mathrm{Tr}X+\lambda P_e\mathrm{Tr}(P_eX)}{d},
\qquad \lambda=\frac12.
```

These are CPTP, unital Pauli channels. Their Pauli-error probabilities are $`4^{-n}[1+\lambda(-1)^{[e,v]}]`$, which are nonnegative and sum to one. The alternative retains coefficient $`1/2`$ at $`P_e`$ and erases every other nonidentity coefficient. This attenuation parameter $`\lambda`$ differs from the identity-mixture strength $`\tau`$ in [the exactly preserved-correlation detector](correlation_detection.md).

The processor consists of the $`n`$-qubit queried register $`S`$ and a fixed protected register $`A`$. It starts in a known state $`\rho_{\mathrm{in}}`$ independent of the hypothesis. Each ordinary channel call acts on $`S`$. Between calls, known CPTP controls act jointly on $`SA`$ and are unital on the entire processor. All retained records belong to this initialized processor. No fresh pure probe, reset, newly clean record, environment output, inverse or controlled use of the unknown channel is supplied. Nonselective dephasing is allowed. A recorded measurement is allowed only when its complete implementation respects these resource conditions.

After $`T`$ calls, one common terminal measurement must distinguish the null from every alternative. With acceptance denoting the alternative, worst-case error at most $`0<\delta<1/2`$ means

```math
p_0\leq\delta,\qquad p_e\geq1-\delta
\quad(e\in\mathcal A_1).
```

Write $`D=\dim(SA)`$ for the dimension of the complete initialized processor. Define initial entropy deficit in bits and dimension-normalized collision purity by

```math
\begin{aligned}
C&=\log_2D-H(\rho_{\mathrm{in}}),\\
\mathcal P&=D\mathrm{Tr}(\rho_{\mathrm{in}}^2).
\end{aligned}
```

Here $`H(\rho)=-\mathrm{Tr}(\rho\log_2\rho)`$ and relative entropy is also measured in bits. For $`c`$ initially pure qubits tensored with maximally mixed qubits, $`C=c`$ and $`\mathcal P=2^c`$. For general initial states, $`C\leq\log_2\mathcal P`$; these resource parameters should not be interchanged.

## The immediate collision-purity restriction

The sister repository's [common-effect collision bound](https://github.com/GoGoKo699/Quantum-Learning-Without-Resets/blob/main/science/decision_bound.md) restricts directly to the $`3n`$ weight-one labels: restricting the sums in its forward and backward orthogonality budgets preserves their upper bounds. It gives, for the uniform alternative mixture $`\bar\rho_T=M^{-1}\sum_e\rho_T^e`$,

```math
D_{\mathrm{tr}}(\bar\rho_T,\rho_T^0)
\leq\min\left\{1,
\frac{\sqrt{\mathcal P-1}}{2M}\right\},
\qquad D_{\mathrm{tr}}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

For product clean/mixed initialization, error $`\delta`$ therefore requires

```math
2^c-1\geq4(3n)^2(1-2\delta)^2.
```

At $`\delta=1/3`$, this is $`c\geq\log_2(1+4n^2)`$. It is an inherited restricted-label corollary. It leaves logarithmic purity possible and does not settle the joint question.

## A stronger initial-entropy-deficit obstruction

For every finite $`T`$ and every protected dimension, the shared entropy theorem proves

```math
\boxed{
\sum_{e\in\mathcal A_1}
D_{\mathrm{bits}}(\rho_T^0\|\rho_T^e)
\leq\frac34 C.
}
```

Here ordinary quantum relative entropy in bits is

```math
D_{\mathrm{bits}}(\rho\|\sigma)
=\mathrm{Tr}[\rho(\log_2\rho-\log_2\sigma)].
```

It uses the usual support convention and is distinct from Rényi divergence of order two. Measurement data processing gives

```math
\begin{aligned}
D_{\mathrm{bits}}(\rho_T^0\|\rho_T^e)&\geq j(\delta),\\
j(\delta)&=(1-2\delta)\log_2\frac{1-\delta}{\delta}.
\end{aligned}
```

Summing over the $`3n`$ labels yields

```math
\boxed{C\geq4n\,j(\delta).}
```

In particular, at error $`1/3`$,

```math
\boxed{C\geq\frac{4n}{3}.}
```

For product clean/mixed initialization, this is $`c\geq4n/3`$. Thus $`c=O(\log n)`$ is impossible at any fixed error below one half, even with arbitrarily many calls and unrestricted protected width. The proposed polynomial-query protocol using logarithmic side memory and logarithmic initial clean qubits cannot exist in this model.

The same necessity also transfers to later-requested coefficient learning with merely per-target confidence. If an acquisition procedure estimates any requested weight-one coefficient to additive error strictly below $`1/4`$ with success at least $`2/3`$ under the null and each promised alternative, threshold its estimate at $`1/4`$ when the request is $`e`$. This separates the null from that alternative. The entropy theorem bounds each individual reverse relative entropy before summing, so different final effects for different requests are allowed; simultaneous accuracy is not needed for this conclusion. If every estimate is simultaneously accurate, thresholding their maximum additionally gives one common detector.

Pinsker's inequality and averaging also imply

```math
D_{\mathrm{tr}}(\bar\rho_T,\rho_T^0)
\leq\min\left\{1,\frac{\sqrt{C\ln2}}{\sqrt{8n}}\right\}.
```

The binary relative-entropy calculation above gives the sharper stated constant for a specified worst-case error. No optimality of that constant or matching linear-purity protocol is claimed.

## Why the entropy charge accumulates only once

Write $`Q_0=\mathcal D\otimes\mathrm{id}_A`$ and $`Q_e=\mathcal E_{e,1}\otimes\mathrm{id}_A-Q_0`$. The map $`R_e=Q_0+Q_e`$ is the conditional expectation retaining the active Pauli axis and the full side algebra. Three ingredients establish the theorem.

First, for arbitrary null and alternative prequery states $`\sigma,\rho`$, joint convexity and data processing give the amortized inequality

```math
\begin{aligned}
&D_{\mathrm{bits}}(Q_0\sigma\|(Q_0+\tfrac12Q_e)\rho)\\
&\quad\leq D_{\mathrm{bits}}(\sigma\|\rho)\\
&\qquad+\frac12D_{\mathrm{bits}}(R_e\sigma\|Q_0\sigma).
\end{aligned}
```

The special attenuation $`1/2`$ permits a positive binary flip: a known Pauli conjugation reverses the retained axis of $`R_e\sigma`$, and averaging the flipped and unflipped states gives $`Q_0\sigma`$. This works with noncommuting quantum side-memory blocks. The conjugation is a proof device and gives the learner no access to the hidden label.

Second, the three dephasings of a single qubit satisfy a relative-entropy source budget. For $`e=(i,\alpha)`$ and $`g_i=D_{\mathrm{bits}}(\sigma_{S_iA}\|I_i/2\otimes\sigma_A)`$, two distinct axes obey $`d_{i,\alpha}+d_{i,\beta}\leq g_i`$, where $`d_{i,\alpha}=D_{\mathrm{bits}}(R_{i,\alpha}\sigma\|Q_0\sigma)`$. Summing these pair inequalities and using conditional subadditivity gives

```math
\begin{aligned}
&\sum_{e\in\mathcal A_1}D_{\mathrm{bits}}(R_e\sigma\|Q_0\sigma)\\
&\qquad\leq\frac32\,[H(Q_0\sigma)-H(\sigma)].
\end{aligned}
```

Finally, along the common null trajectory, each query's entropy increase is paid from the same initial entropy deficit. Unital controls cannot decrease entropy, so the query increases telescope to at most $`C`$ bits. Combining the factor $`1/2`$ from amortization with the factor $`3/2`$ from the source budget gives $`3/4`$. The [authoritative proof](https://github.com/GoGoKo699/Quantum-Learning-Without-Resets/blob/main/science/entropy_bound.md) gives the identities, time ordering and support treatment in full.

## What the side-width conclusion requires

If the entire fixed processor has $`n+k_{\mathrm{phys}}`$ qubits, including all protected records, then $`C\leq n+k_{\mathrm{phys}}`$. Consequently error $`1/3`$ requires

```math
\boxed{k_{\mathrm{phys}}\geq n/3.}
```

This is a necessary width condition, not an attaining frontier. It applies to the physical dimension of every protected register. The original coherent-width parameter $`k`$ exempts a dephased classical history $`H`$; if additional initially supplied classical records are exempted from $`k`$, substituting that $`k`$ for $`k_{\mathrm{phys}}`$ is unjustified. The linear initial-entropy-deficit obstruction still holds when all those records and their initial purity are charged, regardless of their dimension or coherence.

## Relation to the original frontier and its detector

At weight one, the original reset-permitting law $`w(n-k)/n=O(\log n)`$ allows polynomial query cost even with no coherent reference. Its partial-Bell and local-axis protocols obtain new polarized probes and retain their outcomes. They do not meet the fixed-initial-purity restrictions above. Their original frontier remains correct in its stated access model.

The $`\tau`$-dependent detector in [correlation_detection.md](correlation_detection.md) retains the hidden eigenvalue exactly at one: adding an identity branch does not attenuate it. Its rank test relies on an exact parity constraint, and its fresh records also carry a resource cost in the present model. Neither that detector nor the near-conservation one-clean-qubit scans in the sister repository are protocols for a hidden eigenvalue fixed at $`1/2`$.

The established joint result is the stronger obstruction at weight one and attenuation one half. A matching protocol at linear resources, sharp constants, and the full frontier at higher weights or other attenuation strengths remain separate questions.
