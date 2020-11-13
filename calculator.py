# a simple calculator by sugan
def add(x, y):
    """this function add two
    numbers"""
    return x+y


def subtract(x, y):
    """this function subtract
    two numbers"""
    return x-y


def multiply(x, y):
    """this function multiply
    two numbers"""
    return x*y


def division(x, y):
    """this function divide
    two numbers"""
    return x/y


print("select operations.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("Enter Q to quit")


while True:
    choice = int(input('enter your choice(1/2/3/4):'))

    num1 = int(input("enter your first number:"))
    num2 = int(input("enter your second number:"))

    if choice == 1:
        for i in range(1, 2):
            print(num1, "+", num2, '=', add(num1, num2))
    elif choice == 2:
        for i in range(1, 2):
            print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == 3:
        for i in range(1, 2):
            print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == 4:
        for i in range(1, 2):
            print(num1, "/", num2, "=", division(num1, num2))
    else:
        break
