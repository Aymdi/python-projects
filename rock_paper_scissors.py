"""
Beginner Pythn Project by Aymdi
Rock Paper Scissors game
"""

import random

def play():
    user_score, computer_score, total_games,replay = 0,0,0,1
    while replay == 1:
        user=input("Paper (P), Rock (R), or Scissors (S) ? ").lower()
        while user!='p' and user!='r' and user!='s':
            print(f"{user} is not available, please choose again")
            user=input("Paper (P), Rock (R), or Scissors (S) ? ").lower()
        computer=random.choice(['P','R','S']).lower()
        print(f"User choosed {user}")
        print(f"Computer choosed {computer}")
        result=is_win(user,computer)
        if result==1:
            user_score+=1
        else:
            computer_score+=1
            total_games+=1
        replay=show_score(total_games,user_score,computer_score)
    
def show_choice(player):
    print(player)

def show_score(total_games,user_score,computer_score):
    print(f"You played {total_games} times\nuser score: {user_score}\ncomputer score: {computer_score}")
    rps=input(f"Want to play again ? Yes (y) or No (n) : ").lower()
    if rps=='y':
        return 1
    else:
        return 0
    
    
def is_win(player,opponent):
    if player==opponent:
        print("Equality !")
    elif    (player=='s' and opponent=='p') \
            or (player=='p' and opponent=='r') \
            or (player=='r' and opponent=='s'):
        print("User wins !")
        return 1
    else:
        print("Computer wins !")
        return 0

play()
    
