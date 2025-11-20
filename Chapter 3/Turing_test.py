question_one = input("What is your problem? ")

while True :
    question_two = input("Have you had this problem before(yes or no: )").lower()
    if question_two == "yes":
        print("well, you have it again")
    if question_two == "no":
        print("well, you have it now")
    break
