import random

def cracker(password):
    x = len(password)
    letters = "abcdefghijklmnopqrstuvwxyz"
    word = ""
    for i in range(0,x):
        index = random.randint(0,25)
        letter = letters[index]
        word = word + letter
    return word


def start_crack(password):
    numb = 0
    while True:
        numb+=1
        temp = cracker(password)
        print(numb)
        if temp == password:
            print("cracked")
            break



start_crack("er")


def coder(word):
    x = word.len
    letters = "abcdefghijklmnopqrstuvwxyz"
    for 



