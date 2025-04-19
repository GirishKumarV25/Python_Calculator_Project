def calculator():
    print("Simple CALCULATOR project made by me during INGRADE session assignment")
    print("Calculator for 2 numbers")

    # Get user inputs and store it in variables num1 & num2 (can be used INT as well, since division may have decimal value we are using FLOAT)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display choice for user selection
    print("Enter your choice for mode of operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
       
    # Get input choice from user
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        print("Addition is :", num1 + num2)
    elif choice == '2':
        print("Subtraction is :", num1 - num2)
    elif choice == '3':
        print("Multiplication is :", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Divison is :", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid input")

# Run the calculator
calculator()