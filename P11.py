x, op, y = input("Enter x op y (+ - * / ^): ").split()

try:
    x = float(x)
    y = float(y)
except ValueError:
    print("Invalid op")
    exit()

if op not in ("+", "-", "*", "/", "^"):
    print("Invalid op")
elif y == 0 and op == "/":
    print("Invalid op")
else:
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    elif op == "^":
        result = x ** y

    if op in ("/", "^"):
        print(f"{result:.4f}")
    else:
        print(f"{result:.2f}")

#Finished