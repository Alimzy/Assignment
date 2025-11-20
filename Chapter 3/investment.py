principal_amount = int(input("Enter principal amount"))
rate = int(input("Enter annual rate"))
years = int(input("Enter amount of years"))

for number in range(0,31):
    amount = principal_amount * (1 + rate)**number
    print(f"Amount at the end of the year is ", amount)
    
     {}

