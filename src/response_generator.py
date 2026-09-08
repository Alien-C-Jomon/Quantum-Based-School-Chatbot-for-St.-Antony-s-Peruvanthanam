def generate_response(question, answer):

    if not answer:
        return (
            "❌ I couldn't find verified information "
            "in my knowledge base."
        )

    # =========================================
    # LIST RESPONSES
    # =========================================

    if isinstance(answer, list):

        # -------------------------------------
        # Achievement results
        # -------------------------------------

        if answer and "achievement" in answer[0]:

            lines = [
                "🏆 Verified achievements:\n"
            ]

            for item in answer:

                lines.append(
                    f"• {item['name']} — "
                    f"{item['achievement']} "
                    f"in {item['program']} "
                    f"({item['year']})"
                )

            return "\n".join(lines)

        # -------------------------------------
        # Faculty results
        # -------------------------------------

        if answer and "role" in answer[0]:

            question_lower = question.lower()

            hod_keywords = [
                "hod",
                "head of department",
                "head of the department",
                "department head",
                "who heads"
            ]

            is_hod_question = any(
                keyword in question_lower
                for keyword in hod_keywords
            )

            # Single HOD
            if is_hod_question and len(answer) == 1:

                person = answer[0]

                clean_role = (
                    person["role"]
                    .replace("HOD & ", "")
                    .replace("HOD, ", "")
                )

                return (
                    f"👩‍🏫 The Head of the "
                    f"{person['department']} Department is "
                    f"{person['name']}, "
                    f"{clean_role}."
                )

            # Multiple faculty
            lines = [
                f"👩‍🏫 Verified faculty in "
                f"{answer[0]['department']}:\n"
            ]

            for person in answer:

                lines.append(
                    f"• {person['name']} — "
                    f"{person['role']}"
                )

            return "\n".join(lines)

        # -------------------------------------
        # Course / Program results
        # -------------------------------------

        if answer and "name" in answer[0] and "level" in answer[0]:

            lines = [
                "🎓 Verified courses and programs:\n"
            ]

            for course in answer:

                name = course.get(
                    "name",
                    "Unknown course"
                )

                level = course.get(
                    "level",
                    ""
                )

                department = course.get(
                    "department",
                    ""
                )

                line = f"• {name}"

                if level:
                    line += f" — {level}"

                if department:
                    line += f" — {department}"

                lines.append(line)

            return "\n".join(lines)

    # =========================================
    # COLLEGE INFORMATION
    # =========================================

    if isinstance(answer, dict):

        # -------------------------------------
        # Established
        # -------------------------------------

        if "established" in answer:

            return (
                "🏛️ St Antony's College "
                "Peruvanthanam was established "
                f"in {answer['established']}."
            )

        # -------------------------------------
        # Official website
        # -------------------------------------

        if "official_website" in answer:

            return (
                "🌐 The official website is:\n"
                f"{answer['official_website']}"
            )

        # -------------------------------------
        # Affiliation
        # -------------------------------------

        if "affiliated_to" in answer:

            return (
                "🎓 The college is affiliated to "
                f"{answer['affiliated_to']}."
            )

        # -------------------------------------
        # Recognitions
        # -------------------------------------

        if "recognitions" in answer:

            return (
                "🏅 The college's verified "
                "recognitions include:\n"
                + "\n".join(
                    f"• {item}"
                    for item in answer["recognitions"]
                )
            )

        # -------------------------------------
        # Contact
        # -------------------------------------

        if "contact" in answer:

            lines = [
                "📞 Official college contact:"
            ]

            for key, value in answer.items():

                lines.append(
                    f"• {key.title()}: {value}"
                )

            return "\n".join(lines)

    # =========================================
    # GENERIC LIST FALLBACK
    # =========================================

    if isinstance(answer, list):

        return "\n".join(
            (
                f"• {item.get('name', 'Unknown')}"
                f" — {item.get('level', '')}"
                f" — {item.get('department', '')}"
            )
            if isinstance(item, dict)
            else f"• {item}"
            for item in answer
        )

    # =========================================
    # GENERIC DICTIONARY FALLBACK
    # =========================================

    if isinstance(answer, dict):

        return "\n".join(
            f"• {key}: {value}"
            for key, value in answer.items()
        )

    # =========================================
    # FINAL FALLBACK
    # =========================================

    return str(answer)