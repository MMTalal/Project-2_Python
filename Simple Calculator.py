# Print a title for the calculator
print("Simple Calculator")

# Get the first number from the user and convert it to an integer
num1 = float(input("Please input your first number: ").strip())

# Get the operation from the user and remove any leading/trailing whitespace
operation = input("Choose operation ( + , - , * , / , % , ** , // ) :- ").strip()

# Get the second number from the user and convert it to an integer
num2 = float(input("Please input your second number: ").strip())

# Check the chosen operation and perform the corresponding calculation
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    # Check if the user is trying to divide by zero, and display an error message if so
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(num1 / num2)
elif operation == "%":
    print(num1 % num2)
elif operation == "**":
    print(num1 ** num2)
elif operation == "//":
    print(num1 // num2)
else:
    # Display an error message for an invalid operation
    print("Error: Invalid operation. Please choose from +, -, , /, %, *, //.")