# even or odd?
x = None # sets the value of x to None
while x is None: # loops until x is not None AND is an integer
    try:
        x = int(input(" enter an integer: "))
    except ValueError:
        print("use a valid integer")

if x % 2 == 0: # checks if x is divisible by 2
    print(f"{x} is even")
else:
    print(f"{x} is odd")