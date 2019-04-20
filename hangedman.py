from functions import *
import time

hangedman=[
        "           \n"
        "           \n"
        "           \n"
        "           \n"
        "           \n"
        "           \n",

        "            \n"
        "  |         \n"
        "  |         \n"
        "  |         \n"
        "  |         \n"
        " _|         \n",

        "  _______   \n"
        "  |         \n"
        "  |         \n"
        "  |         \n"
        "  |         \n"
        " _|         \n",

        "  _______   \n"
        "  | /       \n"
        "  |/        \n"
        "  |         \n"
        "  |         \n"
        " _|         \n",

        "  _______   \n"
        "  | /   '   \n"
        "  |/        \n"
        "  |         \n"
        "  |         \n"
        " _|         \n",

        "  _______   \n"
        "  | /   '   \n"
        "  |/    O   \n"
        "  |         \n"
        "  |         \n"
        " _|         \n",

        "  _______   \n"
        "  | /   '   \n"
        "  |/    O   \n"
        "  |     |   \n"
        "  |         \n"
        " _|         \n",


        "  _______   \n"
        "  | /   '   \n"
        "  |/    O   \n"
        "  |     |   \n"
        "  |    /    \n"
        " _|         \n",

        "  _______   \n"
        "  | /   '   \n"
        "  |/    O   \n"
        "  |     |   \n"
        "  |    / \\ \n"
        " _|         \n",

        "  _______   \n"
        "  | /   '   \n"
        "  |/   \\O  \n"
        "  |     |   \n"
        "  |    / \\ \n"
        " _|         \n",

        "  _______   \n"
        "  | /   '   \n"
        "  |/   \\O/ \n"
        "  |     |   \n"
        "  |    / \\ \n"
        " _|         \n",

        ]

def copadam(turns):
    print(turns,"hakkiniz kaldi.")
    print(hangedman[10 - turns])


def gamestart():
    for i in hangedman:
        clear_screen()
        print(i)
        time.sleep(0.123)
    for i in range(len(hangedman)):
        clear_screen()
        print(hangedman[-i-1])
        time.sleep(0.123)
    for i in range(2):
        clear_screen()
        time.sleep(0.234)
        print(hangedman[10])
        time.sleep(0.234)
    clear_screen()
    print("---HANGMAN---                                          (gokselaktas)\n\n")
