'''
DOCSTRING
Adventure Game
Author: Charchit Pokhrel
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest
'''

# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")



#Ask for the player's name
player_name= input("What is your name, adventurer?")

#concatenate strings to create a personalized message
print("Welcome, " + player_name + "! Your journey begins now")

#use an f-string to display the same message in a more readable way
print(f"welcome, {player_name}! Your journey begins now.")


#Describe the starting area
starting_area = """
You find yourself in a dark forest
The sound of rustling leaves fills the air
A faint path lies ahead, leading deeper into the
unknown...

"""
print(starting_area)