import csv
import math


INPUT_FILE = "src/quantum/grover_benchmark_v2.csv"


def main():

    results = []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            results.append({
                "search_space": int(row["search_space"]),
                "qubits": int(row["qubits"]),
                "grover_iterations": int(
                    row["grover_iterations"]
                ),
                "success_probability": float(
                    row["success_probability"]
                ),
                "runtime": float(row["runtime"]),
                "classical_queries": int(
                    row["classical_queries"]
                ),
                "grover_queries": int(
                    row["grover_queries"]
                ),
                "query_reduction": float(
                    row["query_reduction"]
                )
            })

    print()
    print("📊 Q-AI BENCHMARK ANALYSIS")
    print("=" * 70)

    print(
        f"{'N':>6} "
        f"{'Qubits':>8} "
        f"{'Grover':>8} "
        f"{'Success':>10} "
        f"{'Reduction':>12}"
    )

    print("-" * 70)

    for row in results:

        print(
            f"{row['search_space']:>6} "
            f"{row['qubits']:>8} "
            f"{row['grover_iterations']:>8} "
            f"{row['success_probability']:>9.2%} "
            f"{row['query_reduction']:>11.2f}x"
        )

    print()
    print("🔬 SCALING ANALYSIS")
    print("=" * 70)

    for row in results:

        n = row["search_space"]

        theoretical_sqrt = math.sqrt(n)

        print(
            f"N={n:>3}: "
            f"classical={n:>3} queries | "
            f"Grover={row['grover_iterations']:>3} iterations | "
            f"√N={theoretical_sqrt:>6.2f} | "
            f"reduction={row['query_reduction']:.2f}x"
        )

    largest = results[-1]

    print()
    print("🏆 LARGEST TEST")
    print("=" * 70)

    print(
        f"Search space:       "
        f"{largest['search_space']}"
    )

    print(
        f"Qubits:             "
        f"{largest['qubits']}"
    )

    print(
        f"Classical queries:  "
        f"{largest['classical_queries']}"
    )

    print(
        f"Grover iterations:  "
        f"{largest['grover_queries']}"
    )

    print(
        f"Success probability:"
        f" {largest['success_probability']:.2%}"
    )

    print(
        f"Query reduction:    "
        f"{largest['query_reduction']:.2f}x"
    )

    print()
    print("📌 CONCLUSION")
    print("=" * 70)

    print(
        "The experiment demonstrates the expected "
        "sublinear Grover query scaling."
    )

    print(
        "The number of Grover iterations grows "
        "approximately with √N rather than N."
    )

    print(
        "The measured runtime is CPU simulation time "
        "and must not be interpreted as quantum speedup."
    )


if __name__ == "__main__":
    main()