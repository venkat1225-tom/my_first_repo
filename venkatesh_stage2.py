num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        exit()
    else:
        result = num1 / num2

else:
    print("Invalid operator")
    exit()

print("Result =", result)

# Result check
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")

