def calculate_sgpa(sem_data):
    total_points = 0
    total_credits = 0

    for sub in sem_data:
        total_points += sub["grade"] * sub["credit"]
        total_credits += sub["credit"]

    return total_points / total_credits if total_credits != 0 else 0


def calculate_cgpa(sgpa_list):
    return sum(sgpa_list) / len(sgpa_list)