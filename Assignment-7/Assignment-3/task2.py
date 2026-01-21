import math

def triangle_area(side):
    return (side**2 * math.sqrt(3)) / 4

# Part 1
a = float(input("Enter hexagon side: "))
hexagon_area = 6 * triangle_area(a)
print(hexagon_area)

# Part 2
for i in range(3):
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    rect_area = side1 * side2
    print(rect_area)