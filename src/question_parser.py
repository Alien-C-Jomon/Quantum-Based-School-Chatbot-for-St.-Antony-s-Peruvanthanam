import re


def parse_question(question):
    text = question.lower().strip()

    result = {
        "intent": "unknown",
        "department": None,
        "achievement_topic": None,
        "person": None,
        "course_level": None,
        "course_name": None
    }

    # -----------------------------------------
    # Department aliases
    # -----------------------------------------

    department_aliases = {
        "computer science": [
            "computer science",
            "computer sci",
            "cs department",
            "cs"
        ],
        "commerce": [
            "commerce",
            "commerce department"
        ],
        "mathematics": [
            "mathematics",
            "maths",
            "math"
        ],
        "physics": [
            "physics",
            "physics department"
        ],
        "chemistry": [
            "chemistry",
            "chemistry department"
        ],
        "english": [
            "english",
            "english department"
        ],
        "psychology": [
            "psychology",
            "psychology department"
        ],
        "management": [
            "management",
            "management department"
        ],
        "fashion technology": [
            "fashion technology",
            "fashion tech"
        ],
        "hotel management": [
            "hotel management",
            "hotel"
        ],
        "social work": [
            "social work",
            "social work department",
            "msw"
        ],
        "malayalam": [
            "malayalam",
            "malayalam department"
        ]
    }

    # -----------------------------------------
    # Detect department
    # -----------------------------------------

    for department, aliases in department_aliases.items():
        if any(
            re.search(
                rf"\b{re.escape(alias)}\b",
                text
            )
            for alias in aliases
        ):
            result["department"] = department
            break

    # -----------------------------------------
    # COURSE INTENT
    # -----------------------------------------

    course_keywords = [
        "course",
        "courses",
        "program",
        "programs",
        "programme",
        "programmes",
        "degree",
        "degrees",
        "study",
        "studies",
        "offer",
        "offers",
        "available"
    ]

    course_degree_keywords = [
        "b.a",
        "ba",
        "b.com",
        "bcom",
        "b.sc",
        "bsc",
        "m.a",
        "ma",
        "m.com",
        "mcom",
        "m.sc",
        "msc"
    ]

    if (
        any(keyword in text for keyword in course_keywords)
        or any(keyword in text for keyword in course_degree_keywords)
    ):
        result["intent"] = "course"

    # -----------------------------------------
    # Course level
    # -----------------------------------------

    if any(
        keyword in text
        for keyword in [
            "undergraduate",
            "under graduate",
            "ug",
            "bachelor",
            "bachelors"
        ]
    ):
        result["course_level"] = "UG"

    elif any(
        keyword in text
        for keyword in [
            "postgraduate",
            "post graduate",
            "pg",
            "master",
            "masters"
        ]
    ):
        result["course_level"] = "PG"

    # -----------------------------------------
    # Specific course detection
    # -----------------------------------------

    course_aliases = {
        "B.A. English Language & Literature": [
            "b.a english",
            "ba english",
            "ba english language",
            "english language and literature",
            "english language & literature"
        ],

        "B.Com. Commerce with Computer Applications": [
            "b.com",
            "bcom",
            "b.com commerce",
            "commerce with computer applications",
            "bcom computer applications"
        ],

        "B.Sc. Mathematics": [
            "b.sc mathematics",
            "bsc mathematics",
            "bsc maths",
            "b.sc maths"
        ],

        "B.Sc. Physics": [
            "b.sc physics",
            "bsc physics"
        ],

        "B.Sc. Chemistry": [
            "b.sc chemistry",
            "bsc chemistry"
        ],

        "B.Sc. Computer Science": [
            "b.sc computer science",
            "bsc computer science",
            "bsc cs"
        ],

        "M.A. English Language & Literature": [
            "m.a english",
            "ma english",
            "ma english language",
            "m.a english language and literature"
        ],

        "M.Com. Finance & Taxation": [
            "m.com",
            "mcom",
            "m.com finance",
            "mcom finance",
            "finance and taxation",
            "finance & taxation"
        ],

        "M.Sc. Mathematics": [
            "m.sc mathematics",
            "msc mathematics",
            "msc maths",
            "m.sc maths"
        ],

        "M.Sc. Physics": [
            "m.sc physics",
            "msc physics"
        ],

        "M.Sc. Chemistry": [
            "m.sc chemistry",
            "msc chemistry"
        ],

        "M.Sc. Computer Science": [
            "m.sc computer science",
            "msc computer science",
            "msc cs"
        ]
    }

    for course_name, aliases in course_aliases.items():
        if any(
            re.search(
                rf"\b{re.escape(alias)}\b",
                text
            )
            for alias in aliases
        ):
            result["course_name"] = course_name
            result["intent"] = "course"

            # Automatically determine level
            if course_name.startswith("B."):
                result["course_level"] = "UG"
            elif course_name.startswith("M."):
                result["course_level"] = "PG"

            break

    # -----------------------------------------
    # Faculty intent
    # -----------------------------------------

    faculty_keywords = [
        "hod",
        "head of department",
        "head of the department",
        "head the department",
        "department head",
        "who heads",
        "who teaches",
        "teacher",
        "teachers",
        "professor",
        "faculty",
        "lecturer",
        "principal",
        "vice principal"
    ]

    if any(
        keyword in text
        for keyword in faculty_keywords
    ):
        result["intent"] = "faculty"

    # -----------------------------------------
    # Achievement intent
    # -----------------------------------------

    achievement_keywords = [
        "rank",
        "rank holder",
        "achievement",
        "achievements",
        "achieved",
        "cleared",
        "performer",
        "outstanding",
        "topped",
        "topper",
        "cma"
    ]

    if any(
        keyword in text
        for keyword in achievement_keywords
    ):
        result["intent"] = "achievement"

    # -----------------------------------------
    # Achievement topics
    # -----------------------------------------

    if "cyber forensic" in text:
        result["achievement_topic"] = "cyber forensic"

    elif "fashion technology" in text:
        result["achievement_topic"] = "fashion technology"

    elif "cma" in text:
        result["achievement_topic"] = "cma"

    # -----------------------------------------
    # College information intent
    # -----------------------------------------

    college_keywords = [
        "college",
        "established",
        "founded",
        "accredited",
        "accreditation",
        "recognition",
        "recognitions",
        "recognized",
        "affiliated",
        "affiliation",
        "website",
        "contact",
        "phone",
        "telephone"
    ]

    if any(
        keyword in text
        for keyword in college_keywords
    ):
        # Don't override a specific course question
        # merely because it contains the word "college".
        if result["intent"] == "unknown":
            result["intent"] = "college"

    # -----------------------------------------
    # Specific college questions
    # -----------------------------------------

    if (
        "university" in text
        and "under" in text
    ):
        result["intent"] = "college"

    if (
        "aicte" in text
        and any(
            word in text
            for word in [
                "approved",
                "approval",
                "recognition",
                "recognized"
            ]
        )
    ):
        result["intent"] = "college"

    # -----------------------------------------
    # Person detection
    # -----------------------------------------

    person_match = re.search(
        r"\b(?:is|was)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:a|an)\b",
        question
    )

    if person_match:
        result["person"] = person_match.group(1).strip()

    if result["person"] is None:
        person_match = re.search(
            r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+"
            r"(?:is|was)\s+(?:a\s+)?(?:rank holder|performer)\b",
            question
        )

        if person_match:
            result["person"] = person_match.group(1).strip()

    return result