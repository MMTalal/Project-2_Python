# Simple Calculator

This is a simple command-line calculator program written in Python. It allows the user to perform basic arithmetic operations such as addition, subtraction, multiplication, division, modulo, exponentiation, and integer division.

## Usage

To use the calculator, simply run the `Simple Calculator.py` script. The program will prompt the user to input the first number, choose an operation, and input the second number. The result of the calculation will be displayed.

```
$ python calculator.py
Simple Calculator
Please input your first number: 10
Choose operation ( + , - , * , / , % , ** , // ) :- *
Please input your second number: 5
50.0
```

If the user tries to divide by zero, the program will display an error message.

```
$ python calculator.py
Simple Calculator
Please input your first number: 10
Choose operation ( + , - , * , / , % , ** , // ) :- /
Please input your second number: 0
Error: Cannot divide by zero.
```

If the user enters an invalid operation, the program will display an error message.

```
$ python calculator.py
Simple Calculator
Please input your first number: 10
Choose operation ( + , - , * , / , % , ** , // ) :- ^
Error: Invalid operation. Please choose from +, -, , /, %, *, //.
```

## Features

- Supports basic arithmetic operations: addition, subtraction, multiplication, division, modulo, exponentiation, and integer division.
- Handles division by zero errors.
- Validates user input to ensure valid numbers and operations are entered.

## Future Improvements

- Add support for more advanced operations such as trigonometric functions, logarithms, and more.
- Implement a history feature to allow users to view and recall previous calculations.
- Provide a graphical user interface (GUI) for the calculator.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/MMTalal/Project-2_Python).
