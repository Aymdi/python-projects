"""
Hangman implementation by Aymdi
"""

import random
import string
from words import words

def get_valid_word(words):
    '''
    get a valid word from the list words
    a valid word is a random word chosen from the list without some characters that make it\
    hard to guess.
    '''
    word = random.choice(words)
    while '-' in word or ' ' in word or '_' in word:
        word = random.choice(words)
    return word

def hangman():
    
    replay='y'
    while replay=='y':
        word = get_valid_word(words).upper()
        word_letters = set(word) # the missing word letters 
        alphabet = set(string.ascii_uppercase)
        used_letters = set() # the used letters by the player
        lives = 10
        while len(word_letters)>0 and lives>0:
            print(f"You have {lives} lives left and you have used those letters: {used_letters}")
            word_list = [letter if letter in used_letters else '-' for letter in word] # W-ORD
            print("Current word: ", ' '.join(word_list))

            user_letter=input("Guess a letter: ").upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print("Nice !\n")
                else:
                    lives -=1 # takes away a life if wrong
                    print("You have chosen the letter {user_letter} and it's not in the word.")
            elif user_letter in used_letters:
                print("You have already used this letter. Guess another one.\n")
            else:
                print("That is not valid letter.\n")

        if lives==0:
            print(f"You died x(. The word was {word}.")
        else:
            print(f"Yay! You have correctly guessed the word {word} ! =D")
        replay = input("Want to play again ? Yes (y) or No (n): ").lower()
        
    
hangman()
