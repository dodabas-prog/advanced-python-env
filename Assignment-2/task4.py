data = input().split()
n = int(data[0])
m = int(data[1])
s = input()

all_words = set()

for i in range(n - m + 1):
    part = s[i:i+m]
    all_words.add(part)

print(len(all_words))