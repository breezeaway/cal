# basic cal functions
def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def times(x, y):
    return x * y


def divide(x, y):
    return x / y


# Terminal
while True:
    print("Select Operations")
    print("Add(1)")
    print("Minus(2)")
    print("Multiply(3)")
    print("Divide(4)")
    option = input()
    if option == "1":
        break
    elif option == "2":
        break
    elif option == "3":
        break
    elif option == "4":
        break
    else:
        print("Please enter a valid option")
print("You have chosen " + option)
print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
if option == "1":
    print(add(a,b))
elif option == "2":
    print(minus(a,b))
elif option == "3":
    print(times(a,b))
else:
    print(divide(a,b))
