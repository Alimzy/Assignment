number = int(input("Enter an integer and enter -2 to stop: "))

positive = 0
negative = 0
zero = 0

stop = -2
while number != -2 :
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1
    if number == 0:
        zero += 1 
    number = int(input("Enter an integer and enter -2 to stop: "))
print("Sum of positive number is ", positive)
print("Sum of negative number is ", negative)
print("Sum of zero number is ", zero)


    


  
