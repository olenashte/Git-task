def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def multiply(a, b):
    return a * b
operation = input("Enter operation (+,*, / or -): ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#Add elif
if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
elif operation == "/":
    print(divide(num1, num2))
#elif operation == "*":
    #print(multiply(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
else:
    print("Unknown operation")