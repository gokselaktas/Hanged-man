import time
import random
import os

print("---HANGMAN---\n\n")
time.sleep(0.5)

def clear_screen():#ekrani temizlemek icin
    os.system('clear')
    return

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_alphabet(alphabet):
    x = '|'.join(alphabet)
    print("Kullanilabilir harfler=> ",x)


triedword=[]
def inputal():#kullanicindan input alma sartlari
    try:
        while True:
            time.sleep(0.3)
            harf = input("Harf giriniz\n")
            if harf == word:
                break
            elif len(harf)>1 :
                print("harf girmeniz lazim\n")
            elif harf in triedword:
                print("Kullandiginiz harfi tekrar kullandiniz")
            elif len(harf)==1:
                triedword.append(harf)
                alphabet.remove(harf)
                break
    except ValueError:
        print("harf veya tahmin girmediniz.")
        triedword.remove(harf)
        time.sleep(1)
    return harf

#text dosyasindan kelime okuma
f=open("wordlist.txt","r")
content = f.read()
wordlist = content.split("\n")
i = random.randint(0,len(wordlist)-1)
word = wordlist[i]
################################################################################



def copadam(turns):
    copadam=[
            "           \n"
            "           \n"
            "           \n"
            "           \n"
            "           \n"
            " _         \n",

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
            "  |/    '   \n"
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
    #0,1,2,3,4,5,6,7,8,9,10 ~ len(copadam)=11
    print(turns,"hakkiniz kaldi.")
    print(copadam[10-turns])


guesses = ''
turns = 11
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print (char,end=" ")
        else:
            print("_",end=" ")
            failed+=1

    if failed==0:
        print("\n Kazandin")
        break

    print("\n")
    guess = inputal()
    guesses += guess
    if guess not in word:
        turns -=1
        clear_screen()
        print_alphabet(alphabet)
        print("\nYanlış Bildiniz")
        copadam(turns)
        if turns == 0:
            print("Kelime =>",word)
            print("\nKaybettiniz")
    else:
        clear_screen()
        print_alphabet(alphabet)
        copadam(turns)
