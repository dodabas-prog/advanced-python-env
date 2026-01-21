import math

# part 1 
def right_triangle_area(x, y):
    return 0.5 * x * y

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

x = float(input("enter x: "))
y = float(input("enter y: "))
z = float(input("enter z: "))
t = float(input("enter t: "))

area1 = right_triangle_area(x, y)

diag = math.sqrt(x**2 + y**2)
area2 = triangle_area(z, t, diag)

total_area = area1 + area2
print("area:", total_area)

# part 2
num = int(input("enter number: "))
octal_code = format(num, '010o')
print(octal_code)