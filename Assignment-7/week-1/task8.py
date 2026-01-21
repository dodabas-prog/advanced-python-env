input_word = input("Enter a word: ")

try:
    Count = int(input("Enter a number: "))
except ValueError:
    print("Invalid number input.")
    exit()

for character in input_word:
    line = ""
    for k in range(Count):
        line += character
    print(line)