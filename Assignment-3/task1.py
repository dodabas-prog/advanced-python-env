import math

# part 1
radius = float(input("enter circle radius: "))
circle_area = 3.14 * radius * radius
print("circle area:", circle_area)

width = float(input("enter rectangle width: "))
height = float(input("enter rectangle height: "))
rect_area = width * height
print("rectangle area:", rect_area)

base = float(input("enter triangle base: "))
theight = float(input("enter triangle height: "))
tri_area = 0.5 * base * theight
print("triangle area:", tri_area)

# part 2
for i in range(3):
    print("processing array", i + 1)
    user_input = input("enter integers: ").split()
    
    numbers = []
    for val in user_input:
        numbers.append(int(val))
    
    if len(numbers) > 15:
        numbers = numbers[:15]
    
    total_sum = sum(numbers)
    if len(numbers) > 0:
        mean = total_sum / len(numbers)
    else:
        mean = 0
        
    print("sum:", total_sum)
    print("mean:", mean)