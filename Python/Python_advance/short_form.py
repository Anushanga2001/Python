# Word splitting
def short(sentence):
    txt = sentence.split()
    short_form = ""
    for i in txt:
        short_form = short_form + i[0]
    print(short_form)

txt = input("Enter the sentence: ")
short(txt)

def number():
    Y = int(input("Enter the number: "))
    if (Y >10):
        print("This is a bigger number")
    elif (Y >5):
        print("This is a little bit bigger number")
    else:
        print("This is a smaller number")

number()