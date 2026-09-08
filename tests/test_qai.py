from src.knowledge_base import KnowledgeBase
from src.qa_engine import QAEngine
from src.response_generator import generate_response


kb = KnowledgeBase([
    "data/college.json",
    "data/faculty.json",
    "data/achievements.json"
])

qa = QAEngine(kb)


tests = [
    {
        "question": "Who is the HOD of Computer Science?",
        "expected": "Mrs. Jintumol John"
    },
    {
        "question": "Who heads CS?",
        "expected": "Mrs. Jintumol John"
    },
    {
        "question": "Who teaches maths?",
        "expected": "Mrs. Manju S Nair"
    },
    {
        "question": "Who got first rank in Cyber Forensic?",
        "expected": "Liya Rojo"
    },
    {
        "question": "When was the college established?",
        "expected": "2013"
    },
    {
        "question": "What is the official website?",
        "expected": "stantonyscollegepeerumade.ac.in"
    },
    {
        "question": "What is the college affiliated to?",
        "expected": "Mahatma Gandhi University"
    },
    {
        "question": "What are the college recognitions?",
        "expected": "NAAC"
    },
    {
        "question": "Who is the HOD of Physics?",
        "expected": None
    },
    {
        "question": "Who is the HOD of Aerospace Engineering?",
        "expected": None
    },
    {
        "question": "What is the quantum computer professor?",
        "expected": None
    }
]


print()
print("🧪 Q-AI FULL TEST SUITE")
print("=" * 60)

passed = 0
failed = 0


for number, test in enumerate(tests, start=1):

    question = test["question"]
    expected = test["expected"]

    answer = qa.answer(question)

    response = generate_response(
        question,
        answer
    )

    if expected is None:

        success = answer is None

    else:

        success = (
            expected.lower()
            in response.lower()
        )

    if success:
        status = "✅ PASS"
        passed += 1

    else:
        status = "❌ FAIL"
        failed += 1

    print()
    print(f"{number}. {status}")
    print(f"Question: {question}")
    print(f"Expected: {expected}")
    print(f"Answer:   {response}")


print()
print("=" * 60)
print("📊 TEST RESULTS")
print("=" * 60)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total:  {len(tests)}")

if failed == 0:
    print()
    print("🎉 ALL TESTS PASSED!")
else:
    print()
    print("⚠️ Some tests need attention.")