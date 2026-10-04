import streamlit as st

import course_operations
import file_operations
import student_operations


st.set_page_config(page_title="Student Management", page_icon="🎓")

st.title("Student Management System")
st.caption("Manage students and browse course information.")

if "students" not in st.session_state:
    print("[streamlit_app] Calling file_operations.load_students_json().")
    try:
        st.session_state.students = file_operations.load_students_json()
    except (OSError, ValueError) as error:
        st.error(f"Could not load students.json: {error}")
        st.stop()
    st.session_state.unsaved_changes = False

students = st.session_state.students
if st.session_state.unsaved_changes:
    st.warning("You have unsaved student changes. Use Save Students to keep them.")
else:
    st.success(f"Student data is saved. Current records: {len(students)}.")

pages = [
    "Register Student",
    "View Students",
    "Search Student",
    "Check Eligibility",
    "View Courses",
    "View Registered Courses",
    "Save Students",
    "Export CSV",
    "Exit",
]
page = st.sidebar.radio("Choose an option", pages)
st.sidebar.caption("Changes are kept in this browser session until saved.")

if page == "Register Student":
    st.header("Register Student")
    with st.form("register_student_form"):
        student_id = st.text_input("Student ID")
        name = st.text_input("Student name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        available_courses = course_operations.view_courses()
        selected_course_ids = st.multiselect(
            "Select courses",
            options=[course["course_id"] for course in available_courses],
            format_func=lambda course_id: next(
                f"{course['course_name']} ({course['course_id']})"
                for course in available_courses
                if course["course_id"] == course_id
            ),
        )
        submitted = st.form_submit_button("Register")

    if submitted:
        print("[streamlit_app] Calling student_operations.register_student().")
        was_added, message = student_operations.register_student(
            students,
            student_id,
            name,
            age,
            selected_course_ids,
            available_courses,
        )
        if was_added:
            st.session_state.unsaved_changes = True
            st.success(message)
        else:
            st.error(message)

elif page == "View Students":
    st.header("Registered Students")
    print("[streamlit_app] Calling student_operations.view_students().")
    student_records = student_operations.view_students(students)
    if student_records:
        st.dataframe(student_records, hide_index=True, use_container_width=True)
    else:
        st.info("There are no registered students yet.")

elif page == "Search Student":
    st.header("Search Student")
    with st.form("search_student_form"):
        search_name = st.text_input("Name to search for")
        search_submitted = st.form_submit_button("Search")

    if search_submitted:
        if not search_name.strip():
            st.warning("Enter a name or part of a name to search.")
        else:
            print("[streamlit_app] Calling student_operations.search_student().")
            matching_students = student_operations.search_student(students, search_name)
            if matching_students:
                st.dataframe(
                    matching_students, hide_index=True, use_container_width=True
                )
            else:
                st.info(f"No students found matching '{search_name}'.")

elif page == "Check Eligibility":
    st.header("Check Eligibility")
    if not students:
        st.info("Register or load a student before checking eligibility.")
    else:
        selected_student_id = st.selectbox(
            "Select a student",
            options=[student["student_id"] for student in students],
            format_func=lambda student_id: next(
                f"{student['name']} ({student['student_id']})"
                for student in students
                if student["student_id"] == student_id
            ),
        )
        if st.button("Check eligibility"):
            print("[streamlit_app] Calling student_operations.check_eligibility().")
            student, is_eligible = student_operations.check_eligibility(
                students, selected_student_id
            )
            if student is None:
                st.error(f"No student found with ID '{selected_student_id}'.")
            elif is_eligible:
                st.success(f"{student['name']} is eligible (age 18 or older).")
            else:
                st.warning(f"{student['name']} is not eligible (under age 18).")

elif page == "View Courses":
    st.header("Available Courses")
    print("[streamlit_app] Calling course_operations.view_courses().")
    available_courses = course_operations.view_courses()
    st.dataframe(available_courses, hide_index=True, use_container_width=True)

elif page == "View Registered Courses":
    st.header("Unique Registered Courses")
    print("[streamlit_app] Calling course_operations.view_registered_courses().")
    registered_courses, unknown_course_ids = (
        course_operations.view_registered_courses(students)
    )
    if registered_courses:
        st.dataframe(registered_courses, hide_index=True, use_container_width=True)
    else:
        st.info("No known courses have been registered by students.")

    if unknown_course_ids:
        st.warning(
            "Course details are unavailable for: "
            + ", ".join(unknown_course_ids)
        )

elif page == "Save Students":
    st.header("Save Students")
    st.write(f"Student data file: `{file_operations.STUDENTS_JSON_PATH}`")
    if st.button("Save student data"):
        print("[streamlit_app] Calling file_operations.save_students_json().")
        try:
            saved_path = file_operations.save_students_json(students)
        except OSError as error:
            st.error(f"Could not save student data: {error}")
        else:
            st.session_state.unsaved_changes = False
            st.success(f"Saved {len(students)} student(s) to `{saved_path}`.")

elif page == "Export CSV":
    st.header("Export Students to CSV")
    st.write(f"CSV file: `{file_operations.STUDENTS_CSV_PATH}`")
    if st.button("Export student data"):
        print("[streamlit_app] Calling file_operations.export_students_csv().")
        try:
            exported_path = file_operations.export_students_csv(students)
        except OSError as error:
            st.error(f"Could not export student data: {error}")
        else:
            st.success(f"Exported {len(students)} student(s) to `{exported_path}`.")

elif page == "Exit":
    st.header("Exit")
    if st.session_state.unsaved_changes:
        st.warning(
            "There are unsaved changes. Use Save Students before closing this tab "
            "if you want to keep them."
        )
    st.info("You can now close this browser tab. The Streamlit server may still run.")
