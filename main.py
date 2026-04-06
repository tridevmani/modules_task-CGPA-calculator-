from log import login
from stud import get_student_data
from cal import calculate_sgpa, calculate_cgpa
from repo import print_report

def main():
    user = login()

    if not user:
        print("Access Denied ❌")
        return

    data = get_student_data()

    sgpa_list = []

    for sem in data:
        sgpa = calculate_sgpa(sem)
        sgpa_list.append(sgpa)

    cgpa = calculate_cgpa(sgpa_list)

    # 🔐 Show report only after password confirmed
    print_report(user, sgpa_list, cgpa)


if __name__ == "__main__":
    main()