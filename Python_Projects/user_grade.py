################################################################################

# Program Name: User grade and identity

# Author Name: Oryon J. Facey

# Date: 19 September 2024

# Description: Calculating the number of ducks in the Durham campus reservoir

###############################################################################

# Declarations:
# gives grade a blank value
grade = ""

# Input:
# User input variables
# Display message: “Please enter your first name.”

first_name = input("Please enter your first name.")

# Display message: “Please enter your last name.”

last_name = input("Please enter your last name.")

# Display message: “Please enter your age.”

age = input("Please enter your age.")

# Display message: “Please enter your test score.”

test_score = input("Please enter your test score.")

# creates a select statement to check if first_name is not an alphabetic character

if not first_name.isalpha():
    print("Sorry the values should all be alphabetic characters.")
else:

    # creates a select statement to check if last_name is an alphabetic character

    if not last_name.isalpha():
        print("Sorry the values should all be alphabetic characters.")
    else:

        # creates a select statement to check if age is a numeric value

        if not age.isnumeric():
            print("Sorry your age should be numeric values.")
        else:

            # creates a select statement to check if age is between 18 and 25

            if not (26 > int(age) > 17):
                print("Sorry your age is outside of the required parameters please choose a value between 18-25.")
            else:

                # creates a select statement to check if test_score is a numeric value

                if not test_score.isnumeric():
                    print("Sorry your test score should be numeric values.")
                else:

                    # creates an if statement to check if test is between 0 and 100
                    if not (0 <= int(test_score) <= 100):
                        print("Sorry your score is outside of the required parameters please choose a value between 0-100.")
                    else:

                        # creates an if statement to check if test is between 80 and 100

                        if 80 <= int(test_score) <=100:

                            # Assign grade to A

                            grade = "A"

                            # creates a select statement to check if test is between 60 and 79

                        elif 60 <= int(test_score) < 80:

                            # Assign grade to B

                            grade = "B"

                            # creates a select statement to check if test is between 50 and 59

                        elif 50 <= int(test_score) < 60:

                            # Assign grade to C

                            grade = "C"

                            # creates a select statement for the rest of the values for test
                        else:

                            # Assign grade to D

                            grade = "D"
                    # Display user's information
                    print(first_name + " " + last_name + " who is " + age + " years old, has achieved a grade of " + grade)