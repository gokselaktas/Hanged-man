import random

def choose_word():#text dosyasindan kelime okuma
    f=open("wordlist.txt","r")
    content = f.read()
    wordlist = content.split("\n")
    i = random.randint(0,len(wordlist)-1)
    return wordlist[i]
