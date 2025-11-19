input_one = int(input("Enter an integer: "))
input_two = int(input("Enter an integer: "))

addition = input_one + input_two
print("Sum of integer One and Two is: ", addition)
stop = -2

while input_one != stop or input_two != stop:
    print("Enter -2 to terminate ")
    print("Enter integers to continue")
    input_one = int(input("Enter an integer: "))
    input_two = int(input("Enter an integer: "))
    addition = input_one + input_two
    print("Sum of integer One and Two is: ", addition)
