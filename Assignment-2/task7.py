items = input().split()

counts = {}
for x in items:
    if x in counts:
        counts[x] = counts[x] + 1
    else:
        counts[x] = 1

print("Purchase frequency:")
for x in counts:
    print(x + ": " + str(counts[x]))

most_pop = items[0]
for x in counts:
    if counts[x] > counts[most_pop]:
        most_pop = x
print("Most popular item: " + most_pop)

print("Purchased once:", end=" ")
for x in counts:
    if counts[x] == 1:
        print(x, end=" ")
print()

print("Sorted by frequency:")
copy_counts = counts.copy()
while len(copy_counts) > 0:
    current_max_key = ""
    current_max_val = -1
    for x in copy_counts:
        if copy_counts[x] > current_max_val:
            current_max_val = copy_counts[x]
            current_max_key = x
    print(current_max_key + " " + str(current_max_val))
    del copy_counts[current_max_key]