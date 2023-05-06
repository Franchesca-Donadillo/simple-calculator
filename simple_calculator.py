# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Assignment 4 - Simple Calculator

# use while loop
while True:

    # ask user to choose between four math oparations
    # use try
    try:
        user_operation = input("Enter what math operation you want to use: ").upper()
        # Ask user for two numbers
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))

        # perform calculations
        # display result if there are no errors
        if user_operation == "ADDITION":
            print("The sum of your first and second number is " + str(num_1 + num_2))

        elif user_operation == "SUBTRACTION":
            print("The difference of your first and second number is " + str(num_1 - num_2)) 

        elif user_operation == "MULTIPLICATION":
            print("The product of your first and second number is " + str(num_1 * num_2))

        elif user_operation == "DIVISION":
            print("The quotient of your first and second number is " + (num_1 / num_2))

    # use exeption to capture errors
    except ZeroDivisionError:
        print("Invalid. You are dividing by zero.")

    except ValueError:
        print("Invalid value. Enter integers only")

    # ask user if they want to repeat
    user_repeat = input("Do you want to repeat? yes/no: ").lower()

    # if yes loop from the start
    if user_repeat == "yes":
        print()
    # if no, exit the program 
    elif user_repeat == "no":
        print("Tank You!")
        exit()
