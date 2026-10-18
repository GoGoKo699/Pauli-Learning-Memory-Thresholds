"""Finite check of the coefficient-matrix convention in fresh_experiments.md.

The direct calculation contracts a physical system-reference input state.
The comparison uses C = M Psi^dagger, including complex Pauli Y factors.
This checks normalization and transposes; it does not prove the lower bound.
"""
import itertools
import json

import numpy as np

rng = np.random.default_rng(69920261018)
local_paulis = [
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
]
errors = {
    "null_probability": 0.0,
    "signal_probability": 0.0,
    "reality": 0.0,
}
cases = 0
for n in range(1, 4):
    d = 2**n
    paulis = []
    for label in itertools.product(range(4), repeat=n):
        operator = np.array([[1.0 + 0j]])
        for local_label in label:
            operator = np.kron(operator, local_paulis[local_label])
        paulis.append(operator)
    for k in range(n + 1):
        reference_dimension = 2**k
        for _ in range(3):
            psi_matrix = (
                rng.normal(size=(d, reference_dimension))
                + 1j * rng.normal(size=(d, reference_dimension))
            )
            psi_matrix /= np.linalg.norm(psi_matrix)
            effect_matrix = (
                rng.normal(size=(d, reference_dimension))
                + 1j * rng.normal(size=(d, reference_dimension))
            )
            effect_matrix /= np.linalg.norm(effect_matrix)
            psi = psi_matrix.reshape(-1)
            effect_vector = effect_matrix.reshape(-1)
            state_tensor = np.outer(psi, psi.conj()).reshape(
                d, reference_dimension, d, reference_dimension
            )
            reference_state = np.einsum("iaib->ab", state_tensor)
            direct_null = np.vdot(
                effect_vector,
                np.kron(np.eye(d) / d, reference_state) @ effect_vector,
            )
            coefficient = effect_matrix @ psi_matrix.conj().T
            algebraic_null = np.trace(coefficient @ coefficient.conj().T) / d
            errors["null_probability"] = max(
                errors["null_probability"],
                float(abs(direct_null - algebraic_null)),
            )
            for pauli in paulis[1:]:
                reference_signal = np.einsum("ji,iajb->ab", pauli, state_tensor)
                direct_signal = np.vdot(
                    effect_vector,
                    np.kron(pauli / d, reference_signal) @ effect_vector,
                )
                algebraic_signal = np.trace(
                    pauli @ coefficient @ pauli @ coefficient.conj().T
                ) / d
                errors["signal_probability"] = max(
                    errors["signal_probability"],
                    float(abs(direct_signal - algebraic_signal)),
                )
                errors["reality"] = max(
                    errors["reality"],
                    float(abs(algebraic_signal.imag)),
                )
                cases += 1

print(
    json.dumps(
        {
            "nonidentity_signal_cases": cases,
            "system_qubits": [1, 2, 3],
            "reference_qubits": "every k from 0 through n",
            "errors": errors,
        },
        indent=2,
    )
)
assert max(errors.values()) < 1e-12
