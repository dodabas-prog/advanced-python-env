import math

def get_triangle_area(a):
    return (math.sqrt(3) / 4) * a * a

def get_hexagon_area(side):
    return 6 * get_triangle_area(side)

hex_side = float(input("enter hexagon side: "))
print("hexagon A is:", get_hexagon_area(hex_side))

print("rectangle 1:")
w1 = float(input("enter width: "))
h1 = float(input("enter height: "))
print("A:", w1 * h1)

print("rectangle 2:")
w2 = float(input("enter width: "))
h2 = float(input("enter height: "))
print("A:", w2 * h2)

print("rectangle 3:")
w3 = float(input("enter width: "))
h3 = float(input("enter height: "))
print("A:", w3 * h3)