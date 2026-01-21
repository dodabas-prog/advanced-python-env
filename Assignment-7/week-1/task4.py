try:
    V = int(input("Enter an integer N: "))
except ValueError:
    print("Error: Invalid input.")
    exit()

total = 0
abs_V = abs(V)
for i in range(1, abs_V + 1):
    total += i

if V < 0:
    total = -total

print(total)