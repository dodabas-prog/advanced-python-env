import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# part 1
a1 = float(input("first triangle leg a: "))
b1 = float(input("first triangle leg b: "))
h1 = calculate_hypotenuse(a1, b1)

a2 = float(input("second triangle leg a: "))
b2 = float(input("second triangle leg b: "))
h2 = calculate_hypotenuse(a2, b2)

print(h1)
print(h2)

if h1 > h2:
    print("first hypotenuse is greater")
elif h2 > h1:
    print("second hypotenuse is greater")
else:
    print("equal")

# part 2
text = input("string: ")
words = text.split()
new_words = []

for word in words:
    sorted_letters = sorted(word)
    new_word = "".join(sorted_letters)
    new_words.append(new_word)

print(" ".join(new_words))