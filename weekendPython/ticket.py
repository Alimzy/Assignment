age = int(input("Enter Age for ticket policy: "))

if age < 5:
    print("Entry is free")
elif age >= 15 and age <= 12:
    print("Entry is $5")
elif age >= 13 and age <= 64:
    print("Entry is $12")
elif age >= 65:
 print("Entry is $8")

