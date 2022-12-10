# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from simple_term_menu import TerminalMenu
from random import randint

# Global Information about the player
PLAYER_HP = 25
PLAYER_DMG = 5

# Gloabl Information about monsters (consider revising)
MONSTER_HP = 1
MONSTER_DMG = 1

"""
Player Setup
"""

def player_class_selection(player_class):
    """
    Sets the HP/DMG values for the player class
    """
    global PLAYER_HP
    global PLAYER_DMG

    if player_class == 'Warrior':
        PLAYER_HP = 40
        PLAYER_DMG = 10
        print(f"Your stats are HP: {PLAYER_HP} | DMG: {PLAYER_DMG}")

    elif player_class == 'Mage':
        PLAYER_HP = 15
        PLAYER_DMG = 20
        print(f"Your stats are HP: {PLAYER_HP} | DMG: {PLAYER_DMG}")

    elif player_class == 'Rogue':
        PLAYER_HP = 20
        PLAYER_DMG = 15
        print(f"Your stats are HP: {PLAYER_HP} | DMG: {PLAYER_DMG}")

    return player_class

# Dice Rolls
# Could this be one function with paramenters for the rarity?
def low_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/6
    """
    roll_6 = randint(1, 6)
    print(f"You scored a {roll_6 }")
    return roll_6

def med_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/24
    """
    roll_24 = randint(1, 24)
    print(f"You scored a {roll_24 }")
    return roll_24

def high_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/50
    """
    roll_50 = randint(1, 50)
    print(f"You scored a {roll_50 }")
    return roll_50

def legendary_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/100
    """
    roll_100 = randint(1, 100)
    print(f"You scored a {roll_100 }")
    return roll_100

# Player Navigation
def player_nav():
    """
    Allows the users to choose where to move next
    """
    print("Which direction do you want to go?\n")
    move = input("Type 'up, down, left or right'\n")
    print(move)
    return move

# Main Combat functions
def monster_attack(dmg):
    """Attack Loop for Monster Encounters"""
    # Need to make monster Damage variable
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - dmg
    print(f"Your HP is: {PLAYER_HP}")
    return PLAYER_HP

def player_attack(dmg):
    """Attack Loop for Monster Encounters"""
    # Needs some more thought about how the Monster HP/DMG is stored
    global MONSTER_HP
    MONSTER_HP = MONSTER_HP - dmg
    print(f"The Monsters HP is: {MONSTER_HP}")
    # If Statement about the Monsters Condition (is it dead?)
    # Is there a terminal library for colored terminal text?
    return MONSTER_HP



# ------------------MAIN GAME LOOP------------------
def main():
    """
    Main game Loop
    """
    options = ["Warrior", "Mage", "Rogue"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    player_class_selection(options[menu_entry_index])
    # print(options[menu_entry_index])
    # monster_attack(3)
    # player_attack(PLAYER_DMG)
    player_nav()
    # legendary_weighted_dice_roll()
  

if __name__ == "__main__":
    main()
