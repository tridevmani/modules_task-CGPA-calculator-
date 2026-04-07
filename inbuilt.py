
import math
import random
import statistics
import datetime

def analyze_marks(marks):
    print("\n--- Marks Analysis ---")
    print("Marks:", marks)
    print("Total:", sum(marks))
    print("Average:", statistics.mean(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

    # Using math module
    print("Rounded Average:", math.ceil(statistics.mean(marks)))

def generate_student_id(name):
    # Using random + string logic
    unique_id = name[:3].upper() + str(random.randint(1000, 9999))
    return unique_id

def show_time():
    now = datetime.datetime.now()
    print("\nSystem Time:", now.strftime("%d-%m-%Y %H:%M:%S"))

def main():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter mark : ").split()))

    student_id = generate_student_id(name)
    print("\nGenerated Student ID:", student_id)

    analyze_marks(marks)
    show_time()

if __name__ == "__main__":
    main()