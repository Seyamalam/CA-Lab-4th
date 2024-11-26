def calculate_cgpa(grades, credits):
    total_points = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_points / total_credits


subjects = int(input("Enter the number of subjects: "))
grades = []
credits = []

for i in range(subjects):
    grade = float(input(f"Enter grade for subject {i + 1}: "))
    credit = int(input(f"Enter credit for subject {i + 1}: "))
    grades.append(grade)
    credits.append(credit)

cgpa = calculate_cgpa(grades, credits)
print(f"The calculated CGPA is: {cgpa:.2f}")
