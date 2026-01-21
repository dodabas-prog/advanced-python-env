import math

def get_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

# part 1
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

num = a * d
den = b * c

common = get_gcd(num, den)

print(num // common, "/", den // common)

# part 2
def check_point(px, py, xa, ya, r):
    distance_sq = (px - xa)**2 + (py - ya)**2
    if distance_sq <= r**2:
        return True
    return False

xa = float(input("enter xa: "))
ya = float(input("enter ya: "))
radius = float(input("enter R: "))

points_count = 0

p1 = float(input("p1: "))
p2 = float(input("p2: "))
if check_point(p1, p2, xa, ya, radius):
    points_count += 1

f1 = float(input("f1: "))
f2 = float(input("f2: "))
if check_point(f1, f2, xa, ya, radius):
    points_count += 1

l1 = float(input("l1: "))
l2 = float(input("l2: "))
if check_point(l1, l2, xa, ya, radius):
    points_count += 1

print(points_count)