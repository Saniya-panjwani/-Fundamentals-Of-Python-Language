# Assessment:  Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.

def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

calculator()
