import random
import os
import time
from hangedman import *




def clear_screen():#ekrani temizlemek icin
    os.system('clear')
    return

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def print_alphabet(alphabet):
    x = '|'.join(alphabet)
    print("Kullanilabilir harfler=> ",x)


triedword=[]
def inputal(word,turns):#kullanicindan input alma sartlari

    try:
        while True:
            time.sleep(0.3)
            harf = input("\n\nHarf giriniz: \n")
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
    except:
        print("harf veya tahmin girmediniz.")
        triedword.remove(harf)
        turns += 1
        time.sleep(1)
    return harf,turns
