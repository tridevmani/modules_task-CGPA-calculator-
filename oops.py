import datetime


class InvalidGradeError(Exception):
    pass


class Person:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no


class Student(Person):
    def __init__(self, name, reg_no):
        super().__init__(name, reg_no)
        self.subjects = {}

    def add_subject(self, subject, grade):
        if grade < 0 or grade > 10:
            raise InvalidGradeError("Invalid grade!")
        self.subjects[subject] = grade

    def calculate_cgpa(self):
        if not self.subjects:
            return 0
        return round(sum(self.subjects.values()) / len(self.subjects), 2)

    def display(self):
        print(f"\nName: {self.name}, Reg No: {self.reg_no}")
        print("Subjects:")
        for sub, grade in self.subjects.items():
            print(f"{sub}: {grade}")
        print("CGPA:", self.calculate_cgpa())


# Save to file
def save_student(student):
    with open("records.txt", "a") as f:
        f.write(f"{student.name},{student.reg_no},{student.calculate_cgpa()}\n")


# View all records
def view_records():
    try:
        with open("records.txt", "r") as f:
            print("\n--- Saved Records ---")
            print(f.read())
    except FileNotFoundError:
        print("No records found.")


# Search student
def search_student(reg_no):
    try:
        with open("records.txt", "r") as f:
            for line in f:
                name, reg, cgpa = line.strip().split(",")
                if reg == reg_no:
                    print(f"Found: {name}, CGPA: {cgpa}")
                    return
        print("Student not found.")
    except FileNotFoundError:
        print("No records available.")


# Ranking system
def rank_students():
    try:
        with open("records.txt", "r") as f:
            data = []
            for line in f:
                name, reg, cgpa = line.strip().split(",")
                data.append((name, reg, float(cgpa)))

        data.sort(key=lambda x: x[2], reverse=True)

        print("\n--- Ranking ---")
        for i, s in enumerate(data, 1):
            print(f"{i}. {s[0]} - CGPA: {s[2]}")

    except FileNotFoundError:
        print("No records to rank.")


def main():
    while True:
        print("\n=== CGPA System ===")
        print("1. Add Student")
        print("2. View Records")
        print("3. Search Student")
        print("4. Rank Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                name = input("Enter name: ")
                reg = input("Enter reg no: ")

                student = Student(name, reg)

                n = int(input("Number of subjects: "))
                for _ in range(n):
                    sub = input("Subject: ")
                    grade = float(input("Grade: "))
                    student.add_subject(sub, grade)

                student.display()
                save_student(student)

            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            view_records()

        elif choice == "3":
            reg = input("Enter reg no to search: ")
            search_student(reg)

        elif choice == "4":
            rank_students()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()