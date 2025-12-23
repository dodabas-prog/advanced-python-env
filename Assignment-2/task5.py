n = int(input())
letters = "ABCEHKMOPTXY"

for i in range(n):
    s = input()
    
    if len(s) == 6:
        if (s[0] in letters and 
            s[1:4].isdigit() and 
            s[4] in letters and 
            s[5] in letters):
            print("Yes")
        else:
            print("No")
    else:
        print("No")