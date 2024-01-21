# Create a function called grade_converter that takes a numerical grade as an argument and returns the corresponding letter grade (A, B, C, D, F) based on the standard grading scale.

def grade_converter(grade):
    if grade > 100 or grade < 0:
        print("Invalid response")
    else:
        if grade >= 90:
            return 'A'
        elif grade < 90 and grade >=80:
            return 'B'
        elif grade < 80 and grade >=70:
            return 'C'
        elif grade < 70 and grade >=50:
            return 'D'
        else:
            return 'F'

percent = int(input("Enter your grade percentage: "))
result = grade_converter(percent)
print("Grade is ",result)