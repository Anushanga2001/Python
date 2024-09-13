x = int(input("Enter number for the pattern : "))

for i in range(x):
    print("*" * (i + 1))

for i in range (x, 0, -1):
    print("*" * i)

y = input("Enter your name : ")
for i in y:
    if i in ['a', 'e', 'i', 'o', 'u']:
       y = y.replace(i, "")
    else :
       print(i, end="")

Z = int(input("\nEnter number : "))

i=1
while i<=Z:
    print("*" * i)
    i+=1
