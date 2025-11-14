integers = int(input("Enter five user input: "))

number_one = integers // 10000
number_two = (integers % 10000) // 1000
number_three =(integers % 1000) // 100
number_four = (integers % 100) // 10
number_five = integers % 10

print(number_one, number_two, number_three, number_four, number_five)
