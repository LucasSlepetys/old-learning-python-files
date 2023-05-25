import time
import random

def chooseWinner(p1, bot): 
    

player_one_choice = input("rock, paper or scissors ->")

list_choice = ["rock", "paper", "scissors"]
bot = random.choice(list_choice)


chooseWinner(player_one_choice, bot)


