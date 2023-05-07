# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Assignment 4 - Simple Calculator

# import pyfiglet
import pyfiglet

# import termcolor
from termcolor import colored
from termcolor import colored, cprint

# import rich 
from rich.theme import Theme
from rich.console import Console

# generate theme
theme_calc = Theme({"error" : "bold red", "thank" : "bold green", "ans": "bold cyan"})
console_calc = Console(theme = theme_calc)

# use while loop
while True:
       
    # use try
    try:
        # menu
        print("_" * 80)
        title = pyfiglet.figlet_format ("MATH OPERATIONS", font = "cricket")
        print("\n" + colored((title.center(55)), "blue"))
        console_calc.print("\n~ ADDITION", style = "thank")
        console_calc.print("~ SUBTRACTION", style = "thank")
        console_calc.print("~ MULTIPLICATION", style = "thank")
        console_calc.print("~ DIVISION", style = "thank")
        print("_" * 60)

        while True:
            # ask user choose between four math operations 
            user_operation = input(colored("\nEnter what math operation you want to use: ", "light_yellow")).upper()

            if user_operation != "ADDITION" and user_operation != "SUBTRACTION" and user_operation != "MULTIPLICATION" and user_operation != "DIVISION":
                console_calc.print("\nEnter only the four math operations.\n(check your spelling)", style = "error")
                print("_" * 60)

            else: 
                # Ask user for two numbers
                num_1 = int(input("\n" + colored("--Enter first number: ", "yellow")))
                num_2 = int(input(colored("--Enter second number: ", "yellow")))
                
                # perform calculations
                # display result if there are no errors
                if user_operation == "ADDITION":
                    print("_" * 60)
                    print(colored("Calculating......", "light_cyan" ))
                    cprint("\n" + colored(" The sum of your first and second number is " + str(num_1 + num_2) + ". "),"light_magenta", attrs = ["bold", "reverse"])
                    print("_" * 60)

                elif user_operation == "SUBTRACTION":
                    print("_" * 60)
                    print(colored("Calculating......", "light_cyan" ))
                    cprint("\n" + colored(" The difference of your first and second number is " + str(num_1 - num_2) + ". "),"light_magenta", attrs = ["bold", "reverse"]) 
                    print("_" * 60)

                elif user_operation == "MULTIPLICATION":
                    print("_" * 60)
                    print(colored("Calculating......", "light_cyan" ))
                    cprint("\n" + colored(" The product of your first and second number is " + str(num_1 * num_2) + ". "),"light_magenta", attrs = ["bold", "reverse"])
                    print("_" * 60)

                elif user_operation == "DIVISION":
                    print("_" * 60)
                    print(colored("Calculating......", "light_cyan" ))
                    cprint("\n" + colored(" The quotient of your first and second number is " + str(num_1 / num_2) + ". "),"light_magenta", attrs = ["bold", "reverse"])
                    print("_" * 60)
                break

    # use exeption to capture errors
    except ZeroDivisionError:
        console_calc.print("\n❗ Invalid. You are dividing by zero.", style = "error")
        print("_" * 60)

    except ValueError:
        console_calc.print("\n❗ Invalid value. Enter integers only", style = "error")
        print("_" * 60)
    
    finally:
        # ask user if they want to repeat
        user_repeat = input("\nDo you want to repeat? yes/no: ").lower()

        # if yes loop from the start
        if user_repeat == "yes":
            print()
        # if no, exit the program 
        elif user_repeat == "no":
            thanks = pyfiglet.figlet_format("THANK YOU!", font = "linux")
            print("\n" + colored((thanks),"green", attrs = ["bold"]) + "\n")
            exit()
        # else if there are other input/s
        elif user_repeat != "yes" and user_repeat != "no":
            print("\n" + colored("Invalid input.\n(Check your spelling)", "red"))
            print("_" * 60)
            user_repeat = input("\nDo you want to repeat? yes/no: ").lower()
            print()