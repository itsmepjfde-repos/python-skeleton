import csv
import json
from pathlib import Path


DATA_DIRECTORY = Path(__file__).parent
STUDENTS_JSON_PATH = DATA_DIRECTORY / "students.json"
STUDENTS_CSV_PATH = DATA_DIRECTORY / "students.csv"


def load_students_json():
    """Load students from students.json, returning an empty list if absent."""
    print("[file_operations] Entered load_students_json().")
    if not STUDENTS_JSON_PATH.exists():
        print("students.json was not found; starting with an empty student list.")
        return []

    with STUDENTS_JSON_PATH.open("r", encoding="utf-8") as json_file:
        students = json.load(json_file)

    if not isinstance(students, list):
        raise ValueError("students.json must contain a JSON list of students.")

    print(f"Loaded {len(students)} student(s) from students.json.")
    return students


def save_students_json(students):
    """Save the current student list to students.json."""
    print("[file_operations] Entered save_students_json().")
    with STUDENTS_JSON_PATH.open("w", encoding="utf-8") as json_file:
        json.dump(students, json_file, indent=4)

    print(f"Saved {len(students)} student(s) to students.json.")
    return STUDENTS_JSON_PATH


def export_students_csv(students):
    """Export the current student list to students.csv."""
    print("[file_operations] Entered export_students_csv().")
    fieldnames = ["student_id", "name", "age", "registered_courses"]

    with STUDENTS_CSV_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            csv_student = student.copy()
            csv_student["registered_courses"] = ", ".join(
                csv_student.get("registered_courses", [])
            )
            writer.writerow(csv_student)

    print(f"Exported {len(students)} student(s) to students.csv.")
    return STUDENTS_CSV_PATH
