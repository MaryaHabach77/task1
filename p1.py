#This code defines a function called assessment_grade that prompts the user to input a numerical mark. It then evaluates
#the mark and returns a corresponding letter grade based on certain conditions. The grading scale ranges from 'A+' for
#marks of 90 or above, down to 'F' for marks below 50. The code includes error handling to ensure the user enters a valid
#number, and finally, it calls the function, assigns the result to a variable grade_thisyear, and prints the calculated
#grade.


def assessment_grade():
    while True:
        try:
            # Prompt the user to input the mark
            mark = float(input("Enter the mark: "))
            # if the mark is bigger or equal to 90
            if mark >= 90:
                return 'A+'
            # Check if the mark is bigger or equal to 85
            elif mark >= 85:
                return 'A'
            # Check if the mark is bigger or equal to 80
            elif mark >= 80:
                return 'B+'
            # Check if the mark is bigger equal to 75
            elif mark >= 75:
                return 'B'
            # Check if the mark is bigger or equal to 70
            elif mark >= 70:
                return 'C+'
            # Check if the mark is bigger or equal to 65
            elif mark >= 65:
                return 'C'
            # Check if the mark is bigger or equal to 60
            elif mark >= 60:
                return 'D+'
            # Check if the mark is bigger or equal to 50
            elif mark >= 50:
                return 'D'
            # If none of the above conditions are met, return 'F'
            else:
                return 'F'
        except ValueError:
            print("Error, Please enter a valid number:")

# Call the function and display the result
grade_thisyear = assessment_grade()
print(f"The grade is: {grade_thisyear}")