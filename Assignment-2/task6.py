def all_eq(lst):
    if not lst:
        return []
    
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    res = []
    for s in lst:
        new_s = s
        while len(new_s) < max_len:
            new_s = new_s + "_"
        res.append(new_s)
        
    return res

words = input().split()
print(all_eq(words))