from src.question_parser import parse_question


class QAEngine:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def answer(self, question):
        parsed = parse_question(question)
        question_lower = question.lower()

        # =========================================
        # PREVENT ANSWERS ABOUT OTHER INSTITUTIONS
        # =========================================

        college_name = "st antony's college"

        external_institutions = [
            "harvard",
            "oxford",
            "cambridge",
            "mit",
            "stanford",
            "iit",
            "aiims"
        ]

        if any(
            institution in question_lower
            for institution in external_institutions
        ):
            if college_name not in question_lower:
                return None

        # =========================================
        # COURSE QUESTIONS
        # =========================================

        course_data = self.kb.data.get("courses", {})
        courses = course_data.get("courses", [])

        course_keywords = [
            "course",
            "courses",
            "program",
            "programs",
            "programme",
            "programmes",
            "degree",
            "degrees"
        ]

        is_course_question = (
            parsed.get("intent") == "course"
            or any(
                keyword in question_lower
                for keyword in course_keywords
            )
        )

        if is_course_question and courses:

            # -----------------------------------------
            # Specific course search
            # -----------------------------------------

            course_name = parsed.get("course_name")

            if course_name:
                matches = [
                    course
                    for course in courses
                    if course_name.lower()
                    in course["name"].lower()
                ]

                if matches:
                    return matches

            # -----------------------------------------
            # UG / PG filtering
            # -----------------------------------------

            course_level = parsed.get("course_level")

            if course_level:
                matches = [
                    course
                    for course in courses
                    if course["level"].upper()
                    == course_level.upper()
                ]

                if matches:
                    return matches

            # -----------------------------------------
            # Department filtering
            # -----------------------------------------

            department = parsed.get("department")

            if department:
                matches = [
                    course
                    for course in courses
                    if course["department"].lower()
                    == department.lower()
                ]

                if matches:
                    return matches

            # -----------------------------------------
            # General course question
            # -----------------------------------------

            return courses

        # =========================================
        # FACULTY QUESTIONS
        # =========================================

        faculty_question = (
            parsed["intent"] == "faculty"
            or any(
                keyword in question_lower
                for keyword in [
                    "hod",
                    "head of department",
                    "head of the department",
                    "department head",
                    "who heads",
                    "who teaches",
                    "professor",
                    "faculty",
                    "lecturer",
                    "principal",
                    "vice principal"
                ]
            )
        )

        if faculty_question:

            faculty_data = self.kb.data.get(
                "faculty",
                {}
            )

            faculty = faculty_data.get(
                "faculty",
                []
            )

            # -----------------------------------------
            # Principal
            # -----------------------------------------

            if "principal" in question_lower:

                if "vice principal" not in question_lower:

                    matches = [
                        person
                        for person in faculty
                        if "principal"
                        in person["role"].lower()
                        and "vice principal"
                        not in person["role"].lower()
                    ]

                    if matches:
                        return matches

            # -----------------------------------------
            # Vice Principal
            # -----------------------------------------

            if "vice principal" in question_lower:

                matches = [
                    person
                    for person in faculty
                    if "vice principal"
                    in person["role"].lower()
                ]

                if matches:

                    hod_vp = [
                        person
                        for person in matches
                        if "hod"
                        in person["role"].lower()
                    ]

                    if hod_vp:
                        return hod_vp

                    return matches

            # -----------------------------------------
            # Department
            # -----------------------------------------

            department = parsed["department"]

            if "hotel management" in question_lower:
                department = "hotel management"

            if "msw" in question_lower:
                department = "social work"

            if department:

                if department == "social work":

                    matches = [
                        person
                        for person in faculty
                        if person["department"].lower()
                        in [
                            "social work",
                            "msw"
                        ]
                    ]

                else:

                    matches = [
                        person
                        for person in faculty
                        if person["department"].lower()
                        == department.lower()
                    ]

                # -----------------------------------------
                # HOD / Department Head
                # -----------------------------------------

                hod_keywords = [
                    "hod",
                    "head of department",
                    "head of the department",
                    "department head",
                    "who heads"
                ]

                if any(
                    keyword in question_lower
                    for keyword in hod_keywords
                ):

                    matches = [
                        person
                        for person in matches
                        if "hod"
                        in person["role"].lower()
                    ]

                if matches:
                    return matches

        # =========================================
        # ACHIEVEMENT QUESTIONS
        # =========================================

        if parsed["intent"] == "achievement":

            achievement_data = self.kb.data.get(
                "achievements",
                {}
            )

            achievements = achievement_data.get(
                "achievements",
                []
            )

            topic = parsed["achievement_topic"]

            person = parsed.get("person")

            if person is None:

                for item in achievements:

                    name = item.get(
                        "name",
                        ""
                    )

                    if (
                        name
                        and name.lower()
                        in question_lower
                    ):

                        person = name
                        break

            achievement_program_phrases = [
                "rank in",
                "rank holder",
                "topped",
                "first rank in",
                "secured first rank in"
            ]

            if (
                topic is None
                and person is None
                and any(
                    phrase in question_lower
                    for phrase in achievement_program_phrases
                )
            ):
                return None

            if topic:

                matches = [
                    item
                    for item in achievements
                    if topic.lower()
                    in item["program"].lower()
                ]

            else:

                matches = achievements

            if person:

                matches = [
                    item
                    for item in matches
                    if person.lower()
                    in item["name"].lower()
                ]

            if (
                "first rank" in question_lower
                or "1st rank" in question_lower
            ):

                matches = [
                    item
                    for item in matches
                    if "1st rank"
                    in item["achievement"].lower()
                ]

            elif (
                "topped" in question_lower
                or "topper" in question_lower
            ):

                matches = [
                    item
                    for item in matches
                    if "1st rank"
                    in item["achievement"].lower()
                ]

            elif "rank holder" in question_lower:

                matches = [
                    item
                    for item in matches
                    if "rank"
                    in item["achievement"].lower()
                ]

            if "outstanding" in question_lower:

                matches = [
                    item
                    for item in matches
                    if "outstanding performer"
                    in item["achievement"].lower()
                ]

            if matches:
                return matches

        # =========================================
        # COLLEGE INFORMATION
        # =========================================

        if parsed["intent"] == "college":

            college = self.kb.data.get(
                "college",
                {}
            )

            if (
                "established" in question_lower
                or "founded" in question_lower
            ):
                return {
                    "established":
                    college.get("established")
                }

            if "website" in question_lower:

                return {
                    "official_website":
                    college.get("official_website")
                }

            if (
                "contact" in question_lower
                or "phone" in question_lower
                or "telephone" in question_lower
            ):

                return college.get("contact")

            if (
                "accredited" in question_lower
                or "accreditation" in question_lower
                or "recognition" in question_lower
                or "recognitions" in question_lower
                or "recognized" in question_lower
                or "aicte" in question_lower
            ):

                return {
                    "recognitions":
                    college.get("recognitions")
                }

            if (
                "affiliated" in question_lower
                or "affiliation" in question_lower
                or (
                    "university" in question_lower
                    and "under" in question_lower
                )
            ):

                return {
                    "affiliated_to":
                    college.get("affiliated_to")
                }

        # =========================================
        # FALLBACK SEARCH
        # =========================================

        results = self.kb.search(question)

        if results:
            return results

        return None