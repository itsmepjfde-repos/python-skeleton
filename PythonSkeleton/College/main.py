import time

import course_operations
import file_operations
import student_operations


def show_menu():
    print("[main] Calling main.show_menu().")
    print("\n=== Student Management System ===")
    print("1. Register Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Check Eligibility")
    print("5. View Courses")
    print("6. View Registered Courses")
    print("7. Save Students")
    print("8. Export CSV")
    print("9. Exit")


def main():
    print("[main] Calling file_operations.load_students_json().")
    students = file_operations.load_students_json()
    unsaved_changes = False

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            age = input("Enter student age: ").strip()
            courses = course_operations.view_courses()
            print("\nAvailable Courses")
            for course in courses:
                print(f"{course['course_id']}: {course['course_name']}")
            selected_course_ids = [
                course_id.strip()
                for course_id in input(
                    "Enter course ID(s) separated by commas (or leave blank): "
                ).split(",")
                if course_id.strip()
            ]
            print("[main] Dispatching option 1 to student_operations.register_student().")
            was_added, message = student_operations.register_student(
                students, student_id, name, age, selected_course_ids, courses
            )
            print(message)
            if was_added:
                unsaved_changes = True
        elif choice == "2":
            print("[main] Dispatching option 2 to student_operations.view_students().")
            result = student_operations.view_students(students)
            if result:
                print("\nRegistered Students")
                for student in result:
                    print(
                        f"ID: {student['student_id']} | Name: {student['name']} | "
                        f"Age: {student['age']}"
                    )
            else:
                print("There are no registered students.")
        elif choice == "3":
            name = input("Enter a student name to search: ")
            print("[main] Dispatching option 3 to student_operations.search_student().")
            matches = student_operations.search_student(students, name)
            if matches:
                print("\nMatching Students")
                for student in matches:
                    print(
                        f"ID: {student['student_id']} | Name: {student['name']} | "
                        f"Age: {student['age']}"
                    )
            else:
                print(f"No students found matching '{name}'.")
        elif choice == "4":
            student_id = input("Enter the student ID to check: ").strip()
            print("[main] Dispatching option 4 to student_operations.check_eligibility().")
            student, is_eligible = student_operations.check_eligibility(
                students, student_id
            )
            if student is None:
                print(f"No student found with ID '{student_id}'.")
            elif is_eligible:
                print(f"{student['name']} is eligible (age 18 or older).")
            else:
                print(f"{student['name']} is not eligible (under age 18).")
        elif choice == "5":
            print("[main] Dispatching option 5 to course_operations.view_courses().")
            courses = course_operations.view_courses()
            print("\nAvailable Courses")
            for course in courses:
                print(f"{course['course_id']}: {course['course_name']}")
        elif choice == "6":
            print(
                "[main] Dispatching option 6 to "
                "course_operations.view_registered_courses()."
            )
            registered_courses, unknown_course_ids = (
                course_operations.view_registered_courses(students)
            )
            if not registered_courses and not unknown_course_ids:
                print("No courses have been registered by students.")
            else:
                print("\nUnique Registered Courses")
                for course in registered_courses:
                    print(f"{course['course_id']}: {course['course_name']}")
                for course_id in unknown_course_ids:
                    print(f"{course_id}: Course details are unavailable.")
        elif choice == "7":
            print("[main] Dispatching option 7 to file_operations.save_students_json().")
            file_operations.save_students_json(students)
            unsaved_changes = False
        elif choice == "8":
            print("[main] Dispatching option 8 to file_operations.export_students_csv().")
            file_operations.export_students_csv(students)
        elif choice == "9":
            if unsaved_changes:
                print(
                    "[main] Unsaved changes detected; calling "
                    "file_operations.save_students_json()."
                )
                file_operations.save_students_json(students)
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

        print("[main] Operation complete. Returning to the main menu in 5 seconds.")
        time.sleep(5)


if __name__ == "__main__":
    main()
