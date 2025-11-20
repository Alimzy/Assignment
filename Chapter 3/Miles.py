miles_driven = float(input("Enter miles driven: "))
gallon_used = float(input("Enter gallon used and use (-1) to end: "))


total_mile = 0
total_gallon = 0
sentinel = -1

while gallon_used != sentinel:   
    miles_driven = float(input("Enter miles driven: "))
    total_mile += miles_driven
    gallon_used = float(input("Enter gallon used and use (-1) to end: "))
    total_gallon += gallon_used
average = total_mile / total_gallon
print("The overall average is", average)
