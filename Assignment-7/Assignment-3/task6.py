import math

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# part 1
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

gcd_val = get_gcd(num1, num2)
lcm_val = (num1 * num2) // gcd_val

print("gcd:", gcd_val)
print("lcm:", lcm_val)

# part 2
a = float(input("side a: "))
b = float(input("side b: "))
c = float(input("side c: "))
d = float(input("side d: "))
diag = float(input("diagonal: "))

s1 = (a + b + diag) / 2
area1 = math.sqrt(s1 * (s1 - a) * (s1 - b) * (s1 - diag))

s2 = (c + d + diag) / 2
area2 = math.sqrt(s2 * (s2 - c) * (s2 - d) * (s2 - diag))

total_area = area1 + area2
print("area:", total_area)