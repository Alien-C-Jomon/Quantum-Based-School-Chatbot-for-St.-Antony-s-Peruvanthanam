from src.knowledge_base import KnowledgeBase
from src.qa_engine import QAEngine
from src.response_generator import generate_response

kb = KnowledgeBase([
    "data/college.json",
    "data/faculty.json",
    "data/achievements.json"
])

qa = QAEngine(kb)

print("🧠 Q-AI")
print("=" * 30)

question = input("Ask Q-AI something: ")

answer = qa.answer(question)

print("\n🤖 Q-AI Answer:\n")

print(generate_response(question, answer))