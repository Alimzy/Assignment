integer_one = int(input("Enter integer one: "))
integer_two = int(input("Enter integer two: "))
integer_three = int(input("Enter integer three: "))

if integer_one > integer_two and integer_one > integer_three: 
    print("integer_one is the largest number: ", integer_one)
if integer_two > integer_one and integer_two > integer_three:
    print("integer_two is the largest number: ")
else:print("integer three is the largest number: ", integer_three)
