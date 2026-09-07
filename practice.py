#even or odd?
print("even or odd?")
x = None
while x is None:
    try:
        x = int(input(" enter an integer: "))
    except ValueError:
        print("use a valid integer")

if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

#password gatekeeper
print("password gatekeeper")
password = input("enter password: ")
if len(password) >= 8:
    print("password accepted")
else:
    print("password too short") 

#movie ticket price
print("movie ticket price")
age = None
while age is None:
    try:
        age = int(input("enter your age: "))
    except ValueError:
        print("use a valid integer")
if age in range(0, 12):
    print("ticket is ₱180")
elif age in range(13, 64):
    print("ticket is ₱250")
else:
    print("ticket is ₱200")

#leap year
print("leap year")
year = None
while year is None:
    try:
        year = int(input("enter a year: "))
    except ValueError:
        print("use a valid integer")

if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
