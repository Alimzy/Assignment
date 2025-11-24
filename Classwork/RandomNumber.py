
guess_number = 20
input_number = int(input("Guess a number: "))

while input_number != guess_number:
    if input_number > guess_number:
        print("Too high")
    elif input_number < guess_number:
        print("Too low")
    elif input_number == guess_number:
        print("you are correct ", guess_number, "is the correct number")
    input_number = int(input("Guess a number: "))
