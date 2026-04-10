# Encapsulation: private data + controlled access
class Student:
    def __init__(self, name, reg_no):
        self.__name = name
        self.__reg_no = reg_no
        self.__marks = []

    def add_mark(self, mark):
        if 0 <= mark < 100:
            self.__marks.append(mark)
        else:
            print("Invalid mark")

    def calculate_cgpa(self):
        if len(self.__marks) == 0:
            return 0
        return round(sum(self.__marks) / len(self.__marks), 2)

    def get_details(self):
        return self.__name, self.__reg_no


# Polymorphism: method overriding
class EngineeringStudent(Student):
    def display(self):
        name, reg = self.get_details()
        print("\n--- Engineering Student ---")
        print(f"Name: {name}")
        print(f"Reg No: {reg}")
        print("CGPA:", self.calculate_cgpa())


# Polymorphism: method overriding
class DegreeStudent(Student):
    def display(self):
        name, reg = self.get_details()
        print("\n--- Degree Student ---")
        print(f"Student: {name} ({reg})")
        print("Final CGPA:", self.calculate_cgpa())



def main():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nEnter details for student {i+1}")
        name = input("Enter name: ")
        reg = input("Enter reg no: ")

        choice = input("Type (1: Engineering, 2: Degree): ")

        if choice == "1":
            s = EngineeringStudent(name, reg)
        else:
            s = DegreeStudent(name, reg)

        m = int(input("Enter number of subjects: "))

        for _ in range(m):
            mark = int(input("Enter mark: "))
            s.add_mark(mark)

        students.append(s)

    print("\n=== Student Results ===")
    for s in students:
        s.display()   # Polymorphism


if __name__ == "__main__":
    main()