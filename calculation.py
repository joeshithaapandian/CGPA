def cgpa_calculator():
    total_credits = 0
    total_grade_points = 0
    grade_points = {'A': 10, 'B': 8, 'C': 6, 'D': 4, 'E': 2, 'F': 0}

    num_courses = int(input("Enter the number of courses: "))

    for _ in range(num_courses):
        grade = input("Enter the grade (A/B/C/D/E/F): ").upper()
        credits = int(input("Enter the number of credits for this course: "))
        
        total_credits += credits
        total_grade_points += grade_points[grade] * credits

    if total_credits == 0:
        print("No courses entered.")
    else:
        cgpa = total_grade_points / total_credits
        print(f"Your CGPA is: {cgpa:.2f}")

cgpa_calculator()
