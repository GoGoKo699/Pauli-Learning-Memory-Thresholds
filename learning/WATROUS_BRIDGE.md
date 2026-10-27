# From Watrous to the Pauli learning threshold

The educational anchor is **John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/), Cambridge University Press, 2018**. The section and equation pointers below refer to the author's linked pre-publication chapter files, whose front matter is dated January 2018. They provide a route into this project without requiring a sequential reading of the entire book.

Watrous supplies the language of finite quantum systems, channels, measurements, operator norms, and distinguishability. The project adds a particular learning task, a restriction on coherent resources, weighted Pauli estimates, and algorithms. The distinction matters: a textbook channel representation does not establish a query lower bound, and the selected educational anchor does not replace the primary research ingredients in [related work](../references/RELATED_WORK.md).

Use the [30-milestone map](MILESTONES.md) for the complete sequence of understanding targets. The [worked example](WORKED_EXAMPLE.md) shows what the apparatus actually prepares, records, and computes with two system qubits and one reference qubit. This bridge explains how those operations connect to the general proofs.

## Start with the experimental question

A Pauli correlation is measured by choosing an axis $`X`$, $`Y`$, or $`Z`$ at each active site and multiplying the resulting signs. For example, measuring $`X`$ on one qubit and $`Z`$ on another gives the outcome of $`X\otimes Z`$. Identity factors ignore their sites; the remaining sites form the support.

A Pauli channel applies a random tensor product of Pauli errors. Its error distribution is unknown and may contain correlations between distant sites. For a target Pauli $`P_e`$, the eigenvalue $`\lambda_e`$ is the mean sign indicating whether the random error commutes or anticommutes with that target:

```math
\lambda_e=\mathbb E_v(-1)^{[e,v]}.
```

Here $`[e,v]`$ is zero for commuting operators and one for anticommuting operators, and $`\mathbb E_v`$ averages over the error draw. The coefficient also has an input–output meaning: an input mean $`\mathrm{Tr}(P_e\rho)`$ becomes $`\lambda_e\mathrm{Tr}(P_e\rho)`$. For a one-qubit channel that applies $`I`$ with probability $`0.9`$ and $`X`$ with probability $`0.1`$, the $`Z`$ coefficient is $`0.9-0.1=0.8`$.

The experimenter must acquire a reusable record before learning which target will be requested. The family contains every support and every choice of axes through weight $`w`$. A reference bypasses the unknown channel but can be prepared and measured jointly with the system. One reference qubit paired with a system qubit can reveal both local error bits through a Bell measurement. An unpaired system qubit, prepared and measured along one Pauli axis, reveals one commutation bit. The central question is how much coherent reference capacity is needed to make an initially unknown target accessible.

The [model](../science/model.md) fixes the three parameters: the channel acts on $`n`$ qubits, every target has weight at most $`w`$, and all coherent registers outside the queried register have total width at most $`k`$ at each invocation. Write

```math
D=n-k,\qquad R=\frac{wD}{n}.
```

In the upper construction, $`R`$ bounds the average number of target sites lacking a reference. In the converse, $`D`$ appears through a rank-to-dimension ratio and combines with the weight-dependent prior. Connecting these two mechanisms gives the polynomial-query frontier.

## Relevant parts of the anchor

These are source pointers for specific concepts. The last column identifies the additional project step, whose exact statement remains in its scientific home.

| Watrous pointer | Foundation to use | Project connection |
|---|---|---|
| [§1.1.2, Linear operators](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), especially the vec and partial-trace identities (1.133)–(1.134) | Matrix representations of bipartite vectors and reduced operators. | Check the transposes in the [fresh-experiment likelihood](../science/fresh_experiments.md#the-one-experiment-likelihood). |
| [§1.1.3, Operator decompositions and norms](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), Schmidt decomposition (1.162)–(1.164), rank comparison (1.169), and Hölder inequality (1.174) | Singular values, rank, and ordinary Schatten norms. | Convert reference dimension into the rank restriction in [the weighted bounds](../science/weighted_bounds.md). |
| [§2.1.3, Reductions and purifications of quantum states](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), Theorem 2.10 | The auxiliary dimension needed for a purification. | Apply the rank restriction to pure inputs; extend to actual mixed inputs without adding accessible memory. |
| [§§2.2.1–2.2.3, Quantum channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), including the Choi representation (2.64) and classical–quantum form (2.170) | Ordinary channel action, representations, and classical registers. | Specify the [access contract](../science/model.md#coherent-access) and its charged registers. |
| [§§2.3.1–2.3.2, Measurements](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), instruments (2.258)–(2.262) | Outcome probabilities and retained conditional quantum states. | Distinguish a fresh experiment from adaptive processing with persistent coherence. |
| [§3.1.1, Discriminating between pairs of quantum states](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Theorem 3.4 | The operational meaning of trace-norm separation. | Turn an accurate coefficient estimate into a test in [the coherent converse](../science/coherent_memory.md#learning-to-testing-reduction-and-finite-constants). |
| [§3.2, The fidelity function](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Definition 3.11 and Eq. (3.64) | Unsquared fidelity. | Recognize the single-call response controlled by [Lemma W2](../science/weighted_bounds.md#root-fidelity-bound). |
| [§§3.3.1–3.3.3, Channel distances and discrimination](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), including Corollary 3.40 | Auxiliary systems, the completely bounded trace norm, and trace-norm contraction. | Separate an unrestricted channel norm from the bounded-reference estimate needed at every query. |

The [anchor's contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) give the surrounding chapter structure. For the present results, the weighted prior, classical likelihood calculation, concentration estimate, and binary syndrome argument are developed in the repository. They are not assigned to unrelated textbook chapters.

## Conventions that must survive the translation

### Ordinary and normalized Schatten norms

Watrous uses ordinary Schatten norms in §1.1.3. The physical trace norm on this project's states and output differences uses the same convention. The hypercontractive inequality instead uses the normalized trace. For a $`d`$-by-$`d`$ matrix and finite $`p\ge1`$,

```math
\|A\|_p=\bigl(\mathrm{Tr}|A|^p\bigr)^{1/p},
\qquad
\|A\|_{p,\mathrm{av}}
=\left(\frac{\mathrm{Tr}|A|^p}{d}\right)^{1/p}
=d^{-1/p}\|A\|_p.
```

Consequently, for rank $`r`$ and $`1\le p\le2`$, the ordinary rank comparison becomes

```math
\|A\|_{p,\mathrm{av}}
\le
\left(\frac rd\right)^{1/p-1/2}
\|A\|_{2,\mathrm{av}}.
```

The normalization makes the identity matrix have norm one. For example, two system qubits give $`d=4`$, while one reference qubit permits a pure probe with system rank at most two, hence $`r/d\le1/2`$.

Here the division by $`d`$ is load-bearing. With $`r\le2^k`$ and $`d=2^n`$, the relevant ratio is at most $`2^{-D}`$. Dropping the normalization loses the dimension-dependent suppression. Conversely, inserting a normalized trace norm into a physical distinguishability formula introduces an incorrect factor of $`d`$. [The weighted proof](../science/weighted_bounds.md#hypercontractivity-and-the-rank-comparison) keeps these uses separate and derives the conversion explicitly.

### Root fidelity and squared fidelity

Watrous's $`F(\rho,\sigma)`$ is unsquared, as specified in Definition 3.11. This project's term *root fidelity* uses that same quantity:

```math
F(\rho,\sigma)=\|\sqrt{\rho}\sqrt{\sigma}\|_1,
\qquad
f_e(\rho)=F(\rho,P_e\rho P_e)
=\|\sqrt{\rho}P_e\sqrt{\rho}\|_1.
```

The final equality uses $`\sqrt{P_e\rho P_e}=P_e\sqrt{\rho}P_e`$ and unitary invariance of the trace norm. Lemma W2 bounds an average of $`f_e(\rho)^2`$. The square belongs to the second-moment estimate; it does not redefine the fidelity appearing in the single-call response.

### Trace distance, total variation, and diamond norm

The project writes

```math
\mathrm{TD}(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\qquad
\mathrm{TV}(p,q)=\frac12\sum_z|p(z)-q(z)|.
```

A measurement cannot produce outcome distributions with total variation exceeding the input trace distance. A test with error at most $`\delta`$ under each of two hypotheses therefore requires distance at least $`1-2\delta`$. This is the testing normalization used in both converse proofs.

Watrous's completely bounded trace norm, denoted by a triple-bar trace norm in §3.3.2, is written $`\|\Phi\|_\diamond`$ here. It is the **full** norm. Thus the weak-channel statement $`\|\widetilde\Lambda-\mathrm{Id}\|_\diamond\le2\tau`$ has no extra factor of one half. This unrestricted norm describes the channel pair; the memory-sensitive lower bound uses the response on each allowed input and then averages over hidden targets. Optimizing an input separately for each hidden target would change the learning task.

### Vectors, adjoints, and the fresh-response matrix

Watrous writes vectors as $`u`$, pure states as $`uu^*`$, and adjoints as $`A^*`$. The project also uses $`|\psi\rangle`$, $`|\psi\rangle\langle\psi|`$, and $`A^\dagger`$. These are notation translations, not different state conventions.

For the fresh-experiment proof, write a pure input and a rank-one effect using system-by-reference matrices $`\Psi`$ and $`M`$. The relevant matrix is

```math
C=M\Psi^\dagger,\qquad
q_{\mathcal D}=\frac{\|C\|_F^2}{d},\qquad
\frac{q_{e,s}}{q_{\mathcal D}}
=1+sa\,
\frac{\mathrm{Tr}(P_eCP_eC^\dagger)}
     {\mathrm{Tr}(CC^\dagger)}.
```

The reference reduction obeys $`\rho_A^{\mathsf T}=\Psi^\dagger\Psi`$ with this coefficient convention. The [component calculation](../science/fresh_experiments.md#the-one-experiment-likelihood) fixes the transposes before simplifying the probability. Although the response is real, $`C`$ need not be Hermitian or normal. Its rank is at most the reference dimension, which is the property the weighted lemma needs.

## Which systems are actually available?

The register language of Chapter 2 permits an exact resource statement. At each invocation, the unknown channel acts on an $`n`$-qubit register $`S`$ and leaves an accessible reference $`A`$ untouched. Every coherent register outside $`S`$, including a controller or retained workspace, counts toward $`\dim A\le2^k`$. An unrestricted classical history is stored as orthogonal blocks and may select the next known operation. It supplies feedback without supplying a coherent copy of that history. The queried system itself may retain coherence between calls. See [the full contract](../science/model.md#coherent-access).

For a **pure** state on $`S\otimes A`$, the reduced state on $`S`$ has rank at most $`\dim A`$. A mixed input does not generally have a reduced state of that rank. The coherent proof therefore decomposes the mixed input into pure states inside its existing $`S\otimes A`$ space and uses convexity. It does not replace the input by an accessible purification on a larger register. This is the operational use of the purification and Schmidt-rank foundations.

A channel's mathematical representation also needs to be separated from its access mechanism. Applying the channel to half of a normalized maximally entangled state would produce $`J(\Lambda)/d`$ in Watrous's Choi convention. Preparing that experiment uses $`n`$ reference qubits beside the $`n`$ queried qubits. Copies of this normalized Choi state are therefore not supplied for free when $`k<n`$. Similarly, a Stinespring representation establishes that a dilation exists; it does not grant access to the unknown environment or its inverse.

The counted resource $`N`$ is the number of ordinary channel invocations. Ten invocations inside one coherent block cost ten queries even if only one measurement is made at the end. Independent channel uses also do not mean that an adaptive experiment's full quantum inputs or classical outcomes are independent. The [forward hybrid](../science/coherent_memory.md#forward-hybrid-for-adaptive-coherent-protocols) is what controls their dependence.

## The additional steps supplied by the project

### 1. Put weight and reference dimension into the same estimate

The Pauli product prior weights labels by their support size and becomes uniform at its full-family endpoint. Averaging conjugation under that prior acts as a tensor product of qubit depolarizing maps. [Lemma W1 and Lemma W2](../science/weighted_bounds.md) combine this identity with the rank comparison and King's hypercontractivity theorem to bound two responses: a complex-matrix likelihood response and a root-fidelity response.

The imported theorem is [King2014, Corollary 2](../references/RELATED_WORK.md#king2014), with the complex-matrix domain and normalized norms stated explicitly. It is a research dependency. The project supplies the Pauli averaging, the two weighted applications, and the conditioning that restricts the prior to physical nonidentity targets of weight at most $`w`$. A proposed sharper weighted inequality in the literature is not used as a proved input.

### 2. Control a whole coherent experiment

At one invocation, the difference between a positive-spike channel and depolarization is a tensor product involving

```math
B_e(\omega)=\mathrm{Tr}_S[(P_e\otimes I_A)\omega].
```

For a pure input, $`\|B_e(\omega)\|_1`$ equals the root-fidelity response of its reduced state. The weighted bound therefore limits how strongly a bounded-reference input can respond on average to a hidden target.

The remaining problem is adaptivity: after seeing a spike, the apparatus can carry information about its label into later inputs. The [coherent converse](../science/coherent_memory.md) compares adjacent executions whose common prefix uses the null channel. The input at the changed invocation is then independent of the hidden label. Their common suffix contracts trace distance, and summing over invocations bounds the final separation. A successful late-index estimate forces that separation to be large. The resulting inverse-accuracy lower factor is $`\epsilon^{-1}`$.

### 3. Use the additional structure of fresh experiments

When every call ends in complete measurement, the outcome probabilities can be multiplied along a classical transcript. [The fresh converse](../science/fresh_experiments.md) uses signed spike alternatives with one sign fixed for the whole execution. Averaging the two complete transcript laws cancels the first-order likelihood response and leaves a second-moment bound proportional to $`N a^2`$.

This yields the stronger $`\epsilon^{-2}`$ lower factor. Averaging the channel sign independently on each call would describe a different experiment and would not prove this result. The fresh and coherent lower bounds share a polynomial frontier while retaining distinct finite accuracy statements.

### 4. Turn compatible records into a learning algorithm

For a weight-$`u`$ target, the random partial-Bell setting is usable with probability

```math
p_u=\mathbb E_K 3^{-|\mathrm{supp}(e)\setminus K|}
\ge3^{-uD/n}.
```

The [construction](../science/partial_bell.md) divides a usable commutation sign by $`p_u`$ and returns zero on an unusable record. This gives an unbiased estimator with second moment $`1/p_u`$. A variance-sensitive concentration bound then costs $`p_u^{-1}`$ rather than $`p_u^{-2}`$. A union bound supplies simultaneous estimates from the same stored record. The output is that record and its evaluation rule; printing an exponentially long coefficient list has its own output cost.

### 5. Recognize when one-bit detection becomes linear algebra

An exactly preserved positive Pauli spike restricts the error labels to a homogeneous binary hyperplane: the bit strings satisfying one nonzero parity equation. A parity is the sum of selected bits modulo two, also called XOR. A compatible partial-Bell setting makes that equation accessible through its $`n+k`$ recorded bits. Every observed row then satisfies the same equation, so the rows cannot span all binary directions. Their rank, the number of independent rows over $`\mathbb F_2`$, is deficient.

[The detector](../science/correlation_detection.md) searches for rank deficiency across random settings, using Gaussian elimination rather than enumerating candidate Paulis. It has a direct testing lower bound. Exact preservation is essential: a noisy parity constraint no longer makes all recorded rows lie in a proper subspace, so the same rank algorithm does not establish an efficient detector for arbitrary small deviations from the null.

### 6. Resolve the precision scale near the identity

For a known mixture $`(1-\tau)\mathrm{Id}+\tau\Lambda`$, the [weak-channel account](../science/weak_noise.md) centers its estimator on the identity response. The resulting variance and fresh lower bound both have scale $`\tau/\epsilon^2`$. No branch flag is observed. With fixed relative accuracy $`\epsilon=\alpha\tau`$, $`0<\alpha<1/3`$, the additional query cost is proportional to $`1/\tau`$.

The joint polynomial condition is consequently $`R+\log(1/\tau)=O(\log n)`$. At a coarse absolute tolerance $`\epsilon\ge\tau`$, the known midpoint already estimates every nonidentity coefficient without data. The precision qualification is therefore part of the physical statement. Rare global Pauli errors are allowed throughout; proximity to the identity does not impose a spatially local noise model.

## Reading the complete story

The [milestone map](MILESTONES.md) allocates M01–M14 to background and M15–M30 to the project's argument. Its first phase assembles individual operators, experiments, probabilities, and resource distinctions into the learning problem. Its second phase connects the weighted responses to lower bounds, the sampling protocol, the detector, and the final scope.

For a concrete entry, use the [worked example](WORKED_EXAMPLE.md), then identify its operations in [partial-Bell learning](../science/partial_bell.md) and [correlation detection](../science/correlation_detection.md). For the universal obstruction, read [weighted bounds](../science/weighted_bounds.md) together with [coherent memory](../science/coherent_memory.md). The [interpretation](../science/interpretation.md) brings the two directions together. The general theorems are established by those analytical arguments; the [finite verification programs](../verification/README.md) check selected identities and implementations.
