# Simple Python Calculator
print("Simple Calculator")
print("-----------------")

# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"2

# Display result
print(f"\nResult: {num1} {operator} {num2} = {result}")