import math

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


SHOTS = 1024


def run_quantum_search(target_index, num_items):
    """
    Run an experimental Grover search.

    The search is performed over a power-of-two
    quantum search space and simulated locally
    using Qiskit Aer on the CPU.
    """

    # -----------------------------------------
    # Determine quantum search space
    # -----------------------------------------

    n = math.ceil(math.log2(num_items))
    search_space = 2 ** n


    # -----------------------------------------
    # Build quantum circuit
    # -----------------------------------------

    circuit = QuantumCircuit(n, n)

    # Equal superposition
    circuit.h(range(n))


    # -----------------------------------------
    # Grover iteration count
    # -----------------------------------------

    iterations = max(
        1,
        round(
            (math.pi / 4)
            * math.sqrt(search_space)
        )
    )


    target = format(
        target_index,
        f"0{n}b"
    )


    # -----------------------------------------
    # Grover algorithm
    # -----------------------------------------

    for _ in range(iterations):

        # Oracle
        for qubit, bit in enumerate(
            reversed(target)
        ):
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


        for qubit, bit in enumerate(
            reversed(target)
        ):
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


    # -----------------------------------------
    # Measurement
    # -----------------------------------------

    circuit.measure(
        range(n),
        range(n)
    )


    # -----------------------------------------
    # Run simulator
    # -----------------------------------------

    simulator = AerSimulator()

    result = simulator.run(
        circuit,
        shots=SHOTS
    ).result()


    counts = result.get_counts()


    # Most frequently measured state
    measured_state = max(
        counts,
        key=counts.get
    )


    measured_index = int(
        measured_state,
        2
    )


    # -----------------------------------------
    # Success probability
    # -----------------------------------------

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


    # -----------------------------------------
    # Query-complexity comparison
    # -----------------------------------------

    classical_worst_case = num_items

    grover_query_count = iterations

    query_reduction = (
        classical_worst_case
        / grover_query_count
    )


    # -----------------------------------------
    # Return experiment data
    # -----------------------------------------

    return {

        "search_space": search_space,

        "qubits": n,

        "grover_iterations": iterations,

        "target_index": target_index,

        "measured_index": measured_index,

        "success": measured_index == target_index,

        "success_probability": success_probability,

        "shots": SHOTS,

        "classical_worst_case": classical_worst_case,

        "grover_query_count": grover_query_count,

        "query_reduction_factor": query_reduction,

        "backend": "Qiskit Aer",

        "mode": "CPU simulation"
    }