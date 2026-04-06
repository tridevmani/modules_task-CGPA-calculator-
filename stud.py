def get_student_data():
    semesters = int(input("Enter number of semesters: "))
    all_sem_data = []

    for sem in range(1, semesters + 1):
        print(f"\n--- Semester {sem} ---")
        
        subjects = int(input("Enter number of subjects: "))
        sem_data = []

        for i in range(subjects):
            print(f"\nSubject {i+1}:")
            
            name = input("Enter subject name: ")

            # Credit validation
            while True:
                credit = float(input("Enter credit: "))
                if credit > 0:
                    break
                else:
                    print("Credit must be positive!")

            # Grade validation
            while True:
                grade = float(input("Enter grade (0-10): "))
                if 0 <= grade <= 10:
                    break
                else:
                    print("Invalid grade! Enter between 0-10")

            sem_data.append({
                "subject": name,
                "credit": credit,
                "grade": grade
            })

        all_sem_data.append(sem_data)

    return all_sem_data