import csv
import matplotlib.pyplot as plt


INPUT_FILE = "src/quantum/grover_benchmark_v2.csv"


def load_results():
    results = []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            results.append({
                "N": int(row["search_space"]),
                "grover": int(row["grover_iterations"]),
                "success": float(
                    row["success_probability"]
                ),
                "classical": int(
                    row["classical_queries"]
                )
            })

    return results


def plot_query_scaling(results):

    n_values = [
        row["N"]
        for row in results
    ]

    classical = [
        row["classical"]
        for row in results
    ]

    grover = [
        row["grover"]
        for row in results
    ]

    plt.figure(figsize=(9, 6))

    plt.plot(
        n_values,
        classical,
        marker="o",
        label="Classical worst-case"
    )

    plt.plot(
        n_values,
        grover,
        marker="o",
        label="Grover iterations"
    )

    plt.xscale("log", base=2)
    plt.yscale("log", base=2)

    plt.xlabel("Search Space (N)")
    plt.ylabel("Query Count / Iterations")

    plt.title(
        "Q-AI: Classical vs Grover Query Scaling"
    )

    plt.grid(True, which="both")
    plt.legend()

    plt.tight_layout()

    output = "python/quantum/grover_query_scaling.png"

    plt.savefig(
        output,
        dpi=200
    )

    print(f"✅ Saved: {output}")

    plt.show()


def plot_success_probability(results):

    n_values = [
        row["N"]
        for row in results
    ]

    success = [
        row["success"] * 100
        for row in results
    ]

    plt.figure(figsize=(9, 6))

    plt.plot(
        n_values,
        success,
        marker="o"
    )

    plt.xscale("log", base=2)

    plt.xlabel("Search Space (N)")
    plt.ylabel("Measured Success Probability (%)")

    plt.title(
        "Q-AI: Grover Search Success Probability"
    )

    plt.ylim(
        0,
        105
    )

    plt.grid(True, which="both")

    plt.tight_layout()

    output = "python/quantum/grover_success_probability.png"

    plt.savefig(
        output,
        dpi=200
    )

    print(f"✅ Saved: {output}")

    plt.show()


def main():

    print()
    print("📈 Q-AI BENCHMARK VISUALIZATION")
    print("=" * 50)

    results = load_results()

    print(
        f"Loaded {len(results)} benchmark results."
    )

    plot_query_scaling(results)

    plot_success_probability(results)

    print()
    print("🎉 Visualization complete!")


if __name__ == "__main__":
    main()