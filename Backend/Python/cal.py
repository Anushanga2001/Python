def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if(y==0):
        print("Cannot divide by zero")
    else:
        return x/y

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter choice(1/2/3/4/5):")

    if choice == '5':
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1':
        print(add(x,y))

    elif choice == '2':
        print(sub(x,y))
    
    elif choice == '3':
        print(mul(x,y))
    
    elif choice == '4':
        print(div(x,y))