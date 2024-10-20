def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Added multiply
def multiply(a, b):
    return a * b

operation = input("Enter operation (+,* or -): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#Add elif
if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
#elif operation == "*":
    #print(multiply(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
else:
    print("Unknown operation")