# Related work and attribution

The result developed in this repository evaluates the dependence on the allowed
Pauli weight $`w`$ and the number $`k`$ of qubits outside each queried
$`n`$-qubit register. At constant accuracy, the joint polynomial-query frontier
is $`w(n-k)/n=O(\log n)`$, including arbitrary coherent sequential processing
under the stated width budget. The one-bit decision theorem has the same
frontier and an efficient rank algorithm; with identity-mixture strength
$`\tau`$, its condition becomes
$`w(n-k)/n+\log(1/\tau)=O(\log n)`$.

These conclusions use established Pauli-spike families, Bell probes,
hypothesis-testing arguments, and hypercontractivity. The precise contribution
must be assessed against those precedents and their access models. In
particular, a lower bound over every Pauli label cannot simply be restricted
to a low-weight family, and a state-copy theorem does not automatically
preserve the width budget of a controlled channel experiment.

## Closest comparisons

| Source | Established result relevant here | Relation to this repository |
|---|---|---|
| [KimOh2026](#kimoh2026) | Weight-restricted Pauli-channel learning with fresh, ancilla-assisted experiments; a conditional sharper boundary in S85–S87. | The weighted rank bound here is weaker than S85 but proves the polynomial frontier. The coherent theorem permits retained memory and concatenation. |
| [ChenGong2025](#chengong2025) | Positive-spike detection and a full-Pauli coherent query lower bound; logarithmic-memory protocols with few measurements. | The spike task and coherent-use distinction are prior work. The present bounds evaluate the dependence on allowed weight and count every call. |
| [KangJeonOh2026](#kangjeonoh2026) | Coherent Pauli-learning bounds under one-sided input or measurement restrictions. | Their restrictions and the total query-cut width constraint are different. The appearance of a half exponent alone is not the contribution here. |
| [ChenGongYe2024](#chengongye2024) | A minimax characterization for Pauli state shadows with arbitrary subsets and allowed measurements. | The abstract characterization is relevant background; the support-dependent channel response still requires evaluation under the channel access contract. |
| [King2014](#king2014) | Hypercontractivity for products of unital qubit semigroups, including depolarizing channels. | The analytic engine is cited as an existing theorem. The rank-constrained weighted response and its channel application are proved here. |

## Primary sources

<a id="kimoh2026"></a>
### KimOh2026

Minsoo Kim and Changhun Oh, **On the fundamental resource for exponential
advantage in quantum channel learning**, *Nature Communications* **17**, 1822
(2026). [DOI](https://doi.org/10.1038/s41467-026-68532-y);
[arXiv](https://arxiv.org/abs/2507.11089);
[version inspected: v2, including supplement](https://arxiv.org/html/2507.11089v2).

Definition 1 uses a fresh input, one channel call, and a final POVM, with
classical adaptivity. Theorem 2 supplies weight-sensitive lower bounds; for
$`w\leq n/2`$ its dependence is
$`\Omega(\epsilon^{-2}n^{-1/2}2^{-k}3^w)`$ at fixed confidence.
Supplement S3.5 proposes the unproved rank-constrained identity S85,

```math
\max_{\mathrm{rank}C\leq2^k}
\mathbb E_{e\sim\nu_x}
\frac{\mathrm{Tr}(P_eCP_eC^\dagger)^2}
     {\mathrm{Tr}(CC^\dagger)^2}
=\left(\frac{1+x}{1+3x}\right)^{n-k}.
```

The bound proved in [weighted_bounds.md](../science/weighted_bounds.md) is
$`2^{-2x(n-k)/(1+x)}`$. It supplies the needed exponential dependence in
$`w(n-k)/n`$ without establishing S85 or the exact exponential rate.

<a id="chengong2025"></a>
### ChenGong2025

Sitan Chen and Weiyuan Gong, **Efficient Pauli Channel Estimation with
Logarithmic Quantum Memory**, *PRX Quantum* **6**, 020323 (2025).
[DOI](https://doi.org/10.1103/PRXQuantum.6.020323);
[arXiv](https://arxiv.org/abs/2309.14326);
[version inspected: v5](https://arxiv.org/pdf/2309.14326v5).

Problem 3 already defines positive Pauli-spike detection against complete
depolarization. Theorem 8 proves an $`\Omega(2^{(n-k)/3})`$ channel-call
bound for the full Pauli family, allowing adaptive concatenation and
$`k`$ ancillas. Theorem 4 gives a two-ancilla detector with one measurement
and exponentially many calls. Consequently measurement count cannot replace
call count in the present resource statement. The support-dependent prior and
bound in [coherent_memory.md](../science/coherent_memory.md), and the
weight-sensitive rank construction in
[correlation_detection.md](../science/correlation_detection.md), specify the
additional conclusions studied here.

<a id="kangjeonoh2026"></a>
### KangJeonOh2026

Hyeongu Kang, Sangwoo Jeon, and Changhun Oh, **Bound Entanglement Is
Insufficient for an Exponential Quantum Learning Advantage**, arXiv:2607.19017
(2026). [Version inspected: v1](https://arxiv.org/html/2607.19017v1).

Theorem 2 and Corollary 1 give full-family coherent bounds including
$`\Omega(\epsilon^{-1}2^{(n-\eta)/2})`$ under a conditional-min-entropy
restriction. In the input-restricted model, each fresh input is uncorrelated
with retained quantum systems conditional on classical history. In the
measurement-restricted model, inputs may be correlated across uses, but the
current POVM acts on the current output and associated ancilla and obeys the
specified restriction. These conditions appear explicitly in Supplement
S2.1.1 and S2.2. They differ from the general feedback and total query-cut
width allowed here. This work is also precedent for combining a coherent
hybrid with a bound on average distinguishability.

<a id="chengongye2024"></a>
### ChenGongYe2024

Sitan Chen, Weiyuan Gong, and Qi Ye, **Optimal tradeoffs for estimating Pauli
observables**, arXiv:2404.19105 (2024).
[arXiv](https://arxiv.org/abs/2404.19105);
[version inspected: v2](https://arxiv.org/pdf/2404.19105v2).

Theorem 1 characterizes state-shadow sample complexity through a minimax
chi-squared optimization over an arbitrary observable subset and an allowed
POVM family. Theorem 4 evaluates a Clifford-measurement case using fractional
coloring. Theorem 6 evaluates the bounded-memory tradeoff for the full Pauli
set; Section 2.2.2 distinguishes the abstract subset characterization from
extracting a usable bound. The paper also uses partial Bell measurements in
its state-learning upper bound. None of these mechanisms is claimed as new
here. A direct reduction through unrestricted Choi-state measurements would
grant reference access that must instead be counted; a resource-preserving
translation would still require the relevant weighted response estimate.

<a id="king2014"></a>
### King2014

Christopher King, **Hypercontractivity for Semigroups of Unital Qubit
Channels**, *Communications in Mathematical Physics* **328**, 285–301 (2014).
[Publisher and DOI](https://link.springer.com/article/10.1007/s00220-014-1982-4);
[arXiv](https://arxiv.org/abs/1210.8412);
[version inspected: v1](https://arxiv.org/pdf/1210.8412v1).

Corollary 2 gives the normalized Schatten-norm hypercontractive inequality
for products of qubit depolarizing channels. The norm in equation (6) is
defined over all matrices, so the application to a complex matrix in
[weighted_bounds.md](../science/weighted_bounds.md) does not require a
Hermitian dilation. The theorem is an external analytic input; the
Pauli-weight prior, rank estimate, channel-response identities, and resource
consequences are established in the repository's proofs.

<a id="chenzhouseifjiang2022"></a>
### ChenZhouSeifJiang2022

Senrui Chen, Sisi Zhou, Alireza Seif, and Liang Jiang, **Quantum advantages
for Pauli channel estimation**, *Physical Review A* **105**, 032435 (2022).
[DOI](https://doi.org/10.1103/PhysRevA.105.032435);
[arXiv and journal metadata](https://arxiv.org/abs/2108.08488);
[version inspected: v2](https://arxiv.org/pdf/2108.08488v2).

This paper establishes the full-reference Bell-sampling advantage, Pauli-spike
lower-bound families, and bounded-ancilla separations. Theorem 3 and its proof
use the signed single-spike construction and adaptive nonconcatenating
experiments. The basic fact that Bell measurements reveal Pauli-error
information is therefore prior work. Full-reference Choi access is not free
in the present model: preparing and retaining all $`n`$ references consumes
the corresponding outside-register width.

<a id="chenohzhouhuangjiang2024"></a>
### ChenOhZhouHuangJiang2024

Senrui Chen, Changhun Oh, Sisi Zhou, Hsin-Yuan Huang, and Liang Jiang,
**Tight bounds on Pauli channel learning without entanglement**,
*Physical Review Letters* **132**, 180805 (2024).
[DOI](https://doi.org/10.1103/PhysRevLett.132.180805);
[arXiv and journal metadata](https://arxiv.org/abs/2309.13461);
[version inspected: v3](https://arxiv.org/html/2309.13461v3).

This work proves the tight full-family entanglement-free scaling
$`\Theta(2^n\epsilon^{-2})`$ for pointwise coefficient success and permits
mid-circuit measurements and classical feedback. Its simultaneous upper
bound has an additional factor of $`n`$; the pointwise lower bound still
applies. This distinction is explicit in Theorem 2 and the paragraph that
follows it. The pointwise result establishes a stronger full-family endpoint
than the general weight-sensitive lower bound alone. That endpoint does not
locate the intermediate frontier with both $`w`$ and $`k`$ varying.

<a id="fawziflammariongarivieroufkir2023"></a>
### FawziFlammarionGarivierOufkir2023

Omar Fawzi, Nicolas Flammarion, Aurélien Garivier, and Aadil Oufkir,
**Quantum Channel Certification with Incoherent Strategies**,
*Proceedings of the Thirty Sixth Conference on Learning Theory*,
PMLR **195**, 1822–1884 (2023).
[arXiv and proceedings metadata](https://arxiv.org/abs/2303.01188);
[version inspected: v2](https://arxiv.org/pdf/2303.01188v2).

This paper studies certification against fixed channel specifications,
including complete depolarization, with alternatives separated in channel
norm. It supplies relevant channel-testing methods and emphasizes the role
of allowed ancillas. A worst-case lower bound over general channel
alternatives does not imply the same lower bound after restricting to the
succinct, weight-bounded positive-spike family. The direct decision proof in
[correlation_detection.md](../science/correlation_detection.md) makes that
restriction explicitly.

<a id="subramaniankwonjiang2026"></a>
### SubramanianKwonJiang2026

Mahadevan Subramanian, Hyukgun Kwon, and Liang Jiang, **Quantum channel
learning with limited parallel access**, arXiv:2608.05307 (2026).
[arXiv](https://arxiv.org/abs/2608.05307);
[version inspected: v2](https://arxiv.org/html/2608.05307v2).

The resource hierarchy concerns the number of parallel channel copies and
access to a complex-conjugate channel, with adaptively chosen
ancilla-assisted experiments. Those are distinct access resources from
ordinary sequential channel use at bounded outside-register width. The
present model grants neither a conjugate-channel oracle nor uncounted
parallel input registers.

<a id="cotlergongkannan2025"></a>
### CotlerGongKannan2025

Jordan Cotler, Weiyuan Gong, and Ishaan Kannan, **Noisy Quantum Learning
Theory**, arXiv:2512.10929 (2025).
[arXiv](https://arxiv.org/abs/2512.10929);
[version inspected: v2](https://arxiv.org/html/2512.10929v2).

This work studies noisy quantum access and memory limitations. In particular,
Theorem F.13 treats Pauli state shadows from locally depolarized copies with
persistent quantum memory and unbounded quantum depth. It is relevant
precedent for joint memory–noise tradeoffs. Here the learner controls channel
inputs, while the weak-noise parameter describes a known identity mixture
of the unknown channel. That is a different noise contract; no claim of
general noisy-memory resilience follows from it.

<a id="kwonliejiang2026"></a>
### KwonLieJiang2026

Hyukgun Kwon, Seok Hyung Lie, and Liang Jiang, **Universal Sample Complexity
Bounds in Quantum Learning Theory via Fisher Information Matrix**,
*PRX Quantum* **7**, 033063 (2026).
[DOI](https://doi.org/10.1103/8k5v-ddtw);
[arXiv](https://arxiv.org/abs/2602.21510);
[version inspected: v4](https://arxiv.org/html/2602.21510v4).

This framework relates small-error sample bounds for regular parametric models
and maximum-likelihood estimation to inverse Fisher information. Its
Pauli-channel applications in Section III.3 compare full-reference learning
with separable strategies, including repeated channel uses and an unbounded
ancilla in Section III.3.4. That repeated-use result requires system–ancilla
separability throughout. The paper supplies a complementary metrological
account of the entanglement advantage; it does not evaluate the joint
low-weight and total coherent-width frontier studied here. Its fixed-dimension
small-error asymptotics alone do not give the growing-system,
constant-accuracy statement of this repository.

## Educational anchor

<a id="watrous2018"></a>
### Watrous2018

John Watrous, **The Theory of Quantum Information**, Cambridge University
Press (2018). [Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).
Section and equation pointers use the linked pre-publication chapter files;
their [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf)
is dated January 2018.

This is the project's single educational anchor for finite quantum systems,
channels, measurements, operator norms, and distinguishability. The
[Watrous bridge](../learning/WATROUS_BRIDGE.md) gives the relevant sections,
convention translations, and steps to the project. King's hypercontractivity
theorem remains a primary research input; the weighted applications and
learning and detection arguments are supplied in the scientific account.

## Attribution and comparison rules

The proofs cite hypercontractivity and the established statistical and Pauli
channel mechanisms at their points of use. The evaluated joint frontier
does not resolve Kim–Oh S85, determine the optimal exponential constant,
or supply a universal optimal accuracy dependence for coherent processors.
For a polynomial-size known observable family, separate direct measurements
can already have polynomial cost even at large weight; the necessity result
here concerns the entire weight ball or the corresponding hidden-label
promise. The reference comparison is about the stated models and theorems,
and makes no categorical claim of priority over every possible formulation.

Bibliographic keys and machine-readable entries are in
[references.bib](references.bib). Primary metadata and the specified theorem
versions were checked on 18 October 2026.
The closest comparisons with Kim–Oh, Chen–Gong, and Kang–Jeon–Oh were rechecked
on 24 October 2026; the Kwon–Lie–Jiang comparison was added on that date.
