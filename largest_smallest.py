number_one = int(input("Enter user input: "))

number_two = int(input("Enter user input: "))

number_three = int(input("Enter user input: "))

addition = number_one + number_two + number_three
print("the sum of integers is :", addition)

average = (number_one + number_two + number_three) / 3
print("The average is: ", average)

product = number_one * number_two * number_three
print("The product is: ", product)

if number_one > number_two and number_one > number_three:
    print("This is the highest number: ", number_one)

if number_one < number_two and number_one < number_three:
    print("This is the lowest number: ", number_one)

if number_two > number_one and number_two > number_three:
    print("This is the highest number: ", number_one)

if number_two < number_one and number_two > number_three:
    print("This is the lowest number: ", number_one)


if number_three > number_one and number_three > number_two:
    print("This is the highest number: ", number_one)


if number_three < number_one and number_three < number_two:
    print("This is the lowest number: ", number_one)

