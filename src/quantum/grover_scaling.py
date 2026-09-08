import csv
import math
import time

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


SHOTS = 1024


def create_oracle(n):
    """Oracle that marks |111...111>."""
    circuit = QuantumCircuit(n)

    circuit.h(n - 1)

    if n == 1:
        circuit.z(0)
    else:
        circuit.mcx(list(range(n - 1)), n - 1)

    circuit.h(n - 1)

    return circuit


def create_diffuser(n):
    """Standard Grover diffusion operator."""
    circuit = QuantumCircuit(n)

    circuit.h(range(n))
    circuit.x(range(n))

    circuit.h(n - 1)

    if n == 1:
        circuit.z(0)
    else:
        circuit.mcx(list(range(n - 1)), n - 1)

    circuit.h(n - 1)

    circuit.x(range(n))
    circuit.h(range(n))

    return circuit


def grover_search(n):
    """Run Grover search for n qubits."""

    circuit = QuantumCircuit(n, n)

    # Initial superposition
    circuit.h(range(n))

    states = 2 ** n

    # Theoretical near-optimal number of iterations
    iterations = max(
        1,
        math.floor((math.pi / 4) * math.sqrt(states))
    )

    for _ in range(iterations):

        oracle = create_oracle(n)
        diffuser = create_diffuser(n)

        circuit.compose(
            oracle,
            inplace=True
        )

        circuit.compose(
            diffuser,
            inplace=True
        )

    circuit.measure(
        range(n),
        range(n)
    )

    simulator = AerSimulator()

    start = time.perf_counter()

    result = simulator.run(
        circuit,
        shots=SHOTS
    ).result()

    runtime = time.perf_counter() - start

    counts = result.get_counts()

    target = "1" * n

    target_count = counts.get(target, 0)

    probability = target_count / SHOTS

    return iterations, probability, runtime


def run_scaling_experiment():

    results = []

    print("\n⚛️ Q-AI Grover Scaling Experiment")
    print("=" * 75)

    print(
        f"{'Qubits':<8}"
        f"{'States':<10}"
        f"{'Classical':<12}"
        f"{'Grover':<10}"
        f"{'Success':<12}"
        f"{'Runtime'}"
    )

    print("-" * 75)

    for n in range(2, 11):

        states = 2 ** n

        iterations, probability, runtime = grover_search(n)

        classical_operations = states

        theoretical_grover = (math.pi / 4) * math.sqrt(states)

        print(
            f"{n:<8}"
            f"{states:<10}"
            f"{classical_operations:<12}"
            f"{iterations:<10}"
            f"{probability:<12.2%}"
            f"{runtime:.6f}s"
        )

        results.append({
            "qubits": n,
            "states": states,
            "classical_worst_case": classical_operations,
            "grover_iterations": iterations,
            "theoretical_grover": theoretical_grover,
            "success_probability": probability,
            "simulation_runtime_seconds": runtime
        })

    # Save results
    output_file = "src/quantum/grover_results.csv"

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    print("\n📊 Results saved to:")
    print(output_file)


if __name__ == "__main__":
    run_scaling_experiment()