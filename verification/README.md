# Finite verification

These programs check the finite matrix identities and binary probability laws
used in the analytical proofs. They cover small systems exhaustively where
practical and use fixed random seeds for matrix examples. The proofs in
[science/](../science/model.md) establish the universal statements.

## Run

Use Python 3.11 or later. The numerical programs use NumPy; the syndrome
program uses only the Python standard library.

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The recorded run used Python 3.12 and NumPy 2.3.5. The runner invokes each
program, stops on an assertion or a changed result, and prints:

```text
PASS verify_operator_bounds.py
PASS verify_fresh_likelihood.py
PASS verify_syndromes.py
{
  "checks_passed": 3
}
```

Each program can also be run individually. It writes a JSON summary to standard
output. The [expected results](expected/) retain the successful summaries.

## Analytical figure

The [resource-figure guide](../figures/README.md) documents a separate plotting route, with its Python generator, pinned dependencies, panel parameters, and canonical formulas. The figure evaluates those formulas directly; the finite checks below verify the identities used in the proofs.

## What is checked

| Program | Coverage | Scientific use |
|---|---|---|
| [verify_operator_bounds.py](verify_operator_bounds.py) | 14 matrix cases through four system qubits; 42 weighted root-fidelity cases; 42 complex-matrix weighted cases; 102 three-query coherent circuits through two system qubits. | Checks the fidelity/trace-norm identity, the Hölder and weighted rank inequalities, Pauli Parseval normalization and coefficient caps, and the forward-hybrid bound. See [weighted bounds](../science/weighted_bounds.md) and [coherent memory](../science/coherent_memory.md). |
| [verify_fresh_likelihood.py](verify_fresh_likelihood.py) | 909 nonidentity signal cases through three system qubits, with every reference width from zero through the system size and complex input/effect amplitudes. | Compares direct contraction of physical system-reference states and measurement effects with the coefficient-matrix likelihood formula, including Pauli Y factors. See [fresh experiments](../science/fresh_experiments.md). |
| [verify_syndromes.py](verify_syndromes.py) | All 84 partial-Bell settings and 4,284 setting–hidden-label pairs through three system qubits; 303 compatibility probabilities; 37,802 enumerated null sample sequences; 225 exact rank/union-bound cases; 120 finite choices of the block parameters. | Checks syndrome projection, the exact preserved constraint, weak-null probabilities, compatibility sampling, and the rank algorithm's finite error bounds. See [correlation detection](../science/correlation_detection.md). |

The matrix checks use seeds 41286 and 69920261018. The operator program permits
absolute residuals up to `2e-10`; the physical likelihood program requires
residuals below `1e-12`. The recorded largest operator identity residual was
below `2e-15`, and the largest likelihood probability residual was below
`1.2e-16`. Small floating-point differences across numerical libraries are
expected. The runner compares floating-point summaries with relative tolerance
`1e-9` and absolute tolerance `2e-10`; the assertions inside each program remain
in force.

The syndrome program uses integers and exact rational arithmetic for its
probability identities. Floating point is used only to select the finite
integer block parameters from the logarithmic formulas. Its exact checks
include both the identity-mixture null and the hidden-hyperplane alternative.

## Interpretation and limits

These checks make normalization, complex conjugation, phase conventions, and
finite probability calculations reproducible. Random matrix examples do not
exhaust all inputs or coherent strategies. Small-system enumeration does not
establish an asymptotic lower bound or validate a claim of optimal constants.
Those conclusions depend on the explicit proofs and their cited analytic input.

The programs simulate the ideal mathematical model. They do not evaluate
hardware noise, imperfect state preparation or measurement, approximate
preserved parities, or noisy reference storage.
