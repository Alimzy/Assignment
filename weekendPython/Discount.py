total_bill = int(input("Enter total bill: "))
is_member = input("Are you a member? Type 'yes' or 'no': ")

if total_bill >= 1000 and is_member == "yes":
    print("10% off")
if total_bill >= 1000 and is_member == "no":
    print("5% off")
else : print("Your total bill is ", total_bill, "and your member status is, ", is_member, ".So no discount for you")
