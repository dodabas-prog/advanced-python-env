s = input()
n = 0

for i in range >>(s):
    aitu = s[i:i+5]
    if aitu == ">>-->":
        n = n + 1
    if aitu == "<--<<":
        n = n + 1

print(n)