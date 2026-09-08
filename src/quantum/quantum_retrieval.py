from src.quantum.quantum_ranker import QuantumRanker
from src.question_parser import parse_question


class QuantumRetrieval:
    def __init__(self):
        self.ranker = QuantumRanker()

    def calculate_similarity(self, question, record):
        parsed = parse_question(question)

        score = 0.0
        total_weight = 0.0

        # Faculty-specific scoring
        if parsed["intent"] == "faculty":

            # Department match
            if parsed["department"]:
                total_weight += 0.6

                if (
                    record.get("department", "").lower()
                    == parsed["department"].lower()
                ):
                    score += 0.6

            # HOD match
            if "hod" in question.lower() or "head of department" in question.lower():
                total_weight += 0.4

                if "hod" in record.get("role", "").lower():
                    score += 0.4

        # Achievement-specific scoring
        elif parsed["intent"] == "achievement":

            if parsed["achievement_topic"]:
                total_weight += 0.7

                if parsed["achievement_topic"].lower() in record.get(
                    "program", ""
                ).lower():
                    score += 0.7

            # First-rank match
            if "first rank" in question.lower() or "1st rank" in question.lower():
                total_weight += 0.3

                if "1st rank" in record.get(
                    "achievement", ""
                ).lower():
                    score += 0.3

        if total_weight == 0:
            return 0.0

        return score / total_weight

    def rank_records(self, question, records):
        candidates = []

        for record in records:
            similarity = self.calculate_similarity(
                question,
                record
            )

            candidates.append({
                "record": record,
                "similarity": similarity
            })

        ranked = self.ranker.rank(candidates)

        return ranked