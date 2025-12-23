s = input().strip()

a = s[0]
op = s[1]
b = s[2]
c = s[4]

if a == 'x':
    if op == '+':
        print(int(c) - int(b))
    else:
        print(int(c) + int(b))
elif b == 'x':
    if op == '+':
        print(int(c) - int(a))
    else:
        print(int(a) - int(c))
elif c == 'x':
    if op == '+':
        print(int(a) + int(b))
    else:
        print(int(a) - int(b))