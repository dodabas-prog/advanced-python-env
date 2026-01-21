ticket_num = input("Enter a 6-digit ticket number: ")
if len(ticket_num) != 6 or not ticket_num.isdigit():
    print("NO")
    exit()

digits = [int(d) for d in ticket_num]
sum1 = sum(digits[0:3])
sum2 = sum(digits[3:6])
if sum1 == sum2:
    print("YES")
else:
    print("NO")