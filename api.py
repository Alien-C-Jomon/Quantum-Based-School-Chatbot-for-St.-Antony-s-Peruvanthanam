from flask import Flask, request, jsonify
from flask_cors import CORS

from src.knowledge_base import KnowledgeBase
from src.qa_engine import QAEngine
from src.response_generator import generate_response
from src.quantum.api_quantum import run_quantum_search


app = Flask(__name__)
CORS(app)


# Load Q-AI's verified knowledge base
kb = KnowledgeBase([
    "data/college.json",
    "data/faculty.json",
    "data/achievements.json",
    "data/courses.json"
])

qa = QAEngine(kb)


def get_quantum_result(question, answer):
    """
    Run the experimental Grover search when Q-AI
    has identified a specific faculty candidate.

    The classical QA result remains the source of truth.
    """

    if not isinstance(answer, list) or len(answer) != 1:
        return None

    candidate = answer[0]

    if "name" not in candidate or "role" not in candidate:
        return None

    question_lower = question.lower()

    if not any(
        keyword in question_lower
        for keyword in [
            "faculty",
            "hod",
            "head of department",
            "head of the department",
            "department head",
            "who heads"
        ]
    ):
        return None

    faculty = kb.data.get(
        "faculty",
        {}
    ).get(
        "faculty",
        []
    )

    target_name = candidate["name"]

    try:
        target_index = next(
            i
            for i, person in enumerate(faculty)
            if person["name"] == target_name
        )
    except StopIteration:
        return None

    return run_quantum_search(
        target_index,
        len(faculty)
    )


@app.route("/api/ask", methods=["POST"])
def ask():

    data = request.get_json(silent=True) or {}

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "success": False,
            "error": "Please enter a question."
        }), 400

    answer = qa.answer(question)

    response = generate_response(
        question,
        answer
    )

    quantum = get_quantum_result(
        question,
        answer
    )

    return jsonify({
        "success": True,
        "question": question,
        "answer": response,
        "quantum": quantum
    })


@app.route("/api/status", methods=["GET"])
def status():

    return jsonify({
        "status": "online",
        "system": "Q-AI",
        "knowledge_base": "verified local data",
        "quantum_backend": "Qiskit Aer",
        "quantum_mode": "CPU simulation"
    })


if __name__ == "__main__":

    print()
    print("⚛️ Q-AI LOCAL API")
    print("=" * 40)
    print("Knowledge Base: READY")
    print("QA Engine:      READY")
    print("Quantum:        Qiskit Aer")
    print()
    print("🌐 API running at:")
    print("http://127.0.0.1:5000")
    print()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )