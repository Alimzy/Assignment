player_one = input("'Player One' enter either 'rock','paper' or 'scissors': ")
player_two = input("'Player two' enter either 'rock','paper' or 'scissors': ")




if player_one == "scissors" and player_two == "rock":
    print("player two wins")
elif player_one == "rock" and player_two == "scissors":
    print("player one wins")
elif player_one == "paper" and player_two == "rock":
    print("player one wins")
elif player_two == "scissors" and player_one == "rock":
    print("player one wins")
elif player_two == "rock" and player_one == "scissors":
    print("player two wins")
elif player_two == "paper" and player_one == "rock":
    print("player paper wins")
elif player_one == "paper" and player_two == "paper":
    print("This is a tie")
elif player_one == "rock" and player_two == "rock":
    print("This is a tie")
elif player_one == "scissors" and player_two == "scissors":
    print("This is a tie")
