# Rock Paper Scissors Game
player_1 = input('player 1, Choose between Rock Paper and Scissors: ')
player_2 = input('player 2 Choose between Rock Paper and Scissors: ')

valid_options = ["rock", "paper", "scissors"]
if player_1.lower() in valid_options and player_2.lower() in valid_options:
    if player_1.lower() == "rock" and player_2.lower() == "scissors":
        print('Player 1 has won the game ')
    elif player_1.lower() == "paper" and player_2.lower() == "scissors":
        print('Player 2 has won the game ')
    elif player_1.lower() == "rock" and player_2.lower() == "paper":
        print('Player 2 has won the game ')
    elif player_1.lower() == "scissors" and player_2.lower() == "paper":
        print('Player 2 won the game ')
    elif player_1.lower() == "scissors" and player_2.lower() == "rock":
        print('player 2 has won the game ')
    elif player_1.lower() == "paper" and player_2.lower() == "rock":
        print('Player 1 has won the game ')
    else:
        print('The game is a draw')
else:
    print('Invalid input')
