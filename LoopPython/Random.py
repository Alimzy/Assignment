import random
guess_number = random.randint(1,30)
input_number = int(input("Enter a guess: "))

while input_number != guess_number:
    if input_number > guess_number:
        print("Too high,try again") 
    if input_number < guess_number:
        print("Too low,try again") 
    if input_number == guess_number:
        print("You guess correctly ", guess_number) 
    input_number = int(input("Enter a guess"))
