# student_grades.py

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average_grade(self):
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return average

    def get_letter_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def get_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_grades(self):
        average = self.calculate_average_grade()
        letter_grade = self.get_letter_grade(average)
        gpa = self.get_gpa(average)
        print(f"Student: {self.name}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    student_name = input("Enter student name: ")
    student = Student(student_name)

    while True:
        print("\nOptions:")
        print("  1. Add grade")
        print("  2. Display grades")
        print("  3. Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            student.add_grade(subject, grade)
        elif choice == "2":
            student.display_grades()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()