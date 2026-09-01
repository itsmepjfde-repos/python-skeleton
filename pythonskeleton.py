"""
===========================================================
🎓 COLLEGE STUDENT REGISTRATION SYSTEM
===========================================================

Python concepts demonstrated:

1. 📦 Modules & Imports
2. 🗄️ Data Structures
      - List
      - Dictionary
      - Tuple
      - Set
      - Nested List + Dictionary
3. 🔌 Functions
4. 🛡️ Conditional Statements
5. 🔁 For Loop
6. 🔄 While Loop
7. 💾 File Handling
===========================================================
"""

# =========================================================
# 📦 1. MODULES & IMPORTS
# =========================================================

# json → used to save structured data into a JSON file
import json

# csv → used to export student information as a CSV file
import csv

# time → used to pause the program for better visibility
import time


# =========================================================
# 🗄️ 2. DATA STRUCTURES
# =========================================================

# ---------------------------------------------------------
# 📚 LIST
# ---------------------------------------------------------
# A LIST stores multiple values in an ordered collection.
#
# Example:
# ["Python", "Java", "Data Science"]
#
# We can add, remove, or change items in a list.

courses = [
    "Python",
    "Data Science",
    "Artificial Intelligence",
    "Web Development"
]


# ---------------------------------------------------------
# 🔐 TUPLE
# ---------------------------------------------------------
# A TUPLE is an ordered collection that normally should
# not be changed after it is created.
#
# Think of it as a fixed set of information.
#
# Here, the college information is fixed.

college_info = (
    "ABC College",
    "Chennai",
    2026
)


# ---------------------------------------------------------
# 🧺 SET
# ---------------------------------------------------------
# A SET stores unique values.
#
# If the same value appears more than once,
# Python keeps only one copy.
#
# Useful when we want to know:
# "What different courses are registered?"

registered_courses = set()


# ---------------------------------------------------------
# 🗄️ DICTIONARY
# ---------------------------------------------------------
# A DICTIONARY stores information using:
#
#       KEY → VALUE
#
# Example:
#
# "name"   → "Rahul"
# "age"    → 20
# "course" → "Python"
#
# Think of it like a filing cabinet with labels.

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}


# ---------------------------------------------------------
# 📚 LIST OF DICTIONARIES
# ---------------------------------------------------------
# This is one of the most useful structures in real programs.
#
# The LIST stores multiple students.
#
# Each DICTIONARY stores information about ONE student.

students = [
    {
        "name": "Rahul",
        "age": 20,
        "course": "Python"
    },

    {
        "name": "Priya",
        "age": 21,
        "course": "Data Science"
    },

    {
        "name": "Arun",
        "age": 19,
        "course": "Artificial Intelligence"
    }
]


# =========================================================
# 🔌 3. FUNCTION — REGISTER STUDENT
# =========================================================

def register_student():

    print("\n🎓 STUDENT REGISTRATION")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))

    # Display available courses
    print("\nAvailable Courses:")

    # 🔁 FOR LOOP
    # Go through every course in our LIST.

    for course in courses:

        print("-", course)

    course = input("\nEnter course: ")

    # 🛡️ CONDITIONAL STATEMENT
    # Check whether the selected course exists.

    if course not in courses:

        print("❌ Invalid course.")
        return

    # -----------------------------------------------------
    # DICTIONARY
    # -----------------------------------------------------
    # Create a dictionary containing one student's details.

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    # -----------------------------------------------------
    # LIST
    # -----------------------------------------------------
    # Add the dictionary to our students LIST.

    students.append(student)

    # -----------------------------------------------------
    # SET
    # -----------------------------------------------------
    # Add the course to our SET.
    #
    # If Python was already registered,
    # the SET will still contain Python only once.

    registered_courses.add(course)

    print("\n✅ Student registered successfully!")


# =========================================================
# 📋 4. FUNCTION — DISPLAY STUDENTS
# =========================================================

def display_students():

    print("\n📋 REGISTERED STUDENTS")
    print("-" * 50)

    # 🛡️ CONDITIONAL
    # Check whether the LIST is empty.

    if len(students) == 0:

        print("No students registered.")

        return

    # 🔁 FOR LOOP
    # Visit every dictionary inside the students LIST.

    for student in students:

        print(
            "Name:",
            student["name"]
        )

        print(
            "Age:",
            student["age"]
        )

        print(
            "Course:",
            student["course"]
        )

        print("-" * 50)


# =========================================================
# 🔍 5. FUNCTION — SEARCH STUDENT
# =========================================================

def search_student():

    name = input(
        "\nEnter student name to search: "
    )

    found = False

    # 🔁 FOR LOOP
    # Search through every student.

    for student in students:

        # 🛡️ CONDITIONAL
        # Compare the student's name with the
        # name entered by the user.

        if student["name"].lower() == name.lower():

            print("\n✅ STUDENT FOUND")

            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

            found = True

    # If no student was found

    if found == False:

        print("\n❌ Student not found.")


# =========================================================
# 🛡️ 6. FUNCTION — CHECK ELIGIBILITY
# =========================================================

def check_eligibility():

    age = int(
        input("\nEnter student age: ")
    )

    # CONDITIONAL STATEMENT
    #
    # The program makes a decision based
    # on the student's age.

    if age >= 18:

        print(
            "✅ Student is eligible for registration."
        )

    else:

        print(
            "❌ Student must be at least 18 years old."
        )


# =========================================================
# 📚 7. FUNCTION — DISPLAY COURSES
# =========================================================

def display_courses():

    print("\n📚 AVAILABLE COURSES")

    # FOR LOOP through the LIST

    for course in courses:

        print("-", course)


# =========================================================
# 🧺 8. FUNCTION — DISPLAY UNIQUE COURSES
# =========================================================

def display_registered_courses():

    print("\n🧺 COURSES WITH REGISTERED STUDENTS")

    # SET contains only UNIQUE course names.

    if len(registered_courses) == 0:

        print("No courses have registrations yet.")

        return

    for course in registered_courses:

        print("-", course)


# =========================================================
# 💾 9. FUNCTION — SAVE TO JSON
# =========================================================

def save_students():

    # Open/create a JSON file.

    with open(
        "students.json",
        "w"
    ) as file:

        # Save our LIST of DICTIONARIES.

        json.dump(
            students,
            file,
            indent=4
        )

    print(
        "\n💾 Student data saved to students.json"
    )


# =========================================================
# 📖 10. FUNCTION — LOAD FROM JSON
# =========================================================

def load_students():

    global students

    try:

        with open(
            "students.json",
            "r"
        ) as file:

            students = json.load(file)

        # Rebuild the SET after loading data.
        # Some older records may store course as a list like ["Python"].
        # Convert them to a plain string before adding to a set.

        registered_courses.clear()

        for student in students:

            course = student.get("course")

            if isinstance(course, list):

                if len(course) > 0:
                    student["course"] = course[0]
                else:
                    student["course"] = ""

            registered_courses.add(
                student["course"]
            )

        print(
            "\n📖 Previous student data loaded."
        )

    except FileNotFoundError:

        print(
            "\nℹ️ No previous student data found."
        )


# =========================================================
# 📊 11. FUNCTION — EXPORT TO CSV
# =========================================================

def save_csv():

    with open(
        "students.csv",
        "w",
        newline=""
    ) as file:

        # DictWriter works nicely with
        # our LIST of DICTIONARIES.

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "age",
                "course"
            ]
        )

        writer.writeheader()

        writer.writerows(students)

    print(
        "\n📊 Student data exported to students.csv"
    )


# =========================================================
# 🚪 12. MAIN FUNCTION
# =========================================================
# main() is the starting point of our program.

def main():

    # Load previous data if available.

    load_students()

    # -----------------------------------------------------
    # Display our TUPLE
    # -----------------------------------------------------

    print("\n🏫 COLLEGE INFORMATION")

    print("College:", college_info[0])
    print("Location:", college_info[1])
    print("Year:", college_info[2])


    # -----------------------------------------------------
    # 🔄 WHILE LOOP
    # -----------------------------------------------------
    # Keep showing the menu until the user chooses Exit.

    while True:

        print("\n")
        print("=" * 50)
        print("🎓 COLLEGE STUDENT REGISTRATION SYSTEM")
        print("=" * 50)

        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Check Eligibility")
        print("5. View Available Courses")
        print("6. View Registered Courses")
        print("7. Save Students")
        print("8. Export CSV")
        print("9. Exit")

        choice = input(
            "\nEnter your choice: "
        )


        # =================================================
        # 🛡️ CONDITIONAL STATEMENTS
        # =================================================
        # Decide what the program should do.

        if choice == "1":

            register_student()


        elif choice == "2":

            display_students()


        elif choice == "3":

            search_student()


        elif choice == "4":

            check_eligibility()


        elif choice == "5":

            display_courses()


        elif choice == "6":

            display_registered_courses()


        elif choice == "7":

            save_students()


        elif choice == "8":

            save_csv()


        elif choice == "9":

            print(
                "\n👋 Thank you for using "
                "the College Registration System!"
            )

            # Stop the WHILE LOOP.

            break


        else:

            print(
                "\n❌ Invalid choice."
            )

            print(
                "Please select 1–9."
            )

        # Pause for 10 seconds so user can read output clearly
        time.sleep(5)


# =========================================================
# 🚪 PROGRAM ENTRY POINT
# =========================================================
# Python starts the program through main().

if __name__ == "__main__":

    main()