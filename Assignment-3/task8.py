# part 1
n = int(input("enter n: "))

for num in range(1, n + 1):
    s_num = str(num)
    check = True
    
    for digit_char in s_num:
        digit = int(digit_char)
        if digit == 0 or num % digit != 0:
            check = False
            break
            
    if check:
        print(num, end=" ")
print()

# part 2
def swap_elements(arr):
    if len(arr) > 1:
        temp = arr[0]
        arr[0] = arr[-1]
        arr[-1] = temp

m = int(input("enter array length: "))
data = input("enter elements: ").split()
a = [int(x) for x in data]
a = a[:m]
print("original:", a)

swap_elements(a)
print("resulting:", a)