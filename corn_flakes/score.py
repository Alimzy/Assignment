pass_mark = 45

for score in range(1,15):
    input_score = int(input("Enter a score: "))
    if input_score >= pass_mark:
        print("Student passed, Scholarrrrrr")
    elif input_score < pass_mark:
        print("student failed,olodo rabata")
