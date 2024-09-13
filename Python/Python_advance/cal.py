def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        print("Can't divide by zero")
    else:
        return x/y
    
print ("Select operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print("4.Divide")

def num(x, y):
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

Enter = int(input("Enter choice(1/2/3/4): "))
if (Enter == 5):
    print("Invalid input")
    exit()
elif (Enter == 1):
    print(add(x,y))
elif (Enter == 2):
    print(sub(x,y))
elif (Enter == 3):
    print(mul(x,y))
elif (Enter == 4):
    print(div(x,y))