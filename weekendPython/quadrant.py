number_x = int(input("Enter X: "))
number_y = int(input("Enter y: "))

if number_x > 0 and number_y > 0:
    print("This is 'Q1'")
elif number_x < 0 and number_y > 0:
    print("This is 'Q2'")
elif number_x < 0 and number_y < 0:
    print("This is 'Q3'")
elif number_x > 0 and number_y < 0:
    print("This is 'Q4'")
elif number_x == 0 and number_y == 0:
    print("This is 'Origin'")
elif number_y == 0 and number_x != 0:
    print("This is 'X-axis'")
elif number_x == 0 and y != 0:
    print("This is 'Y-axis'")



