import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read student records. Starting with an empty list.")
    return []


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    if any(student["roll"] == roll for student in students):
        print("Roll number already exists!")
        return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()
    marks = input("Enter Marks: ").strip()

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-------------------------")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


def search_student(students):
    roll = input("Enter Roll Number to Search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")


def update_student(students):
    roll = input("Enter Roll Number to Update: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("Enter new details (leave a field blank to keep its current value):")

            for field, label in [
                ("name", "Name"),
                ("age", "Age"),
                ("course", "Course"),
                ("marks", "Marks")
            ]:
                new_value = input(f"New {label} [{student[field]}]: ").strip()
                if new_value:
                    student[field] = new_value

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student(students):
    roll = input("Enter Roll Number to Delete: ").strip()

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")


def main():
    students = load_students()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
