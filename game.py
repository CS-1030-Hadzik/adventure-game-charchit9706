'''
DOC STRING
Adventure Game
Author: Charchit Pokhrel
Version: 2.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''
#---------------------------------------------------------------------
# Player class to store player info and game state
#---------------------------------------------------------------------

class Player:
    # initializer/constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# --------------------------------------------------------------------
# Function : welcome_player
# Greet the player, ask for their name and return the name as a string
# --------------------------------------------------------------------

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")

    # Ask for the player's name
    name = input("What is your name, adventurer?")
    player = Player(name)

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player.name}! Your journey begins now.")

    return player

# --------------------------------------------------------------------
# Function : describe_area
# Print the opening description of the area
# --------------------------------------------------------------------

def describe_area():
    # Describe the starting area
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown...
    """)
    
# --------------------------------------------------------------------
# Function : add_to_inventory
# Accepts an item as a parameter
# Adds it to the inventory list and confirm the pickup to the player
# --------------------------------------------------------------------

def add_to_inventory(item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

# --------------------------------------------------------------------
# Game starts here
# Call the welcome and describe area functions
# --------------------------------------------------------------------

player = welcome_player()
describe_area()

# --------------------------------------------------------------------
# Main game loop
# Run this until the player quits


# TODO: Inside the game loop:
#       - If the user chooses option 2, call add_to_inventory("map")

# Start the game Loop
while True: 
    print("\nYou see two path ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Take the straight path into the cave.")
    print("\t4. Stay where you are.")

    print("\tType 'i' to view your inventory.")

    decision = input("What will you do (1,2,3,4 or i): ").lower()

    if decision == "i":
        print("Inventory", player.inventory)
        continue

    if decision == "1":
        print(f"{player.name}, you step into the dark woods. The trees whisphered as you walk deeper.")
        add_to_inventory("lantern")
        player.has_lantern = True

    elif decision == "2":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("map")
        player.has_map(True)

    elif decision == "3":
        if player.has_lantern:
            print(f"{player.name}, you see two paths ahead")
            print("Inside the cave, you have hidden treasure.")
        
        else:
            print("Its too dark to continue without a lantern.")
            print("Maybe you find a light source to move ahead!")

    # Stay where you are
    elif decision == "4":
        print("You stay still listening to the "
              "distant sounds of the forest")

    else:
        print("Invalid choice. Please choose "
              "1, 2, 3, 4.")

    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game