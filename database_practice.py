
import sqlite3


def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks REAL NOT NULL CHECK (marks >= 0 AND marks <= 100)
        )
    """)
    connection.commit()


def add_student(connection):
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        marks = float(input("Enter marks (0-100): "))

        if student_id <= 0:
            print("Student ID must be positive.")
            return

        if not name:
            print("Name cannot be empty.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        connection.execute(
            "INSERT INTO students (student_id, name, marks) VALUES (?, ?, ?)",
            (student_id, name, marks)
        )
        connection.commit()
        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid number.")
    except sqlite3.IntegrityError:
        print("That student ID already exists.")


def display_students(connection):
    cursor = connection.execute(
        "SELECT student_id, name, marks FROM students ORDER BY student_id"
    )
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\n--- All Students ---")
    for student in students:
        print(f"ID: {student[0]} | Name: {student[1]} | Marks: {student[2]}")


def search_student(connection):
    try:
        student_id = int(input("Enter student ID to search: "))
        cursor = connection.execute(
            "SELECT student_id, name, marks FROM students WHERE student_id = ?",
            (student_id,)
        )
        student = cursor.fetchone()

        if student:
            print(f"Found: ID: {student[0]} | Name: {student[1]} | Marks: {student[2]}")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


def update_marks(connection):
    try:
        student_id = int(input("Enter student ID: "))
        marks = float(input("Enter new marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        cursor = connection.execute(
            "UPDATE students SET marks = ? WHERE student_id = ?",
            (marks, student_id)
        )
        connection.commit()

        if cursor.rowcount > 0:
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter valid numbers.")


def delete_student(connection):
    try:
        student_id = int(input("Enter student ID to delete: "))

        cursor = connection.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )
        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


def main():
    connection = sqlite3.connect("students.db")
    create_table(connection)

    try:
        while True:
            print("\n=== Student Management System ===")
            print("1. Add student")
            print("2. Display students")
            print("3. Search student")
            print("4. Update marks")
            print("5. Delete student")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                add_student(connection)
            elif choice == "2":
                display_students(connection)
            elif choice == "3":
                search_student(connection)
            elif choice == "4":
                update_marks(connection)
            elif choice == "5":
                delete_student(connection)
            elif choice == "6":
                print("Exiting Student Management System.")
                break
            else:
                print("Invalid choice. Please enter 1-6.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()

