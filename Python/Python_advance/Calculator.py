# python code for calculator

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def sub(x, y):
    return x - y

# Function for multiplication
def mul(x, y):
    return x * y

# Function for division
def div(x, y):
    return x / y

# Take input from user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", sub(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", mul(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", div(num1,num2))
else:
    print("Invalid Input")