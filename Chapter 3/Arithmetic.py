largest = 0
smallest = 
product = 1
addition = 0
average = 0


for counter in range(0,4):
    number = int(input("Enter an integer: "))
    if number > largest:
        largest += number
    if number < smallest:
        smallest += number
    product *= number
    addition += number

average = addition / 4
print("The sum of integers is: ", addition)
print("The Largest number is: ", largest)
print("The smallest number is: ", smallest) 
print("The product of integers is: ", product)
print("The average of integers is: ", average)
      
        
