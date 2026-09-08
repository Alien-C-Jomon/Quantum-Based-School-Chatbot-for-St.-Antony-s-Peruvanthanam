from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def grover_2_qubit():
    circuit = QuantumCircuit(2, 2)

    # Superposition
    circuit.h(0)
    circuit.h(1)

    # Oracle: mark |11>
    circuit.cz(0, 1)

    # Diffuser
    circuit.h(0)
    circuit.h(1)

    circuit.x(0)
    circuit.x(1)

    circuit.cz(0, 1)

    circuit.x(0)
    circuit.x(1)

    circuit.h(0)
    circuit.h(1)

    # Measurement
    circuit.measure(0, 0)
    circuit.measure(1, 1)

    return circuit


def run_grover():
    simulator = AerSimulator()

    circuit = grover_2_qubit()

    result = simulator.run(
        circuit,
        shots=1024
    ).result()

    counts = result.get_counts()

    print("\n⚛️ Q-AI Grover Search")
    print("=" * 40)

    print("Target state: 11")
    print("Measurement results:")

    for state, count in sorted(counts.items()):
        probability = count / 1024

        print(
            f"{state}: "
            f"{count} shots "
            f"({probability:.2%})"
        )


if __name__ == "__main__":
    run_grover()