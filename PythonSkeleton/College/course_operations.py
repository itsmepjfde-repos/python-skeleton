COURSES = [
    {"course_id": "CS101", "course_name": "Introduction to Programming"},
    {"course_id": "MATH201", "course_name": "Calculus I"},
    {"course_id": "BIO110", "course_name": "Biology Basics"},
]


def view_courses(courses=COURSES):
    """Return all available courses."""
    print("[course_operations] Entered view_courses().")
    return courses


def view_registered_courses(students, courses=COURSES):
    """Return each course opted for by at least one student, only once."""
    print("[course_operations] Entered view_registered_courses().")
    registered_course_ids = {
        course_id
        for student in students
        for course_id in student.get("registered_courses", [])
    }

    courses_by_id = {course["course_id"]: course for course in courses}
    registered_courses = [
        courses_by_id[course_id]
        for course_id in sorted(registered_course_ids)
        if course_id in courses_by_id
    ]
    unknown_course_ids = sorted(registered_course_ids - courses_by_id.keys())
    return registered_courses, unknown_course_ids
