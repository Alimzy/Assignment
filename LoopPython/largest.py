#number = int(input("Enter numbers and press -2 to stop: "))

largest = 0
smallest = 0
number = 0

stop = -2
while number != stop:
    number = int(input("Enter numbers and press -2 to stop: "))
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    if number == stop:
        print("Thanks for playing")
print(largest, "is the largest number")
print(smallest, "is the smallest number")
                    
