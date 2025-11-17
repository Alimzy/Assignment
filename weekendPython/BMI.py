weight = int(input("Enter Weight: "))
height = int(input("Enter height: "))

BMI = weight / height * height


if BMI < 18.5:
    print("Your BMI is", BMI, " You are 'Underweight'")
elif BMI <= 18.5 and BMI <= 24.9:
    print("Your BMI is", BMI, "You are 'Normal''")
elif BMI >= 25 and BMI <= 29.9:
    print("Your BMI is", BMI, "You are 'Overweight'")
else: print("Your BMI is", BMI, "you are obese fam! Go to the gym!!!")
