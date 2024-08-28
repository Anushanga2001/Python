def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "Error"
    else:
        return x/y

while True:
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for exit")

    choice = int(input("Enter your choice: "))

    if (choice == 5):
        exit()

    if (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

    if choice == 1:
        print(add(x,y))
    elif choice == 2:
        print(sub(x,y))
    elif choice == 3:
        print(mul(x,y))
    elif choice == 4:
        print(div(x,y))
    else:
        print("Invalid Input")