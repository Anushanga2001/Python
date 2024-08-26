
while True:	
    try:
        x = int(input("Enter the number of elements: "))
        if x >= 10:
            print("This is a bigger value")
        elif x >= 5:
            print("This is a little bit bigger value")
        else:
            print("This is a smaller value")
    except ValueError:
        print("Please enter a valid integer.")