def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Oops! That’s not a valid number. Please try again.")

def get_operation(prompt):
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input(prompt)
        if op in valid_operations:
            return op
        else:
            print("Invalid operation. Please enter one of (+, -, *, /).")

# Main program
num1 = get_number("Please enter the first number: ")
num2 = get_number("Please enter the second number: ")
operation = get_operation("Please enter the operation you would like (+, -, *, /): ")

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

print(f"The result of {num1} {operation} {num2} is: {result}")