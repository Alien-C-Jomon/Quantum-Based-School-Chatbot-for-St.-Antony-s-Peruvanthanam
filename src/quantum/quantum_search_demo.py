import math
import json

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


SHOTS = 1024


def grover_search(num_items, target_index):
    """
    Demonstrate Grover search over a power-of-two search space.
    """

    n = math.ceil(math.log2(num_items))
    search_space = 2 ** n

    circuit = QuantumCircuit(n, n)

    # Create equal superposition
    circuit.h(range(n))

    # Number of Grover iterations
    iterations = max(
        1,
        round((math.pi / 4) * math.sqrt(search_space))
    )

    # Encode target index as a binary string
    target = format(target_index, f"0{n}b")

    for _ in range(iterations):

        # Oracle
        for qubit, bit in enumerate(reversed(target)):
            if bit == "0":
                circuit.x(qubit)

        if n == 1:
            circuit.z(0)
        else:
            circuit.h(n - 1)
            circuit.mcx(list(range(n - 1)), n - 1)
            circuit.h(n - 1)

        for qubit, bit in enumerate(reversed(target)):
            if bit == "0":
                circuit.x(qubit)

        # Diffuser
        circuit.h(range(n))
        circuit.x(range(n))

        if n == 1:
            circuit.z(0)
        else:
            circuit.h(n - 1)
            circuit.mcx(list(range(n - 1)), n - 1)
            circuit.h(n - 1)

        circuit.x(range(n))
        circuit.h(range(n))

    circuit.measure(range(n), range(n))

    simulator = AerSimulator()

    result = simulator.run(
        circuit,
        shots=SHOTS
    ).result()

    counts = result.get_counts()

    measured_state = max(
        counts,
        key=counts.get
    )

    measured_index = int(measured_state, 2)

    return (
        n,
        search_space,
        iterations,
        measured_index,
        counts
    )


def run_demo():

    with open(
        "data/faculty.json",
        "r",
        encoding="utf-8"
    ) as file:
        faculty = json.load(file)["faculty"]

    # Find Jintumol John
    target_name = "Mrs. Jintumol John"

    target_index = next(
        i
        for i, person in enumerate(faculty)
        if person["name"] == target_name
    )

    num_items = len(faculty)

    n, search_space, iterations, measured_index, counts = (
        grover_search(
            num_items,
            target_index
        )
    )

    print("\n⚛️ Q-AI Quantum Faculty Search")
    print("=" * 55)

    print(f"Faculty records:       {num_items}")
    print(f"Quantum search space:  {search_space}")
    print(f"Target:                {target_name}")
    print(f"Target index:          {target_index}")
    print(f"Qubits required:       {n}")
    print(f"Grover iterations:     {iterations}")

    print("\n🔎 Classical search:")
    print(
        f"Worst case: {num_items} candidate checks"
    )

    print("\n⚛️ Grover search:")
    print(
        f"Approx. √N scaling: {math.sqrt(search_space):.2f}"
    )

    print(
        f"Measured index:       {measured_index}"
    )

    if measured_index == target_index:
        print(
            "\n✅ Grover successfully identified "
            "the target candidate."
        )
    else:
        print(
            "\n⚠️ Measurement did not identify "
            "the target on this run."
        )

    print(
        "\n📌 Important:"
    )
    print(
        "This experiment demonstrates quantum "
        "query-complexity scaling."
    )
    print(
        "The circuit is simulated on a classical CPU "
        "using Qiskit Aer."
    )


if __name__ == "__main__":
    run_demo()