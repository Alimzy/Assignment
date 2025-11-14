#colllect input from users
#save it in a variable
#compare if 


integers = input("password: ")


 
if len(integers) <= 10 and len(integers) > 6:
    print("medium")
elif len(integers) < 6:
    print("Weak")
elif len(integers) > 10:
    print("Strong")
elif len(integers) < 1:
    print("This code is invalid")
