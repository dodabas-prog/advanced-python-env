def get_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

# part 1
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

num = a * d - b * c
den = b * d

common = get_gcd(abs(num), den)

print(num // common, "/", den // common)

# part 2
n = int(input("enter number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()