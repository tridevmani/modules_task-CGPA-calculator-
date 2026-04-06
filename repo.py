def print_report(usn, sgpa_list, cgpa):
    print("\n" + "="*40)
    print("🎓 STUDENT RESULT REPORT")
    print("="*40)
    
    print(f"USN: {usn}")
    print("-"*40)

    for i, sgpa in enumerate(sgpa_list, start=1):
        print(f"Semester {i} SGPA : {round(sgpa, 2)}")

    print("-"*40)
    print(f"Final CGPA       : {round(cgpa, 2)}")

    # Performance
    if cgpa > 9:
        perf = "Excellent 🏆"
    elif cgpa > 8:
        perf = "Very Good 👍"
    elif cgpa > 7:
        perf = "Good 🙂"
    else:
        perf = "Needs Improvement ⚠️"

    print(f"Performance      : {perf}")
    print("="*40)