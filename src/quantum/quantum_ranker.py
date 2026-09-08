from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math


class QuantumRanker:
    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()

    def similarity_to_angle(self, similarity):
        similarity = max(0.0, min(1.0, similarity))
        return similarity * math.pi

    def score(self, similarity):
        angle = self.similarity_to_angle(similarity)

        circuit = QuantumCircuit(1, 1)

        # Encode similarity into the qubit
        circuit.ry(angle, 0)

        circuit.measure(0, 0)

        result = self.simulator.run(
            circuit,
            shots=self.shots
        ).result()

        counts = result.get_counts()

        zero_count = counts.get("0", 0)

        return 1 - (zero_count / self.shots)

    def rank(self, candidates):
        ranked = []

        for candidate in candidates:
            similarity = candidate.get("similarity", 0.0)

            quantum_score = self.score(similarity)

            ranked.append({
                "candidate": candidate,
                "quantum_score": quantum_score
            })

        ranked.sort(
            key=lambda item: item["quantum_score"],
            reverse=True
        )

        return ranked