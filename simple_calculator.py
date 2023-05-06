# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Assignment 4 - Simple Calculator

# ask user to choose between four math oparations
try:
    user_operation = input("Enter what math operation you want to use: ").upper()
    # Ask user for two numbers
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))

    # perform calculations
    # display result if there are no errors
    if user_operation == "ADDITION":
        print("The sum of your first and second number is " + num_1 + num_2)

    elif user_operation == "SUBTRACTION":
        print("The difference of your first and second number is " + num_1 - num_2) 

    elif user_operation == "MULTIPLICATION":
        print("The product of your first and second number is " + num_1 * num_2)

    elif user_operation == "DIVISION":
        print("The quotient of your first and second number is " + num_1 / num_2)

# use exeption to capture errors
# ask user if they want to repeat
# use while loop
# if yes loop from the start
# if no, exit the program 
