import math

def circle_area(r):
    return 3.14 * r * r

def rect_area(a, b):
    return a * b

def triangle_area(b, h):
    return 0.5 * b * h

arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30]
arr3 = [5, 5, 5, 5, 5]

def get_info(arr):
    s = sum(arr)
    avg = s / len(arr)
    print("sum:", s)
    print("average:", avg)

print("circle area:", circle_area(5))
print("rectangle area:", rect_area(4, 6))
print("triangle area:", triangle_area(10, 2))

print("array 1")
get_info(arr1)
print("array 2")
get_info(arr2)
print("array 3")
get_info(arr3)