"""
Beginner Python Project by Aymdi
Guess the number
"""

import random

def guess(n):
    '''
    The user has to guess to magic number picked by the computer
    '''
    N=random.randint(1,n)
    number=0
    while (number != N):
        number=int(input(f"Give a number between 1 and {n}: "))
        if number<N:
            print("Sorry, guess again. Too low.")
        elif number > N:
            print("Sorry, guess again. Too high.")
    print(f"Yaaay, congrats. You have guessed the number {N} correctly !")

def computer_guess(n):
    '''
    The computer has to guess the magic number picked by the user
    '''
    low,high=1,n
    feedback=''
    while feedback!='c':
        guessed_number=random.randint(low,high)
        print(f"COMPUTER: I choose {guessed_number}")
        feedback=input(f"Is {guessed_number} too high (H), too low (L), or correct (C) ?").lower()
        if feedback=='H':
            high=guessed_number-1
        elif feedback=='L':
            low=guessed_number+1
    print(f"COMPUTER: Your magic number is {guessed_number}.")

