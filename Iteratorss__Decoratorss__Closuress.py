# Iterator: Marks List
class MarksIterator:
    def __init__(self, marks):
        self.marks = marks
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.marks):
            mark = self.marks[self.index]
            self.index += 1
            return mark
        else:
            raise StopIteration


# Decorator: Logging (FIXED)
def logger(func):
    def wrapper(*args, **kwargs):   # accepts any arguments
        student = args[0]
        print(f"\n[LOG] Processing student: {student['name']}")
        result = func(*args, **kwargs)
        print("[LOG] Completed\n")
        print("done\n")
        return result
    return wrapper


# Closure: CGPA Calculator
def cgpa_closure(max_marks):
    def calculate(marks):
        if len(marks) == 0:
            return 0
        avg = sum(marks) / len(marks)
        return round((avg / max_marks) * 10, 2)
    return calculate


# Function to process student
@logger
def process_student(student, cgpa_func):
    collected_marks = []

    # Using Iterator
    mark_iter = MarksIterator(student["marks"])
    for m in mark_iter:
        collected_marks.append(m)

    cgpa = cgpa_func(collected_marks)

    print(f"Name: {student['name']}")
    print(f"Reg No: {student['reg']}")
    print(f"Marks: {collected_marks}")
    print(f"CGPA: {cgpa}")


# Main (User Input)
def main():
    students = []

    n = int(input("Enter number of students: "))
    max_marks = float(input("Enter maximum marks per subject (e.g., 100): "))

    # Closure created
    cgpa_func = cgpa_closure(max_marks)

    for i in range(n):
        print(f"\nEnter details for student {i+1}")
        name = input("Enter name: ")
        reg = input("Enter reg no: ")

        m = int(input("Enter number of subjects: "))
        marks = []

        for j in range(m):
            while True:
                try:
                    mark = float(input(f"Enter mark {j+1}: "))
                    if 0 <= mark <= max_marks:
                        marks.append(mark)
                        break
                    else:
                        print(f"Enter mark between 0 and {max_marks}")
                except:
                    print("Invalid input! Enter numeric value.")

        students.append({"name": name, "reg": reg, "marks": marks})

    print("\n=== Student Results ===")

    for student in students:
        process_student(student, cgpa_func)


if __name__ == "__main__":
    main()