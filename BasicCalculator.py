def simple_calculator():
    print("Welcome to the Simple Calculator!\n")

    try:
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Get the operation
        print("Choose an operation: +  -  *  /")
        operation = input("Enter the operation: ")

        # Perform calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose from +, -, *, /.")
            return

        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    simple_calculator()