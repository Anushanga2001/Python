# Print the word
print("Hello world!!")

# Check the condition
if ( 5 > 2 ):
    print("Five is greater than two!")	
    if (3 > 2):
        print("Three is greater than two!")

x = "Anushanga"
print(x[4:])
y = "Kaluarachchi"
print(x +' '+ y)

# Function for calculate 2 numbers
def cal():
    x = 5
    y = 6
    z = x + y
    print(z)

cal()

# To get the type
x = 3.14
print(type(x))

# get the type of array
y= ("Anushanga", "Kaluarachchi")
print(type(y))

# sort the array
x = ("Anushanga", "Kaluarachchi")
print(x[0])

# Check if condition 
text = "Hello Anushanga, How are you?"
if "Helloo" in text:
    print("That's right !!!")
else:
    print("That's not write")

# Names
array = ["Anushanga", "Kaluarachchi", "Anujaya", "Chathura"]
print(len(array))

x = ['3', '1', '4', '5', '2']

# Adding additional element
x.append('6')

# remove element
x.remove('3')

# sorting means min to max
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] > x[j]:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
print(x)