# MAKE A ROCK PAPER SCISSOR GAME

import random

ai = random.choice(["rock","paper","scissor"])

user = input("enter your choice: ")

print("ai choose:", ai)

print("you choose:", user)

if(ai == "rock" and user == "paper"):
    print("you win!!!")


elif(ai == "rock" and user == "scissor"):
    print("you lose!!!")


elif(ai == "scissor" and user == "paper"):
    print("you lose!!!")


elif(ai == "scissor" and user == "rock"):
    print("you win!!!")


elif(ai == "paper" and user == "rock"):
    print("you lose!!!")


elif(ai == "paper" and user == "scissor"):
    print("you win!!!")


elif(ai == user):
    print("its a draw!!!")


else:
    print("error")

