from src.knowledge_base import KnowledgeBase
from src.qa_engine import QAEngine


# --------------------------------------------------
# LOAD Q-AI
# --------------------------------------------------

kb = KnowledgeBase([
    "data/college.json",
    "data/faculty.json",
    "data/achievements.json"
])

qa = QAEngine(kb)


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------

tests = [

    # ==============================================
    # COLLEGE INFORMATION
    # ==============================================

    (
        "When was the college established?",
        "2013"
    ),

    (
        "When was St Antony's College founded?",
        "2013"
    ),

    (
        "Which university is the college affiliated to?",
        "Mahatma Gandhi University"
    ),

    (
        "What university is St Antony's College under?",
        "Mahatma Gandhi University"
    ),

    (
        "Is the college NAAC accredited?",
        "NAAC"
    ),

    (
        "What are the college recognitions?",
        "AICTE"
    ),

    (
        "Is the college AICTE approved?",
        "AICTE"
    ),

    (
        "What is the official website?",
        "stantonyscollegepeerumade.ac.in"
    ),


    # ==============================================
    # FACULTY / HOD
    # ==============================================

    (
        "Who is the HOD of Computer Science?",
        "Jintumol John"
    ),

    (
        "Who heads Computer Science?",
        "Jintumol John"
    ),

    (
        "Who heads CS?",
        "Jintumol John"
    ),

    (
        "Who is the Computer Science department head?",
        "Jintumol John"
    ),

    (
        "Who is the HOD of Mathematics?",
        "Suparna Raju"
    ),

    (
        "Who heads Malayalam?",
        "Anurag P"
    ),

    (
        "Who is the HOD of Fashion Technology?",
        "Christy Jose"
    ),

    (
        "Who is the HOD of Hotel Management?",
        "Tomy Joseph"
    ),

    (
        "Who is the HOD of MSW?",
        "Jismi Shaju"
    ),

    (
        "Who teaches Mathematics?",
        "Manju S Nair"
    ),

    (
        "Who teaches Computer Science?",
        "Praicy Antony"
    ),

    (
        "Who is the Principal?",
        "Antony Joseph"
    ),

    (
        "Who is the Vice Principal of the college?",
        "Suparna Raju"
    ),


    # ==============================================
    # ACHIEVEMENTS
    # ==============================================

    (
        "Who got first rank in Cyber Forensic?",
        "Liya Rojo"
    ),

    (
        "Who secured first rank in B.Sc. Cyber Forensic?",
        "Liya Rojo"
    ),

    (
        "Who topped Cyber Forensic?",
        "Liya Rojo"
    ),

    (
        "Who got first rank in Fashion Technology?",
        "Narmadha E R"
    ),

    (
        "Who secured first rank in Bachelor of Fashion Technology?",
        "Narmadha E R"
    ),

    (
        "Who is an All India CMA Rank Holder?",
        "Anagly C R"
    ),

    (
        "Who cleared CMA Final Group 4?",
        "Muhammad Sajid"
    ),

    (
        "Who cleared CMA Intermediate?",
        "Aneesha Mary"
    ),

    (
        "Who cleared Intermediate Group 2 in CMA?",
        "Aiswarya M"
    ),

    (
        "Who cleared Intermediate Group 1 in CMA?",
        "Vyshnav E S"
    ),

    (
        "Who are the outstanding performers?",
        "Poorna Raju"
    ),

    (
        "Is Kesiya M M a rank holder?",
        "Kesiya M M"
    ),


    # ==============================================
    # UNKNOWN / ANTI-HALLUCINATION
    # ==============================================

    (
        "Who is the HOD of Physics?",
        None
    ),

    (
        "Who is the HOD of Aerospace Engineering?",
        None
    ),

    (
        "Who is the quantum computing professor?",
        None
    ),

    (
        "Who teaches Mechanical Engineering?",
        None
    ),

    (
        "Who got first rank in Biotechnology?",
        None
    ),

    (
        "Who is the HOD of Medicine?",
        None
    ),

    (
        "Who is the principal of Harvard University?",
        None
    ),

    (
        "Who won the 2025 Nobel Prize at this college?",
        None
    )
]


# --------------------------------------------------
# RUN TESTS
# --------------------------------------------------

passed = 0
failed = 0

print()
print("=" * 60)
print("🧪 Q-AI EXTENDED KNOWLEDGE TEST")
print("=" * 60)
print()


for number, (question, expected) in enumerate(tests, start=1):

    try:

        result = qa.answer(question)

        # Convert result into searchable text
        result_text = str(result)

        if expected is None:

            success = result is None

        else:

            success = (
                expected.lower()
                in result_text.lower()
            )


        if success:

            print(
                f"{number:02d}. ✅ PASS | {question}"
            )

            passed += 1

        else:

            print(
                f"{number:02d}. ❌ FAIL | {question}"
            )

            print(
                f"     Expected: {expected}"
            )

            print(
                f"     Got:      {result}"
            )

            failed += 1


    except Exception as error:

        print(
            f"{number:02d}. ❌ ERROR | {question}"
        )

        print(
            f"     {error}"
        )

        failed += 1


# --------------------------------------------------
# RESULTS
# --------------------------------------------------

print()
print("=" * 60)
print("📊 EXTENDED TEST RESULTS")
print("=" * 60)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total:  {len(tests)}")

print()

if failed == 0:

    print("🎉 ALL EXTENDED TESTS PASSED!")
    print("🧠 Q-AI KNOWLEDGE SYSTEM: VERIFIED")

else:

    print("⚠️ SOME TESTS FAILED.")
    print("🔧 We will improve the question parser next.")

print("=" * 60)