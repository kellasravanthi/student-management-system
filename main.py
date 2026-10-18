class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if student.student_id <= 0:
            print("Error: Student ID must be positive.")
            return

        if not student.name.strip():
            print("Error: Name cannot be empty.")
            return

        if not 0 <= student.marks <= 100:
            print("Error: Marks must be between 0 and 100.")
            return

        for existing in self.students:
            if existing.student_id == student.student_id:
                print("Error: Student ID already exists.")
                return

        self.students.append(student)
        print(f"{student.name} added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student found:")
                student.display()
                return

        print("Student not found.")


manager = StudentManager()

manager.add_student(Student(101, "Ravi", 85))
manager.add_student(Student(102, "Priya", 92))
manager.add_student(Student(103, "Arun", 78))

print("\n--- All Student Records ---")
manager.display_students()

print("\n--- Search Student ---")
manager.search_student(102)
manager.search_student(999)
