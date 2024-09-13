x = int(input("Enter the amount:"))

Amount_5000 = Amount_1000 = Amount_500 = Amount_100 = Amount_50 = Amount_20 = Amount_10 = Amount_5 = Amount_2 = 0

if x > 5000:
    Amont_5000 = int(x/5000)
    x = x % 5000

if x > 1000:
    Amount_1000 = int(x/1000)
    x = x % 1000

if x > 500:
    Amount_500 = int(x/500)
    x = x % 500

if x > 100:
    Amount_100 = int(x/100)
    x = x % 100

if x > 50:
    Amount_50 = int(x/50)
    x = x % 50

if x > 20:
    Amount_20 = int(x/20)
    x = x % 20

if x > 10:
    Amount_10 = int(x/10)
    x = x % 10

if x > 5:
    Amount_5 = int(x/5)
    x = x % 5

if x > 2:
    Amount_2 = int(x/2)
    x = x % 2

print(f"5000 : {Amont_5000}")
print(f"1000 : {Amount_1000}")
print(f"500 : {Amount_500}")
print(f"100 : {Amount_100}")
print(f"50 : {Amount_50}")
print(f"20 : {Amount_20}")
print(f"10 : {Amount_10}")
print(f"5 : {Amount_5}")
print(f"2 : {Amount_2}")