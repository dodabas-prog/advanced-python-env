try:
    v1 = float(input("First number: "))
    op = input("Operation: ")
    v2 = float(input("Second number: "))
except ValueError:
    print("Invalid number input.")
    exit()

R = None

if op == '+':
    R = v1 + v2
elif op == '-':
    R = v1 - v2
elif op == '*':
    R = v1 * v2
elif op == '/':
    if v2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    else:
        R = v1 / v2
else:
    print("Invalid operation.")
    exit()

print(R)