import time
import random
import os
from hangedman import *
from functions import *
from choose_word import choose_word

def game():
    guesses = ''
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print (char, end = " ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n Kazandin")
            break

        guess,turns = inputal(word,turns)
        guesses += guess
        if guess not in word:
            turns -= 1
            clear_screen()
            print_alphabet(alphabet)
            print("\nYanlış Bildiniz")
            copadam(turns)
            if turns == 0:
                print("Kelime => ", word," <=")
                print("\nKaybettiniz")
        else:
            clear_screen()
            print_alphabet(alphabet)
            copadam(turns)



gamestart()
time.sleep(0.321)
word = choose_word()
game()
