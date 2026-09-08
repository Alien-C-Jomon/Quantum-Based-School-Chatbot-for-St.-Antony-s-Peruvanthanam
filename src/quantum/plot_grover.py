import csv
import matplotlib.pyplot as plt


INPUT_FILE = "src/quantum/grover_results.csv"


def load_results():
    rows = []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows


def create_plot():

    rows = load_results()

    states = [
        int(row["states"])
        for row in rows
    ]

    classical = [
        int(row["classical_worst_case"])
        for row in rows
    ]

    grover = [
        int(row["grover_iterations"])
        for row in rows
    ]

    plt.figure(figsize=(10, 6))

    plt.plot(
        states,
        classical,
        marker="o",
        label="Classical worst-case search"
    )

    plt.plot(
        states,
        grover,
        marker="o",
        label="Grover iterations"
    )

    plt.xscale("log", base=2)
    plt.yscale("log", base=2)

    plt.xlabel("Search space (N)")
    plt.ylabel("Operations / iterations")

    plt.title(
        "Q-AI: Classical Search vs Grover Search Scaling"
    )

    plt.legend()
    plt.grid(True, which="both")

    output_file = "src/quantum/grover_scaling.png"

    plt.savefig(
        output_file,
        dpi=200,
        bbox_inches="tight"
    )

    print("\n📈 Graph created successfully!")
    print("Saved to:")
    print(output_file)

    plt.show()


if __name__ == "__main__":
    create_plot()