# A 30-milestone map of the project

This map gives thirty project-defined understanding targets for any reader, including LLMs. The targets follow the dependencies of the science and together explain the complete result, its physical meaning, and its boundaries. They do not replace the specialist proofs or attempt to cover every technical detail.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) identifies the relevant foundations, translates notation, and explains the additional project ingredients. The [worked example](WORKED_EXAMPLE.md) connects preparations, measurements, classical records, and resource counts in a small system. Primary research papers remain sources for attribution and imported theorems; they are not additional educational anchors.

## Why the allocation is 14 background and 16 narrative milestones

The **background/preliminaries phase, M01–M14**, starts with one qubit and one measurement. It combines Pauli algebra, reference registers, operator norms, statistical records, and binary linear algebra into the complete access and output model. Fourteen targets are useful because the project connects quantum channel discrimination with classical estimation and syndrome processing.

The **narrative/innovation phase, M15–M30**, starts with the response of one preparation and one measurement. Weighted rank estimates then control a whole adaptive experiment, and a constructive protocol supplies the opposite direction of the learning threshold. The last five milestones interpret and extend that mechanism through the physical one-bit promise, an efficient detector, and weak channels before giving the full synthesis.

Dependencies always refer to earlier milestones. Each phase progresses from local objects or arguments to an integrated understanding. Throughout the map, the authoritative definitions are in [the model](../science/model.md): $`n`$ channel-input qubits, at most $`k`$ coherent qubits outside that register at every invocation, maximum target weight $`w`$, deficit $`D=n-k`$, and $`R=wD/n`$.

## Phase I: Background and preliminaries

<a id="m01"></a>
### M01. Local Pauli axes

**Central question.** How can a one-qubit error preserve or flip a measurement outcome along a chosen axis?

**Understanding target.** Distinguish the operators $`I,X,Y,Z`$, the two eigenvalues of a nonidentity Pauli, and the eigenstates prepared or measured along an axis. Explain why a Pauli error preserves the sign when it commutes with that axis and flips the sign when it anticommutes.

**Dependencies and story role.** No earlier milestone. This is the local physical primitive from which both the coefficient estimator and the syndrome detector are built.

**Conceptual connection.** A commutation relation becomes an experimentally recorded bit. The later argument concerns which such bits a probe makes available.

**Source pointers.** [Model: Pauli channels and the target family](../science/model.md#pauli-channels-and-the-target-family); [Partial-Bell protocol: what one experiment records](../science/partial_bell.md#what-one-experiment-records); [worked example](WORKED_EXAMPLE.md).

<a id="m02"></a>
### M02. Binary labels and commutation characters

**Central question.** How does Pauli algebra become binary linear algebra?

**Understanding target.** Represent a Pauli label by $`(x,z)\in\mathbb F_2^{2n}`$, distinguish the label from its Hermitian phase convention, and interpret $`[e,v]`$ as a binary symplectic pairing. Explain why $`(-1)^{[e,v]}`$ is the commutation sign and why, for nonzero $`e`$, the equation $`[e,v]=0`$ defines one linear parity constraint.

**Dependencies and story role.** Uses [M01](#m01). It turns the one-qubit sign rule into a representation that can describe tensor products, probability distributions, and efficient classical processing.

**Conceptual connection.** The same character appears as a channel eigenvalue contribution, a likelihood response, and a syndrome parity.

**Source pointers.** [Model: Pauli channels and the target family](../science/model.md#pauli-channels-and-the-target-family); [Weighted bounds: Pauli notation and the product prior](../science/weighted_bounds.md#pauli-notation-and-the-product-prior).

<a id="m03"></a>
### M03. Tensor weight and the complete target family

**Central question.** What changes when the desired correlation may have any support and any local axes through weight $`w`$?

**Understanding target.** Read Pauli weight as the number of nonidentity tensor factors. Distinguish the complete family $`\mathcal A_w`$ from one known observable or a smaller specified list. Interpret $`M_w=\sum_{u=0}^w\binom nu3^u`$ and explain why its identity term is only a counting convenience.

**Dependencies and story role.** Uses [M01](#m01) and [M02](#m02). It enlarges local observables into the family over which the learning guarantee and hard prior must both be valid.

**Conceptual connection.** A restriction on support size leaves many unknown support-and-axis choices. The lower bound depends on that whole family, not merely its largest weight.

**Source pointers.** [Model: Pauli channels and the target family](../science/model.md#pauli-channels-and-the-target-family); [Model: learning a reusable record](../science/model.md#learning-a-reusable-record); [Interpretation: scope of the complete result](../science/interpretation.md#scope-of-the-complete-result).

<a id="m04"></a>
### M04. Pauli channels and Fourier coefficients

**Central question.** Why is a Pauli-channel coefficient the mean of a classical error character?

**Understanding target.** Relate the random-conjugation form $`\Lambda(\rho)=\sum_vp_vP_v\rho P_v`$ to the diagonal action $`\Lambda(P_e)=\lambda_eP_e`$ and to $`\lambda_e=\sum_vp_v(-1)^{[e,v]}`$. Distinguish independence between channel uses from independence between sites within a single error draw.

**Dependencies and story role.** Uses [M02](#m02) and [M03](#m03). It joins the target operators to a physical memoryless channel and identifies the numerical quantities that a learner must estimate.

**Conceptual connection.** The Pauli probabilities ensure a physical channel, while their Fourier coefficients describe which observables survive its action. Globally correlated errors remain allowed.

**Source pointers.** [Model: Pauli channels and the target family](../science/model.md#pauli-channels-and-the-target-family); [Partial-Bell protocol: what one experiment records](../science/partial_bell.md#what-one-experiment-records); [Watrous bridge](WATROUS_BRIDGE.md).

<a id="m05"></a>
### M05. Probing a specified coefficient

**Central question.** Why is estimating one Pauli given before acquisition easier than preparing a record for an index supplied afterward?

**Understanding target.** Explain how local eigenstate preparation and the corresponding output parity give a sign with mean $`\lambda_e`$ when the target $`e`$ is known in advance. Identify the target-dependent choice of axes. Explain why repeating that procedure separately does not by itself give a cheap record for the complete late-index family.

**Dependencies and story role.** Uses [M01](#m01), [M03](#m03), and [M04](#m04). It gives the simplest operational task before introducing the constraint responsible for the threshold.

**Conceptual connection.** Acquisition timing is part of the learning problem. A later classical decoding request cannot retroactively choose an earlier quantum measurement.

**Source pointers.** [Model: learning a reusable record](../science/model.md#learning-a-reusable-record); [Partial-Bell protocol: compatibility with a requested target](../science/partial_bell.md#compatibility-with-a-requested-target); [worked example](WORKED_EXAMPLE.md).

<a id="m06"></a>
### M06. Reference width and Schmidt rank

**Central question.** How does the size of an accessible reference constrain a pure probe?

**Understanding target.** Relate a pure state on $`S\otimes A`$ to its Schmidt decomposition and the rank of its system marginal. Derive $`\operatorname{rank}\rho_S\leq\dim A\leq2^k`$. Explain why a mixed joint state can have a system marginal of larger rank and why an algebraic decomposition inside the actual registers does not supply extra coherent memory.

**Dependencies and story role.** Uses [M04](#m04). It converts a physical width budget into the matrix-rank parameter that will enter the lower bound.

**Conceptual connection.** Purification is a mathematical representation whose reference dimension matters operationally. The proof must respect that dimension rather than adding an uncharged purifying register.

**Source pointers.** [Watrous §1.1.3, Schmidt decomposition, Eqs. (1.162)–(1.164)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Watrous §2.1.3, Theorem 2.10](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Coherent memory: pure inputs](../science/coherent_memory.md#pure-inputs); [Coherent memory: mixed inputs and classical histories](../science/coherent_memory.md#mixed-inputs-and-classical-histories).

<a id="m07"></a>
### M07. Bell error readout

**Central question.** What additional error information does one reference qubit make accessible?

**Understanding target.** Explain why applying each of the four local Pauli errors to one half of a Bell pair gives distinguishable Bell labels. Compare the two error bits read at a paired site with the single commutation bit read at an unpaired site. Count one reference qubit per pair.

**Dependencies and story role.** Uses [M01](#m01), [M02](#m02), [M04](#m04), and [M06](#m06). It supplies the local operational benefit of the resource being constrained.

**Conceptual connection.** Bell sampling reads error information through an ordinary channel call and a joint measurement. The error label is not supplied as an extra oracle output.

**Source pointers.** [Partial-Bell protocol: what one experiment records](../science/partial_bell.md#what-one-experiment-records); [Partial-Bell protocol: physical and classical resources](../science/partial_bell.md#physical-and-classical-resources); [Watrous bridge](WATROUS_BRIDGE.md); [worked example](WORKED_EXAMPLE.md).

<a id="m08"></a>
### M08. Schatten norms and a rank deficit

**Central question.** How can a low matrix rank suppress a normalized operator norm?

**Understanding target.** Distinguish trace, Hilbert–Schmidt, and general Schatten norms from their dimension-normalized versions. Explain the singular-value comparison

```math
\|A\|_{p,\mathrm{av}}
\leq(r/d)^{1/p-1/2}\|A\|_{2,\mathrm{av}},
\qquad 1\leq p\leq2,
```

for rank $`r`$. Recognize where the factor $`r/d`$ enters and how Schatten Hölder bounds products of matrices.

**Dependencies and story role.** Uses [M06](#m06). It provides the quantitative bridge from a reference dimension to a response bound.

**Conceptual connection.** The normalization by $`d=2^n`$ is essential: combining $`r\leq2^k`$ with the norm comparison produces a dependence on the missing reference width $`D=n-k`$.

**Source pointers.** [Watrous §1.1.3, especially Eq. (1.169)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Weighted bounds: hypercontractivity and the rank comparison](../science/weighted_bounds.md#hypercontractivity-and-the-rank-comparison).

<a id="m09"></a>
### M09. Fidelity, trace distance, and a decision

**Central question.** Which distances connect an operator calculation to the success of an experiment?

**Understanding target.** Use trace distance $`\tfrac12\|\rho-\sigma\|_1`$ as a bound on the probability difference of any measurement event. Relate two decision errors at most $`\delta`$ to distance at least $`1-2\delta`$, and explain contraction under a common channel. Interpret the unsquared fidelity $`F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$; the project's quantity $`f_e`$ uses this same convention.

**Dependencies and story role.** Uses [M04](#m04), [M06](#m06), and [M08](#m08). It links matrix norms to the operational distinction that a lower bound must prevent.

**Conceptual connection.** Fidelity controls the response of a probe, while trace distance limits how much a later measurement or common physical evolution can reveal.

**Source pointers.** [Watrous §3.1.1, Theorem 3.4; Definition 3.11 and Eq. (3.64)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Weighted bounds: root-fidelity bound](../science/weighted_bounds.md#root-fidelity-bound); [Coherent memory: learning-to-testing reduction](../science/coherent_memory.md#learning-to-testing-reduction-and-finite-constants).

<a id="m10"></a>
### M10. Classical histories and coherent experiments

**Central question.** What information can persist between calls without violating the resource contract?

**Understanding target.** Describe known quantum instruments with classical outcomes and conditional quantum states. Distinguish a fully measured fresh experiment from a protocol that retains coherence in both $`S`$ and $`A`$. Count every invocation and every accessible coherent register outside $`S`$ at that invocation, including during adaptive or concatenated strategies.

**Dependencies and story role.** Uses [M04](#m04), [M06](#m06), and [M09](#m09). It assembles local states and measurements into the sequential processor covered by the theorem.

**Conceptual connection.** Classical adaptivity does not consume coherent width, but a coherent controller does. Worst-case call counts also charge long blocks and permit early stopping without replacing the budget by an expected count.

**Source pointers.** [Watrous §2.2.3, Eq. (2.170), and §2.3.2, Eqs. (2.258)–(2.262)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); [Model: coherent access](../science/model.md#coherent-access); [Model: fresh experiments](../science/model.md#fresh-experiments); [Coherent memory: statement and resource contract](../science/coherent_memory.md#statement-and-resource-contract).

<a id="m11"></a>
### M11. Estimator variance and reusable records

**Central question.** How can one random record support many estimates with a controlled number of calls?

**Understanding target.** Distinguish an estimator's expectation, variance, and range. Explain how a second-moment bound enters Bernstein concentration, and how a union bound produces a simultaneous guarantee even when target estimates use the same data. Separate acquiring a record, decoding one coefficient, and printing the entire coefficient family.

**Dependencies and story role.** Uses [M03](#m03), [M04](#m04), [M05](#m05), and [M07](#m07). It turns individual signs into the statistical output needed by the learning task.

**Conceptual connection.** Rare usable records increase variance. Tracking that variance avoids charging a needless second power of the inverse usability probability.

**Source pointers.** [Partial-Bell protocol: unbiased estimation and its variance](../science/partial_bell.md#unbiased-estimation-and-its-variance); [Partial-Bell protocol: simultaneous guarantee](../science/partial_bell.md#simultaneous-guarantee); [Model: computation, storage, and precision](../science/model.md#computation-storage-and-precision).

<a id="m12"></a>
### M12. Syndromes and linear rank

**Central question.** How can an unknown parity be detected without enumerating possible Pauli labels?

**Understanding target.** Interpret a measurement record as $`y=Av`$ over $`\mathbb F_2`$. Relate a character visible through the record to the row space of $`A`$. Explain why an exact homogeneous parity places every observed row in a proper linear subspace and why ordinary Gaussian elimination detects that constraint.

**Dependencies and story role.** Uses [M02](#m02), [M04](#m04), and [M07](#m07). It supplies the classical computational mechanism that will make the one-bit upper bound efficient.

**Conceptual connection.** Bell outcomes and local-axis signs are different local measurements but together form one linear syndrome. The existence of a constraint can be inferred without recovering its hidden Pauli label.

**Source pointers.** [Correlation detection: partial-Bell settings expose a linear syndrome](../science/correlation_detection.md#4-partial-bell-settings-expose-a-linear-syndrome); [Correlation detection: the linear-rank algorithm](../science/correlation_detection.md#5-the-linear-rank-algorithm); [worked example](WORKED_EXAMPLE.md).

<a id="m13"></a>
### M13. Product noise and hypercontractivity

**Central question.** Why does a product distribution on Pauli labels lead to a norm inequality for a noise operator?

**Understanding target.** Relate the prior $`\nu_x(e)`$ to its character average $`t^{|b|}`$ and to the tensor depolarizing map $`\mathcal T_t`$. Interpret the semigroup identity and King's hypercontractive comparison between normalized Schatten norms. Identify its applicability to complex matrices, its parameter range, and the separately justified endpoint.

**Dependencies and story role.** Uses [M02](#m02), [M03](#m03), [M04](#m04), and [M08](#m08). It provides the last analytic ingredient before the full model is assembled.

**Conceptual connection.** Averaging unknown Pauli directions is equivalent to applying a known mathematical noise operator. This averaging operator is a proof device, not a noise assumption imposed on the experimental reference.

**Source pointers.** [Weighted bounds: Pauli notation and the product prior](../science/weighted_bounds.md#pauli-notation-and-the-product-prior); [Weighted bounds: hypercontractivity and the rank comparison](../science/weighted_bounds.md#hypercontractivity-and-the-rank-comparison); [King2014, Corollary 2](../references/RELATED_WORK.md#king2014). King is the imported research theorem; Watrous supplies the operator-norm foundations.

<a id="m14"></a>
### M14. The integrated access and output model

**Central question.** What must be held fixed for a memory threshold to be a meaningful statement?

**Understanding target.** Assemble the channel family, complete target set, index timing, accuracy and confidence, ordinary channel access, worst-case call budget, and total outside-register width. Distinguish the pointwise late-index guarantee, the stronger simultaneous guarantee, and the one-bit promise whose hidden label is never supplied. Identify the ideal controls used by the constructive protocols.

**Dependencies and story role.** Integrates M01–M13, particularly [M03](#m03), [M06](#m06), [M10](#m10), [M11](#m11), and [M12](#m12). This is the background phase's global synthesis.

**Conceptual connection.** The quantity $`R=w(n-k)/n`$ joins a target's possible support with the available reference width. Its significance can only be assessed with the output, access, and precision contract kept explicit.

**Source pointers.** [Model and tasks](../science/model.md); [Interpretation: missing reference width and Pauli support](../science/interpretation.md#missing-reference-width-and-pauli-support); [Watrous bridge](WATROUS_BRIDGE.md).

## Phase II: Narrative and innovation

<a id="m15"></a>
### M15. One physical experiment gives a complex response matrix

**Central question.** Which mathematical object captures the signal of one arbitrary fresh preparation and measurement?

**Understanding target.** Express a pure probe and a rank-one effect by system-by-reference matrices $`\Psi`$ and $`M`$. Explain why $`C=M\Psi^\dagger`$ has rank at most $`2^k`$, why the depolarizing probability is $`\|C\|_F^2/d`$, and why a signed nonidentity Pauli spike gives likelihood $`1+s aG_e(C)`$. Understand the convex extension to mixed preparations and effects, including zero-probability outcomes.

**Dependencies and story role.** Uses [M04](#m04), [M06](#m06), [M08](#m08), and [M14](#m14). This is the narrative's local starting point: one physical probability identity.

**Conceptual connection.** Physical states and effects are positive operators, yet their coefficient-matrix contraction $`C`$ can be non-Hermitian. The needed rank inequality must therefore cover complex matrices.

**Source pointers.** [Watrous §1.1.2, vectorization and Eqs. (1.133)–(1.134)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf); [Fresh experiments: valid channel hypotheses](../science/fresh_experiments.md#valid-channel-hypotheses-and-the-target-prior); [Fresh experiments: the one-experiment likelihood](../science/fresh_experiments.md#the-one-experiment-likelihood); [Fresh experiments: mixed preparations and arbitrary POVMs](../science/fresh_experiments.md#mixed-preparations-and-arbitrary-povms).

<a id="m16"></a>
### M16. The weighted complex-response bound

**Central question.** Why must a limited-rank experiment have a small average squared response?

**Understanding target.** Interpret the normalized squared Pauli coefficients of $`C`$ as a probability distribution $`q`$. Follow the conversion of $`G_e(C)`$ into a character average and its second moment into rows controlled by $`\mathcal T_{\sqrt t}(P_cC)`$. Explain how hypercontractivity and rank give Lemma W1:

```math
\mathbb E_{\nu_x}G_e(C)^2
\leq(r/d)^\gamma\leq2^{-D\gamma},
\qquad \gamma=\frac{2x}{1+x}.
```

**Dependencies and story role.** Uses [M02](#m02), [M08](#m08), [M13](#m13), and [M15](#m15). It establishes the local analytic limitation used by the fresh-experiment converse.

**Conceptual connection.** The physical width constraint enters through matrix rank, while the target-weight preference enters through the product prior. This proved inequality is sufficient for the threshold without resolving the stronger extremal formula proposed in Kim–Oh S85.

**Source pointers.** [Weighted bounds: complex response bound and proof](../science/weighted_bounds.md#complex-response-bound); [Weighted bounds: relation to a stronger weighted inequality](../science/weighted_bounds.md#relation-to-a-stronger-weighted-inequality); [King2014](../references/RELATED_WORK.md#king2014).

<a id="m17"></a>
### M17. The weighted root-fidelity bound

**Central question.** What replaces a classical likelihood response when the output remains quantum?

**Understanding target.** Explain the quantity $`f_e(\rho)=\|\sqrt\rho P_e\sqrt\rho\|_1`$. Follow Schatten Hölder with exponents $`(4,2,4)`$, Pauli averaging, and the semigroup identity to the bound

```math
\mathbb E_{\nu_x}f_e(\rho)^2
\leq(\operatorname{rank}\rho/d)^\gamma.
```

**Dependencies and story role.** Uses [M06](#m06), [M08](#m08), [M09](#m09), and [M13](#m13). It develops the second local estimate needed to treat coherent processing.

**Conceptual connection.** W1 and W2 share a hypercontractive rank mechanism but control different operational quantities. A likelihood argument for a classical record does not by itself bound a retained quantum state.

**Source pointers.** [Watrous Definition 3.11 and Eq. (3.64)](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Weighted bounds: root-fidelity bound and proof](../science/weighted_bounds.md#root-fidelity-bound).

<a id="m18"></a>
### M18. Conditioning onto physical low-weight hypotheses

**Central question.** How can the convenient product prior be restricted to the actual target family without losing the exponent?

**Understanding target.** Explain why the identity label cannot be used as a nonidentity spike hypothesis. Track the conditioning factor $`1/p_A`$, the binomial weight distribution, and the choice $`x=w/[3(2n-w)]`$. Relate $`p_A\geq1/4`$ and $`\gamma=w/(3n-w)`$ to the uniform finite bounds.

**Dependencies and story role.** Uses [M03](#m03), [M04](#m04), [M13](#m13), [M16](#m16), and [M17](#m17). It makes both averaged operator estimates applicable to valid physical alternatives.

**Conceptual connection.** A proof distribution and a promised physical family are separate objects until normalization and support are checked. The constant prior mass retains the support–memory exponent; the full-family endpoint permits a stronger prior choice.

**Source pointers.** [Weighted bounds: conditioning on required nonidentity targets, Lemma W3](../science/weighted_bounds.md#conditioning-on-required-nonidentity-targets); [Coherent memory: physical hard family](../science/coherent_memory.md#physical-hard-family).

<a id="m19"></a>
### M19. The response of one call with a bounded reference

**Central question.** How does W2 bound the distinguishability produced by a single changed channel call?

**Understanding target.** Define $`B_e(\omega)=\operatorname{Tr}_S[(P_e\otimes I)\omega]`$ and relate the output-difference trace norm to $`a\|B_e(\omega)\|_1`$. For pure inputs, use the Schmidt representation to identify this norm with $`f_e(\rho_S)`$. Extend the bound to mixed inputs and classical blocks by convexity inside the declared registers.

**Dependencies and story role.** Uses [M06](#m06), [M09](#m09), [M10](#m10), [M17](#m17), and [M18](#m18). It turns an operator lemma into a statement at one invocation of the allowed processor.

**Conceptual connection.** The reference affects how strongly one unknown Pauli direction can survive in the output difference. Neither mixed states nor arbitrarily long classical histories create extra coherent width.

**Source pointers.** [Coherent memory: one call with a bounded reference](../science/coherent_memory.md#one-call-with-a-bounded-reference); [Coherent memory: pure inputs](../science/coherent_memory.md#pure-inputs); [Coherent memory: mixed inputs and classical histories](../science/coherent_memory.md#mixed-inputs-and-classical-histories).

<a id="m20"></a>
### M20. A forward hybrid for the complete coherent protocol

**Central question.** How can a bound for a label-independent input control an adaptive execution whose actual state depends on the hidden label?

**Understanding target.** Compare executions with an increasing prefix of null-channel calls and a common spike-channel suffix. Explain why the input at the differing call is independent of the hidden label, why the common suffix contracts trace distance for each fixed label, and why summing over slots charges every channel invocation. Include inactive branches after an early halt.

**Dependencies and story role.** Uses [M09](#m09), [M10](#m10), [M18](#m18), and [M19](#m19). It scales the one-call obstruction to arbitrary retained coherence and feedback.

**Conceptual connection.** The direction of the hybrid is essential. It allows the original prior to be averaged at a null-generated state without replacing an unknown posterior by that prior.

**Source pointers.** [Coherent memory: forward hybrid for adaptive coherent protocols](../science/coherent_memory.md#forward-hybrid-for-adaptive-coherent-protocols); [Interpretation: why coherent reuse does not remove the obstruction](../science/interpretation.md#why-coherent-reuse-does-not-remove-the-obstruction).

<a id="m21"></a>
### M21. Late-index learning forces a coherent query lower bound

**Central question.** Why does a reusable coefficient record have to distinguish the hard channel alternatives?

**Understanding target.** Choose a positive spike of amplitude $`a=3\epsilon`$ and separate the null and spike estimation intervals using a final target-dependent threshold. Explain why the index may be revealed for that final decision while remaining unavailable during acquisition. Combine the required distance $`1-2\delta`$ with the hybrid to obtain Theorem C1.

**Dependencies and story role.** Uses [M05](#m05), [M09](#m09), [M14](#m14), [M18](#m18), and [M20](#m20). It completes the general coherent lower-bound argument.

**Conceptual connection.** A pointwise guarantee is enough for the reduction, and a retained bounded quantum output does not defeat it. The resulting finite lower bound has $`\epsilon^{-1}`$ dependence; it does not establish the fresh model's stronger accuracy factor.

**Source pointers.** [Coherent memory: statement and resource contract, Theorem C1](../science/coherent_memory.md#statement-and-resource-contract); [Coherent memory: learning-to-testing reduction and finite constants](../science/coherent_memory.md#learning-to-testing-reduction-and-finite-constants).

<a id="m22"></a>
### M22. A fixed sign across fresh-experiment transcripts

**Central question.** Why does complete measurement between calls permit a quadratic inverse-accuracy lower bound?

**Understanding target.** Form the likelihood product for one fixed channel sign across the entire execution. Explain why averaging the two complete transcript laws is different from averaging the channel independently at every call. Use the signed-product inequality and the weighted second moment at null histories to obtain the fresh lower bound proportional to $`\epsilon^{-2}2^{wD/(3n-w)}`$.

**Dependencies and story role.** Uses [M09](#m09), [M10](#m10), [M15](#m15), [M16](#m16), [M18](#m18), and [M21](#m21). It sharpens the finite rate for the restricted fresh model and explains why that sharpening needs another argument.

**Conceptual connection.** Classical adaptivity is handled by averaging experiments chosen along null transcripts. The sign-mixture method is attributed to its prior framework, while the weighted response supplies the evaluated support–memory dependence.

**Source pointers.** [Fresh experiments: the signed transcript bound](../science/fresh_experiments.md#the-signed-transcript-bound); [Fresh experiments: from learning to a decision](../science/fresh_experiments.md#from-learning-to-a-decision); [Fresh experiments: consequences and model boundary](../science/fresh_experiments.md#consequences-and-model-boundary); [KimOh2026](../references/RELATED_WORK.md#kimoh2026).

<a id="m23"></a>
### M23. Partial-Bell usability across all target supports

**Central question.** How does randomly distributing $`k`$ Bell pairs make one record useful for a later unknown target?

**Understanding target.** Define compatibility by the target's nonidentity factors at unpaired sites. Derive the exact hypergeometric usability probability $`p_u`$ for a target of weight $`u`$, and explain the Jensen lower bound $`p_u\geq3^{-uD/n}`$. Interpret the full-reference and no-reference endpoints.

**Dependencies and story role.** Uses [M03](#m03), [M05](#m05), [M07](#m07), [M11](#m11), and [M14](#m14). It gives the local-to-global construction that complements the lower bounds.

**Conceptual connection.** Random paired sites spread a fixed reference budget across every possible support. The average number of unpaired relevant sites, $`uD/n`$, is the constructive origin of the threshold parameter.

**Source pointers.** [Partial-Bell protocol: compatibility with a requested target](../science/partial_bell.md#compatibility-with-a-requested-target); [Partial-Bell protocol: exact usability probability](../science/partial_bell.md#exact-usability-probability); [Partial-Bell protocol: endpoints and related tasks](../science/partial_bell.md#endpoints-and-related-tasks).

<a id="m24"></a>
### M24. The simultaneous learning guarantee

**Central question.** How does the usable sign become a finite, reusable estimate for the whole family?

**Understanding target.** Explain the estimator $`X_e=H_eY_e/p_u`$, its mean $`\lambda_e`$, and its second moment $`1/p_u`$. Combine Bernstein concentration with a union bound to show that the simultaneous guarantee is achievable with

```math
N\leq\left\lceil
4\epsilon^{-2}3^R\ln(2M_w/\delta)
\right\rceil.
```

**Dependencies and story role.** Uses [M04](#m04), [M11](#m11), and [M23](#m23). It completes the constructive learning argument with explicit accuracy and confidence.

**Conceptual connection.** Settings are independent of the error draw, which makes the estimator unbiased. Estimates of different targets may be correlated; a simultaneous guarantee still follows and supports requests selected after inspecting the record.

**Source pointers.** [Partial-Bell protocol: unbiased estimation and its variance](../science/partial_bell.md#unbiased-estimation-and-its-variance); [Partial-Bell protocol: simultaneous guarantee](../science/partial_bell.md#simultaneous-guarantee).

<a id="m25"></a>
### M25. The learning frontier and its resource meaning

**Central question.** What do the distinct finite upper and lower bounds jointly establish?

**Understanding target.** Combine the coherent lower bound with the fresh upper construction to show that polynomial query complexity is possible exactly when $`R=O(\log n)`$ at fixed nontrivial accuracy and confidence. Interpret the permitted varying-precision regimes and examples with small, intermediate, or extensive weight. Distinguish a matched polynomial frontier from an optimal exponential constant.

**Dependencies and story role.** Uses [M14](#m14), [M21](#m21), [M22](#m22), and [M24](#m24). This is the first global synthesis of the narrative: the complete learning theorem and its implementation.

**Conceptual connection.** Acquisition uses $`O(nN)`$ classical bits, and one coefficient can be decoded by scanning that record with polynomial-bit arithmetic. A polynomial query theorem does not promise polynomial time to print an exponentially long output list. The detector developed next addresses a one-bit output directly.

**Source pointers.** [Coherent memory: polynomial query frontier](../science/coherent_memory.md#polynomial-query-frontier); [Partial-Bell protocol: physical and classical resources](../science/partial_bell.md#physical-and-classical-resources); [Interpretation: distinct asymptotic regimes](../science/interpretation.md#distinct-asymptotic-regimes).

<a id="m26"></a>
### M26. The physical meaning of one preserved correlation

**Central question.** What physical channel lies behind the positive-spike decision promise?

**Understanding target.** Relate the positive spike to a uniform Pauli-error distribution on the commuting hyperplane and to measuring one parity followed by randomization within its eigenspace. Explain its succinct specification and sampler. Distinguish the entanglement-breaking channel at $`\tau=1`$ from its identity mixtures at smaller known $`\tau`$.

**Dependencies and story role.** Uses [M02](#m02), [M04](#m04), [M12](#m12), [M14](#m14), and [M25](#m25). It interprets the hard-family mechanism as a physical decision problem whose answer has only one bit.

**Conceptual connection.** The difficulty can concern access to an unknown preserved correlation even when the alternative has a short classical description and need not preserve input entanglement. The channel-distance witness does not grant the tester extra reference qubits.

**Source pointers.** [Watrous §§3.3.1–3.3.3, channel discrimination and the completely bounded trace norm](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf); [Correlation detection: promise and finite theorem](../science/correlation_detection.md#1-promise-and-finite-theorem); [Correlation detection: a succinct physical channel family](../science/correlation_detection.md#2-a-succinct-physical-channel-family); [Interpretation: one retained classical correlation is enough](../science/interpretation.md#one-retained-classical-correlation-is-enough); [ChenGong2025](../references/RELATED_WORK.md#chengong2025).

<a id="m27"></a>
### M27. A direct lower bound for a one-bit decision

**Central question.** Why is deciding the positive-spike promise hard even when the hidden label is never requested?

**Understanding target.** Apply the bounded-reference response and forward hybrid to the known baseline $`\Gamma_0`$ and each alternative $`\Gamma_P`$. Use the success of one fixed decision rule to force distance at least $`1-2\delta`$ for every allowed label. Obtain the direct lower bound proportional to $`\tau^{-1}2^{wD/[2(3n-w)]}`$.

**Dependencies and story role.** Uses [M09](#m09), [M18](#m18), [M19](#m19), [M20](#m20), and [M26](#m26). It extends the established obstruction to the smaller-output task on its own terms.

**Conceptual connection.** Detection hardness is proved directly, with neither a revealed index nor an inference that every detection problem must be as difficult as learning.

**Source pointers.** [Correlation detection: direct coherent lower bound](../science/correlation_detection.md#3-direct-coherent-lower-bound); [Coherent memory: detection and weak noise](../science/coherent_memory.md#detection-and-weak-noise).

<a id="m28"></a>
### M28. An efficient rank detector

**Central question.** How can the same support–memory boundary be attained with polynomial classical processing?

**Understanding target.** Explain why a compatible partial-Bell setting yields syndromes with an exact homogeneous constraint. Relate the number of random settings to compatibility and the number of repeated calls per setting to the null rank-deficiency probability. Explain the finite $`J,L`$ choices and streaming Gaussian elimination without searching all Pauli labels.

**Dependencies and story role.** Uses [M07](#m07), [M12](#m12), [M23](#m23), [M26](#m26), and [M27](#m27). It completes the one-bit lower-and-upper result, including computational cost.

**Conceptual connection.** Any compatible block under the alternative has deficient raw linear rank deterministically, while the specified null has deficient rank only with controlled probability. Exact preservation is essential to this algorithm; a noisy unknown parity need not leave a rank defect.

**Source pointers.** [Correlation detection: partial-Bell settings expose a linear syndrome, Eqs. (D10)–(D11)](../science/correlation_detection.md#4-partial-bell-settings-expose-a-linear-syndrome); [Correlation detection: the linear-rank algorithm, Eqs. (D12)–(D14)](../science/correlation_detection.md#5-the-linear-rank-algorithm); [Correlation detection: scope and verification](../science/correlation_detection.md#6-scope-and-verification).

<a id="m29"></a>
### M29. Weak channels and relative accuracy

**Central question.** What changes when informative channel effects are rare?

**Understanding target.** Interpret the known identity mixture $`\widetilde\Lambda=(1-\tau)\operatorname{Id}+\tau\Lambda`$. Explain how centering at the identity reduces the upper estimator variance, and how an outcome-weighted likelihood second moment produces the fresh lower factor $`\tau/\epsilon^2`$. Distinguish absolute error from $`\epsilon=\alpha\tau`$ with fixed $`0<\alpha<1/3`$. At fixed nontrivial confidence, derive the relative-accuracy frontier $`R+\log(1/\tau)=O(\log n)`$.

**Dependencies and story role.** Uses [M11](#m11), [M20](#m20), [M22](#m22), [M24](#m24), [M25](#m25), and [M28](#m28). It unifies the acquisition models and the one-bit result with the cost of rare information.

**Conceptual connection.** No flag identifies the mixture branch. Resolving a fixed fraction of a very small noise scale still costs calls, even with a full reference. If instead $`\epsilon\geq\tau`$, returning the known midpoint $`1-\tau`$ requires no data. These weak channels allow rare global correlations and do not impose a local-noise model.

**Source pointers.** [Weak channels: channel class and finite bounds](../science/weak_noise.md#channel-class-and-finite-bounds); [Weak channels: a lower bound that counts the rare informative calls](../science/weak_noise.md#a-lower-bound-that-counts-the-rare-informative-calls); [Weak channels: an estimator centered at the identity](../science/weak_noise.md#an-estimator-centered-at-the-identity); [Weak channels: coherent processing and the polynomial frontier](../science/weak_noise.md#coherent-processing-and-the-polynomial-frontier).

<a id="m30"></a>
### M30. The complete result, its attribution, and its limits

**Central question.** What is the project's full scientific conclusion, and exactly which distinctions keep it valid?

**Understanding target.** Explain one connected story from an unknown Pauli direction, through weighted rank suppression and a coherent hybrid, to the partial-Bell upper bound and the polynomial learning threshold. Extend that explanation to the promised efficient detector and the relative-noise criterion. Identify which foundations and mechanisms are established prior work, which weighted and operational statements are proved in the repository, and which stronger rate claims are not established.

**Dependencies and story role.** Integrates the entire map, especially [M16](#m16), [M17](#m17), [M21](#m21), [M22](#m22), [M25](#m25), [M28](#m28), and [M29](#m29). This is the narrative phase's global synthesis.

**Conceptual connection.** Keep the complete support-and-axis family, ordinary memoryless access, charged coherent width, ideal constructive controls, distinct accuracy factors, and exact detection promise in the same account. Finite verification checks algebra and implementations; the analytical proofs establish the general bounds. Neither those checks nor the matched polynomial frontier establish an optimal exponent, Kim–Oh S85, a generic noisy-parity algorithm, or resilience to arbitrary reference and measurement noise.

**Source pointers.** [Interpretation](../science/interpretation.md); [Model: computation, storage, and precision](../science/model.md#computation-storage-and-precision); [Related work: closest comparisons](../references/RELATED_WORK.md#closest-comparisons); [Related work: attribution and comparison rules](../references/RELATED_WORK.md#attribution-and-comparison-rules); [Verification](../verification/README.md).

## Reading routes

For the physical story, follow M01–M07, M10–M12, M14, and M23–M30, returning to the operator milestones when examining the converse. For the complete proof route, follow the numbered order and use each linked scientific page as the authoritative statement. The [Watrous bridge](WATROUS_BRIDGE.md) supplies the source-to-project translation; the [worked example](WORKED_EXAMPLE.md) supplies a concrete operational entrypoint.
