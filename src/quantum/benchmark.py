import time
import json

from src.quantum.quantum_retrieval import QuantumRetrieval


def classical_rank(question, records, retrieval):
    candidates = []

    for record in records:
        similarity = retrieval.calculate_similarity(
            question,
            record
        )

        candidates.append({
            "record": record,
            "similarity": similarity
        })

    candidates.sort(
        key=lambda item: item["similarity"],
        reverse=True
    )

    return candidates


def run_benchmark():
    with open(
        "data/faculty.json",
        "r",
        encoding="utf-8"
    ) as file:
        records = json.load(file)["faculty"]

    question = "Who is the HOD of Computer Science?"

    retrieval = QuantumRetrieval()

    # Classical benchmark
    start = time.perf_counter()

    classical_results = classical_rank(
        question,
        records,
        retrieval
    )

    classical_time = time.perf_counter() - start

    # Quantum benchmark
    start = time.perf_counter()

    quantum_results = retrieval.rank_records(
        question,
        records
    )

    quantum_time = time.perf_counter() - start

    print("\n⚛️ Q-AI Quantum Benchmark")
    print("=" * 40)

    print(f"Classical time: {classical_time:.6f} seconds")
    print(f"Quantum time:   {quantum_time:.6f} seconds")

    print("\n🏆 Classical winner:")
    print(
        classical_results[0]["record"]["name"],
        "| similarity:",
        classical_results[0]["similarity"]
    )

    print("\n⚛️ Quantum winner:")
    print(
        quantum_results[0]["candidate"]["record"]["name"],
        "| quantum score:",
        quantum_results[0]["quantum_score"]
    )


if __name__ == "__main__":
    run_benchmark()