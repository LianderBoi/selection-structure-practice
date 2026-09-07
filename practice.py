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