s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

variants = []
for i in range(m):
    v = s2[i:] + s2[:i]
    variants.append(v)
ans = 0
for i in range(n - m + 1):
    part = s1[i:i+m]
    if part in variants:
        ans = ans + 1

print(ans)