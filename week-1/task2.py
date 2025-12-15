salaries_raw = input("Enter the salaries (e.g., 100 500 1000): ")

try:
    s_list = [int(s) for s in salaries_raw.split()]
except ValueError:
    print("Error: Invalid input.")
    exit()

if len(s_list) == 0:
    print("Error: No salaries entered.")
    exit()

max_s = s_list[0]
min_s = s_list[0]

for s in s_list:
    if s > max_s:
        max_s = s
    if s < min_s:
        min_s = s

print(max_s - min_s)