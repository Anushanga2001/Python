# Number of rows
num_rows = int(input("Enter the number of rows: "))

# Right-angled triangle pattern
for i in range(1, num_rows + 1):
    print('*' * i)

for i in range(num_rows, 0, -1):
    print('*' * i)

i = 1
while i < 10:
    print("*" * i)
    i += 1