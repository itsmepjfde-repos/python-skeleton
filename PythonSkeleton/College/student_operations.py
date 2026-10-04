def register_student(students, student_id, name, age, selected_course_ids, courses):
    """Add a student to the in-memory list and return a status and message."""
    print("[student_operations] Entered register_student().")
    student_id = str(student_id).strip()
    name = str(name).strip()
    selected_course_ids = list(dict.fromkeys(selected_course_ids))

    if not student_id:
        return False, "Student ID cannot be empty."
    if any(student["student_id"] == student_id for student in students):
        return False, f"A student with ID {student_id} already exists."
    if not name:
        return False, "Student name cannot be empty."

    try:
        student_age = int(age)
    except (TypeError, ValueError):
        return False, "Age must be a whole number."

    if student_age < 0:
        return False, "Age cannot be negative."

    available_course_ids = {course["course_id"] for course in courses}
    invalid_course_ids = set(selected_course_ids) - available_course_ids
    if invalid_course_ids:
        invalid_ids = ", ".join(sorted(invalid_course_ids))
        return False, f"Unknown course ID(s): {invalid_ids}."

    students.append(
        {
            "student_id": student_id,
            "name": name,
            "age": student_age,
            "registered_courses": selected_course_ids,
        }
    )
    return True, f"Student {name} registered successfully with {len(selected_course_ids)} course(s)."


def view_students(students):
    """Return all students currently in memory."""
    print("[student_operations] Entered view_students().")
    return students


def search_student(students, name):
    """Return students whose names contain the supplied search text."""
    print("[student_operations] Entered search_student().")
    search_text = name.strip().casefold()
    return [
        student
        for student in students
        if search_text in student["name"].casefold()
    ]


def check_eligibility(students, student_id):
    """Return the matching student and eligibility, or (None, None)."""
    print("[student_operations] Entered check_eligibility().")
    for student in students:
        if student["student_id"] == student_id:
            return student, student["age"] >= 18

    return None, None
