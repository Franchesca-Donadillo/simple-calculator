# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Assignment 4 - Simple Calculator

# import rich 
from rich.theme import Theme
from rich.console import Console

# generate theme
theme_calc = Theme({})
console_calc = Console(theme = theme_calc)

# use while loop
while True:
       
    # use try
    try:
        # menu
        print("_" * 60)
        print("\n" + "MATH OPERATIONS".center(55))
        print("\n~ ADDITION")
        print("~ SUBTRACTION")
        print("~ MULTIPLICATION")
        print("~ DIVISION")
        print("_" * 60)
        while True:
            # ask user choose between four math operations 
            user_operation = input("\nEnter what math operation you want to use: ").upper()

            if user_operation != "ADDITION" and user_operation != "SUBTRACTION" and user_operation != "MULTIPLICATION" and user_operation != "DIVISION":
                print("\nEnter only the four math operations.\n(check your spelling)")
                print("_" * 60)

            else: 
                # Ask user for two numbers
                num_1 = int(input("\nEnter first number: "))
                num_2 = int(input("Enter second number: "))

                # perform calculations
                # display result if there are no errors
                if user_operation == "ADDITION":
                    print("\nThe sum of your first and second number is " + str(num_1 + num_2))
                    print("_" * 60)

                elif user_operation == "SUBTRACTION":
                    print("\nThe difference of your first and second number is " + str(num_1 - num_2)) 
                    print("_" * 60)

                elif user_operation == "MULTIPLICATION":
                    print("\nThe product of your first and second number is " + str(num_1 * num_2))
                    print("_" * 60)

                elif user_operation == "DIVISION":
                    print("\nThe quotient of your first and second number is " + str(num_1 / num_2))
                    print("_" * 60)
                break

    # use exeption to capture errors
    except ZeroDivisionError:
        print("\nInvalid. You are dividing by zero.")

    except ValueError:
        print("\nInvalid value. Enter integers only")
    
    finally:
        # ask user if they want to repeat
        user_repeat = input("\nDo you want to repeat? yes/no: ").lower()

        # if yes loop from the start
        if user_repeat == "yes":
            print()
        # if no, exit the program 
        elif user_repeat == "no":
            print("\nThank You!\n")
            exit()
