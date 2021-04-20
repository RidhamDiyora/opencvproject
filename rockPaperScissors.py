import random

choices = ["rock","paper","scissors"]

comp = random.choice(choices)
player = None
while player not in choices:
 player = input("rock,paper or scissors:\n").lower()

if comp == player:
   print("player:\n",player)
   print("comp:\n",comp)
   print("tie")

elif player == "rock":
     if comp == "scissors":
       print("comp:\n",comp)
       print("player:\n",player)
       print("you lose")
     if comp == "paper":
       print("comp",comp)
       print("player",player)
       print("you won")

elif player == "paper":
    if comp == "scissors":
     print("comp:\n",comp)
     print("player:\n",player)
     print("you lose")
    if comp == "rock":
     print("comp:\n",comp)
     print("player:\n",player)
     print("you won")

elif player == "scissors":
    if comp == "paper":
     print("comp:\n",comp)
     print("player:\n",player)
     print("you lose")
    if comp == "rock":
     print("comp:\n",comp)
     print("player:\n",player)
     print("you won")

print("end")