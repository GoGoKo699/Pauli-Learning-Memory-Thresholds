# Pauli Learning Memory Thresholds

**How much coherent memory is needed to learn the coefficient of a quantum correlation whose support and measurement axes are revealed only after data collection?** This project gives a joint threshold in the correlation weight and the memory available beside an unknown Pauli channel.

A Pauli correlation is a tensor product of the single-qubit operators $`I,X,Y,Z`$; its weight counts the factors different from $`I`$. A Pauli channel applies random Pauli errors, possibly correlated across sites. Its coefficient $`\lambda_P`$ describes how much of a correlation survives: $`\Lambda(P)=\lambda_P P`$.

Let $`n`$ be the number of channel qubits and $`w`$ the maximum requested Pauli weight. At every channel invocation, count all coherent registers outside the queried $`n`$-qubit register in a budget of $`k`$ qubits, with $`0\le k\le n`$. Arbitrary coherent reuse, intermediate measurements, and adaptive feedback are allowed. At fixed nontrivial accuracy and confidence,

```math
\boxed{
\text{polynomially many channel calls are possible}
\quad\Longleftrightarrow\quad
\frac{w(n-k)}{n}=O(\log n).
}
```

The acquisition procedure knows the complete family of supports and axes through weight $`w`$, but it does not know which member will be requested. It produces a reusable record from which that later coefficient can be estimated. Every channel invocation is charged, including invocations inside long coherent blocks. The upper protocol uses local Pauli measurements and partial Bell references; the lower bound allows arbitrary known quantum processing within the width budget.

## Principal results

Write $`D=n-k`$ for the missing reference width and $`R=wD/n`$. Here $`\epsilon`$ is the additive coefficient error, $`\delta`$ the failure allowance, and $`M_w=\sum_{u=0}^w\binom nu3^u`$ the number of Pauli labels through weight $`w`$, including the known identity coefficient. The exact finite statements and proofs have the following homes.

| Result | Content | Proof |
|---|---|---|
| Coherent memory | A weighted root-fidelity bound and a channel hybrid give a lower bound proportional to $`\epsilon^{-1}2^{w(n-k)/[2(3n-w)]}`$. | [Coherent lower bound](science/coherent_memory.md) |
| Fresh experiments | Complete measurement after each call permits a stronger lower bound proportional to $`\epsilon^{-2}2^{w(n-k)/(3n-w)}`$. | [Fresh-experiment bound](science/fresh_experiments.md) |
| Constructive learning | Random partial-Bell probes give simultaneous estimates with $`O(\epsilon^{-2}3^R\log(M_w/\delta))`$ calls and efficient evaluation of an individually requested coefficient. | [Partial-Bell protocol](science/partial_bell.md) |
| One-bit detection | Under the positive-spike promise, detecting one hidden, exactly preserved Pauli correlation against the specified depolarizing baseline has the same frontier and an explicit polynomial-time algorithm in the polynomial regime. | [Correlation detection](science/correlation_detection.md) |
| Weak channels | For known identity-mixture strength $`\tau`$, fixed relative accuracy adds a $`1/\tau`$ query factor. The frontier becomes $`R+\log(1/\tau)=O(\log n)`$. | [Weak-noise rates](science/weak_noise.md) |

For example, learning through weight $`w=\sqrt n`$ requires $`n-k=O(\sqrt n\log n)`$ for polynomial query cost. Learning through weight $`w=\Theta(n)`$ requires $`n-k=O(\log n)`$. The [interpretation](science/interpretation.md) explains these regimes and why coherent reuse does not remove the obstruction.

## Read the science

For the physical story, start with the [channel, memory budget, and exact tasks](science/model.md), then the [interpretation](science/interpretation.md). The [two-qubit example](learning/WORKED_EXAMPLE.md) shows the preparation, readout, and stored record concretely.

For the proofs, the [weighted Pauli bounds](science/weighted_bounds.md) supply the common mathematical input. Follow either the [coherent](science/coherent_memory.md) or [fresh-experiment](science/fresh_experiments.md) converse, then the [partial-Bell construction](science/partial_bell.md). The [one-bit decision theorem](science/correlation_detection.md) makes the small-output consequence explicit, and [weak noise](science/weak_noise.md) treats rare informative events.

The [related-work account](references/RELATED_WORK.md) and [bibliography](references/references.bib) distinguish imported ingredients, previously studied tasks, and nearby access models. Hypercontractivity, the Pauli-spike family, and the general benefit of reference entanglement are established ingredients. The contribution developed here is the evaluated joint support–memory frontier under the specified coherent-width budget.

[The LLM reading guide](llms.txt) maps scientific questions to their authoritative files.

## Learn the project

The single educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/). The learning route connects its foundations to the physical task, the proofs, and the algorithms developed here.

| Entry | What it provides |
|---|---|
| [30-milestone map](learning/MILESTONES.md) | M01–M14 build the background and access model. M15–M30 connect the weighted bounds, coherent and fresh converses, learning construction, detector, and weak-channel result. Each milestone has a central question, understanding target, dependencies, conceptual connection, and source pointers. |
| [Watrous bridge](learning/WATROUS_BRIDGE.md) | Relevant sections and equations, translations of norms and notation, resource assumptions, and the additional arguments needed for this project. |
| [Two-qubit worked example](learning/WORKED_EXAMPLE.md) | A complete partial-Bell setting with one reference qubit, a reusable coefficient estimator, binary syndrome detection, and finite call counts. |

Start with the worked example for a concrete experiment, then follow the milestone map. The linked scientific pages remain the exact statement and proof homes. Primary research citations, including the imported hypercontractivity theorem, retain their separate attribution in the bridge and related-work account.

## Reproduce the finite checks

With Python 3.11 or later, install the numerical dependency and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks cover weighted operator responses, trace-norm identities, short coherent-query hybrids, and exact binary syndrome calculations. They use fixed inputs or random seeds and compare their outputs with the committed expectations. [Verification](verification/README.md) explains the numerical tolerances and exact-arithmetic checks. The universal lower bounds and asymptotic frontier are proved analytically.

## Scope

The channel is memoryless but may contain globally correlated Pauli errors. Its ordinary CPTP action is supplied without inverse, controlled, or purified-channel access. The constructive protocols use ideal controls and reference qubits and require no QRAM. The target family contains all supports and axes through weight $`w`$; a polynomial-sized known list is a different task.

Query complexity, terminal measurement count, classical processing, and explicit output length are separately accounted for. The one-bit detector exploits an exactly preserved correlation. The finite exponential constants and the coherent accuracy dependence are not claimed optimal, and the stronger extremal formula proposed by Kim–Oh remains open.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
