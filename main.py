# Simple Python Calculator

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
operation = input("Please enter the operation you would like (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."

print(f"The result of {num1} {operation} {num2} is: {result}")
