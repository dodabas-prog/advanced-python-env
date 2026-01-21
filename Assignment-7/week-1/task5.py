try:
    Final_R = int(input("Enter the final result R: "))
except ValueError:
    print("Error: Invalid input.")
    exit()

Step_1 = Final_R - 16
Original = Step_1 / 10
print(int(Original))