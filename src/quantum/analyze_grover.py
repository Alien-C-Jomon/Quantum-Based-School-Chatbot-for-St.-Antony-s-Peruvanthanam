import csv
import math


INPUT_FILE = "src/quantum/grover_results.csv"


def analyze():

    rows = []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    print("\n📊 Q-AI Grover Analysis")
    print("=" * 70)

    print(
        f"{'States':<10}"
        f"{'Classical':<12}"
        f"{'Grover':<10}"
        f"{'Reduction':<12}"
        f"{'Success'}"
    )

    print("-" * 70)

    for row in rows:

        states = int(row["states"])
        classical = int(row["classical_worst_case"])
        grover = int(row["grover_iterations"])
        success = float(row["success_probability"])

        reduction = classical / grover

        print(
            f"{states:<10}"
            f"{classical:<12}"
            f"{grover:<10}"
            f"{reduction:<12.2f}x"
            f"{success:.2%}"
        )

    print("\n🧠 Interpretation")
    print("-" * 70)

    largest = rows[-1]

    states = int(largest["states"])
    classical = int(largest["classical_worst_case"])
    grover = int(largest["grover_iterations"])

    reduction = classical / grover

    print(
        f"For {states} possible states:"
    )

    print(
        f"• Classical worst-case search: {classical} queries"
    )

    print(
        f"• Grover iterations: {grover}"
    )

    print(
        f"• Query-count reduction: {reduction:.2f}x"
    )

    print(
        "\n⚠️ This is a theoretical/query-complexity comparison."
    )

    print(
        "It does NOT mean the CPU simulator is "
        f"{reduction:.2f}x faster."
    )

    print(
        "\nThe quantum circuit was simulated on a "
        "classical CPU using Qiskit Aer."
    )


if __name__ == "__main__":
    analyze()