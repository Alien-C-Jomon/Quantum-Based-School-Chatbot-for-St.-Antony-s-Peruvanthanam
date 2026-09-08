import math
import time
import csv

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


SHOTS = 1024


def grover_search(search_space, target_index):
    """
    Run a Grover search over a power-of-two search space.
    The circuit is simulated locally using Qiskit Aer.
    """

    n = int(math.log2(search_space))

    circuit = QuantumCircuit(n, n)

    # Create equal superposition
    circuit.h(range(n))

        # Optimal Grover iteration count for one marked state
    iterations = max(
        1,
        math.floor(
            (math.pi / 4) * math.sqrt(search_space)
        )
    )

    target = format(
        target_index,
        f"0{n}b"
    )

    for _ in range(iterations):

        # Oracle
        for qubit, bit in enumerate(reversed(target)):
            if bit == "0":
                circuit.x(qubit)

        if n == 1:
            circuit.z(0)
        else:
            circuit.h(n - 1)
            circuit.mcx(
                list(range(n - 1)),
                n - 1
            )
            circuit.h(n - 1)

        for qubit, bit in enumerate(reversed(target)):
            if bit == "0":
                circuit.x(qubit)

        # Diffusion operator
        circuit.h(range(n))
        circuit.x(range(n))

        if n == 1:
            circuit.z(0)
        else:
            circuit.h(n - 1)
            circuit.mcx(
                list(range(n - 1)),
                n - 1
            )
            circuit.h(n - 1)

        circuit.x(range(n))
        circuit.h(range(n))

    # Measurement
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

    target_state = format(
        target_index,
        f"0{n}b"
    )

    target_count = counts.get(
        target_state,
        0
    )

    success_probability = (
        target_count / SHOTS
    )

    measured_state = max(
        counts,
        key=counts.get
    )

    measured_index = int(
        measured_state,
        2
    )

    return {
        "search_space": search_space,
        "qubits": n,
        "grover_iterations": iterations,
        "success_probability": success_probability,
        "measured_index": measured_index,
        "target_index": target_index,
        "runtime": runtime
    }


def run_benchmark():

    search_spaces = [
        4,
        8,
        16,
        32,
        64,
        128,
        256
    ]

    results = []

    print()
    print("⚛️ Q-AI QUANTUM SCALING BENCHMARK")
    print("=" * 60)

    for search_space in search_spaces:

        # Pick the middle-ish target
        target_index = search_space // 2

        result = grover_search(
            search_space,
            target_index
        )

        classical_queries = search_space
        grover_queries = result["grover_iterations"]

        query_reduction = (
            classical_queries
            / grover_queries
        )

        result["classical_queries"] = classical_queries
        result["grover_queries"] = grover_queries
        result["query_reduction"] = query_reduction

        results.append(result)

        print()
        print(f"N = {search_space}")
        print(f"Qubits:                 {result['qubits']}")
        print(f"Grover iterations:      {result['grover_iterations']}")
        print(
            f"Success probability:    "
            f"{result['success_probability']:.2%}"
        )
        print(
            f"Simulator runtime:      "
            f"{result['runtime']:.6f} seconds"
        )
        print(
            f"Classical queries:      "
            f"{classical_queries}"
        )
        print(
            f"Grover queries:         "
            f"{grover_queries}"
        )
        print(
            f"Query reduction:        "
            f"{query_reduction:.2f}x"
        )

    # Save results
    output_file = "src/quantum/grover_benchmark_v2.csv"

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "search_space",
                "qubits",
                "grover_iterations",
                "success_probability",
                "measured_index",
                "target_index",
                "runtime",
                "classical_queries",
                "grover_queries",
                "query_reduction"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print()
    print("=" * 60)
    print("✅ Benchmark complete!")
    print()
    print(f"📄 Results saved to:")
    print(output_file)

    print()
    print("📌 Scientific note:")
    print(
        "This benchmark compares quantum query scaling "
        "with classical worst-case search."
    )
    print(
        "The quantum circuit is simulated on a classical CPU "
        "using Qiskit Aer."
    )
    print(
        "Therefore, simulator runtime is NOT a demonstration "
        "of quantum speedup."
    )


if __name__ == "__main__":
    run_benchmark()