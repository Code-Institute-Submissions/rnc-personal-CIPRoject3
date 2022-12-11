# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from simple_term_menu import TerminalMenu
from random import randint
import emoji

# Consider using https://pypi.org/project/colorama/ for colors in terminal

# Default Information about the player (Is modified by class selection)
PLAYER_HP = 20
PLAYER_DMG = randint(1, 10)
CURRENT_PLAYER_CLASS = None

# Current Player State
PLAYER_HAS_WIN_CONDITION = False
PLAYER_ENCOUNTER = False

# Global Information about Monster
# TODO Make the Monsters name randomised from a dictionary/list
MONSTER_HP = randint(5, 40)
MONSTER_DMG = randint(1, 5)

# TODO - Each Cell Should have a name, think about how do do this: K/V Dictionary?
MAP_GRID = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]

CURRENT_POSITION = MAP_GRID[40]

"""
Player Setup
"""

def player_class_selection(player_class):
    """
    Sets the HP/DMG values for the player class
    """
    global PLAYER_HP
    global PLAYER_DMG
    global CURRENT_PLAYER_CLASS

    if player_class == 'Warrior':
        PLAYER_HP = 40
        PLAYER_DMG = randint(5, 7)
        print(emoji.emojize(f"HP: :red_heart:  {PLAYER_HP} | DMG: :crossed_swords:  {PLAYER_DMG}"))
        print(f"The {player_class} has a higher base damage and good max DMG (6-31).")

    elif player_class == 'Mage':
        PLAYER_HP = 15
        PLAYER_DMG = randint(2, 3)
        print(emoji.emojize(f"HP: :red_heart:  {PLAYER_HP} | DMG: :crossed_swords:  {PLAYER_DMG}"))
        print(f"The {player_class} has a lower base damage but is more consistent (3-9).")

    elif player_class == 'Rogue':
        PLAYER_HP = 20
        PLAYER_DMG = randint(3, 5)
        print(emoji.emojize(f"HP: :red_heart:  {PLAYER_HP} | DMG: :crossed_swords:  {PLAYER_DMG}"))
        print(f"The {player_class} has the lowest base damage but can critical hit for very high damage (4-50).")

    CURRENT_PLAYER_CLASS = player_class
    return CURRENT_PLAYER_CLASS

# Dice Rolls
# Could this be one function with paramenters for the rarity?
def low_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/6
    """
    roll_6 = randint(1, 6)
    # print(f"You scored a {roll_6}")
    return roll_6

def med_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/24
    """
    roll_24 = randint(1, 24)
    # print(f"You scored a {roll_24 }")
    return roll_24

def high_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/50
    """
    roll_50 = randint(1, 50)
    # print(f"You scored a {roll_50}")
    return roll_50

def legendary_weighted_dice_roll():
    """
    Dice roll with a weighting of 1/100
    """
    roll_100 = randint(1, 100)
    # print(f"You scored a {roll_100}")
    return roll_100

# Player Navigation
def player_nav():
    """
    Allows the users to choose where to move next
    """
    global CURRENT_POSITION
    print(f"You are currently in : {CURRENT_POSITION}\n")
    print("Do you want to move or search the area?\n")
    move = input("Type 'up, down, left or right to move or 'search' to loot the area\n")

    # Need to check if the input is a string and matches one of the movement commands here

    if move == 'left':
        # error handling in here
        CURRENT_POSITION -= 1
    if move == 'right':
        # error handling in here
        CURRENT_POSITION += 1
    if move == 'up':
        # error handling in here
        CURRENT_POSITION -= 9
    if move == 'down':
        # error handling in here
        CURRENT_POSITION += 9
    print(f"You Moved: {move}")
    print(f"Your Current Position is {CURRENT_POSITION}")
    return move

def player_enters_location():
    """
    Checks when the player moves, if a monster appears or not
    """
    global PLAYER_ENCOUNTER
    global MONSTER_HP
    encounter = med_weighted_dice_roll()
    if encounter > 20:
        print(f"Your dice roll scored {encounter} and a monster appears!")
        PLAYER_ENCOUNTER = True
        MONSTER_HP = randint(10, 50)
        print(PLAYER_ENCOUNTER)
        print(MONSTER_HP)
        return PLAYER_ENCOUNTER
    else:
        print(f"Your dice roll scored {encounter}...safe...for now.")
        print("You entered a new location")


# Main Combat functions
def monster_attack(dmg):
    """Attack Loop for Monster Encounters"""
    # Need to make monster Damage variable
    global PLAYER_HP
    global PLAYER_ENCOUNTER

    print(emoji.emojize(f"Your HP is: :red_heart:  {PLAYER_HP}\n"))
    print(emoji.emojize(f"The Monster attacks you for: :drop_of_blood:  {MONSTER_DMG}\n"))
    PLAYER_HP = PLAYER_HP - dmg
    print(emoji.emojize(f"Your HP is: :red_heart:  {PLAYER_HP}\n"))
    if PLAYER_HP <= 0:
        print(emoji.emojize(f"You were slain by the monster: :headstone:  HP:{PLAYER_HP} :headstone:  \n"))
        print("Returning to Main Menu")
        PLAYER_ENCOUNTER = False
        main()
        

    return PLAYER_HP

def player_attack(dmg):
    """Attack Loop for Monster Encounters"""
    # Needs some more thought about how the Monster HP/DMG is stored
    global MONSTER_HP
    global PLAYER_ENCOUNTER
    global CURRENT_PLAYER_CLASS

    # Checks the class of the player and adds a 'skill' randomised number to their base damage
    if CURRENT_PLAYER_CLASS == 'Warrior':
        dmg = dmg + med_weighted_dice_roll()

    elif CURRENT_PLAYER_CLASS == 'Mage':
        dmg = dmg + low_weighted_dice_roll()

    elif CURRENT_PLAYER_CLASS == 'Rogue':
        dmg = dmg + high_weighted_dice_roll()

    print(emoji.emojize(f"The Monsters HP is: :blue_heart:  {MONSTER_HP}\n"))
    print(emoji.emojize(f"You Attack the Monster for : :crossed_swords:  {dmg}\n"))
    MONSTER_HP = MONSTER_HP - dmg
    print(emoji.emojize(f"The Monsters HP is: :blue_heart:  {MONSTER_HP}\n"))
    if MONSTER_HP <= 0:
        print(emoji.emojize(f"The Monster is dead: :face_with_crossed-out_eyes: Enemy HP: {MONSTER_HP}\n"))
        PLAYER_ENCOUNTER = False
        player_nav()

    # Is there a terminal library for colored terminal text for Monster death?
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
    while PLAYER_HAS_WIN_CONDITION is False and PLAYER_ENCOUNTER is False:
        player_nav()
        player_enters_location()
        if PLAYER_ENCOUNTER is True:
            while MONSTER_HP > 0:
                monster_attack(MONSTER_DMG)
                player_attack(PLAYER_DMG)


if __name__ == "__main__":
    main()

