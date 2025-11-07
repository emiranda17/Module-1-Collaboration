# Name: Emmanuel Miranda
# File Name: Emmanuel_Miranda-student_gpa_checker.py
# Description: This app accepts student names and GPAs and checks if the student qualifies for the Dean's List (GPA >= 3.5) or the Honor Roll (GPA >= 3.25).
while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        break
    first_name = input("Enter student's first name: ")
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid input for GPA. Please enter a numeric value.")
        continue
    
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")
