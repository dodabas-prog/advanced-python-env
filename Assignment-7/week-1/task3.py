try:
    N = float(input("Enter a real number A (e.g., 12.34): "))
except ValueError:
    print("Error: Invalid input.")
    exit()

int_part = int(N)
frac_part = N - int_part

new_int = round(frac_part * 100)
new_frac = int_part / 100.0

final_result = new_int + new_frac

print(final_result)