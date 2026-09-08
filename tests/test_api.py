import requests


API_URL = "http://127.0.0.1:5000"


tests = [
    {
        "question": "Who is the HOD of Computer Science?",
        "expected_answer": "Mrs. Jintumol John",
        "expect_quantum": True
    },
    {
        "question": "Who heads CS?",
        "expected_answer": "Mrs. Jintumol John",
        "expect_quantum": True
    },
    {
        "question": "Who teaches maths?",
        "expected_answer": "Mrs. Manju S Nair",
        "expect_quantum": False
    },
    {
        "question": "Who got first rank in Cyber Forensic?",
        "expected_answer": "Liya Rojo",
        "expect_quantum": False
    },
    {
        "question": "What are the college recognitions?",
        "expected_answer": "NAAC",
        "expect_quantum": False
    },
    {
        "question": "Who is the HOD of Physics?",
        "expected_answer": "couldn't find verified information",
        "expect_quantum": False
    }
]


print()
print("🌐 Q-AI API + QUANTUM INTEGRATION TEST")
print("=" * 60)

passed = 0
failed = 0


# --------------------------------------------------
# API STATUS TEST
# --------------------------------------------------

try:

    response = requests.get(
        f"{API_URL}/api/status",
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        print()
        print("1. ✅ API STATUS PASS")
        print("Status:", data.get("status"))
        print("System:", data.get("system"))
        print("Quantum:", data.get("quantum_backend"))

        passed += 1

    else:

        print()
        print("1. ❌ API STATUS FAIL")
        print("HTTP:", response.status_code)

        failed += 1

except Exception as error:

    print()
    print("1. ❌ API STATUS FAIL")
    print("Error:", error)

    failed += 1


# --------------------------------------------------
# QUESTION TESTS
# --------------------------------------------------

for number, test in enumerate(tests, start=2):

    question = test["question"]

    try:

        response = requests.post(
            f"{API_URL}/api/ask",
            json={
                "question": question
            },
            timeout=30
        )

        data = response.json()

        answer = data.get(
            "answer",
            ""
        )

        quantum = data.get(
            "quantum"
        )

        answer_ok = (
            test["expected_answer"].lower()
            in answer.lower()
        )

        quantum_ok = (
            quantum is not None
            if test["expect_quantum"]
            else quantum is None
        )

        success = (
            response.status_code == 200
            and data.get("success") is True
            and answer_ok
            and quantum_ok
        )

        if success:

            print()
            print(f"{number}. ✅ PASS")
            print(f"Question: {question}")

            if quantum:

                print(
                    "Quantum:  "
                    f"{quantum['qubits']} qubits | "
                    f"{quantum['grover_iterations']} Grover iterations | "
                    f"{quantum['success_probability']:.2%} success"
                )

            else:

                print("Quantum:  Not required")

            passed += 1

        else:

            print()
            print(f"{number}. ❌ FAIL")
            print(f"Question: {question}")
            print("Answer:", answer)
            print("Quantum:", quantum)

            failed += 1

    except Exception as error:

        print()
        print(f"{number}. ❌ FAIL")
        print(f"Question: {question}")
        print("Error:", error)

        failed += 1


# --------------------------------------------------
# RESULTS
# --------------------------------------------------

print()
print("=" * 60)
print("📊 API INTEGRATION RESULTS")
print("=" * 60)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total:  {passed + failed}")

if failed == 0:

    print()
    print("🎉 ALL API INTEGRATION TESTS PASSED!")
    print("⚛️ Q-AI backend + quantum pipeline is working.")

else:

    print()
    print("⚠️ Some API integration tests need attention.")