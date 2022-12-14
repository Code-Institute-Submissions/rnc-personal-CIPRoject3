# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
import random
from simple_term_menu import TerminalMenu
import emoji
from rich.console import Console
from monsters import Goblin, Rat, Skeleton, Zombie, Dragon, Knight, Wizard, Orc, Troll, Giant
from items import MinorHealthPotion, StandardHealthPotion, FullHealthRestore, MaxHealthUp, WeaponUp, UmbraSword

# Setup for Rich Library for Styling the terminal
console = Console()

# Default Information about the player (Is modified by class selection)
PLAYER_HP = 20
PLAYER_MAX_HP = 100
PLAYER_DMG = randint(1, 10)
CURRENT_PLAYER_CLASS = None
PLAYER_INV = []

# Current Player State
PLAYER_HAS_WIN_CONDITION = False
PLAYER_ENCOUNTER = False

# Global Information about Monster
# TODO Make the Monsters name randomised from a dictionary/list
MONSTER_HP = randint(5, 40)
MONSTER_DMG = randint(1, 5)

# TODO - Each Cell Should have a name, think about how do do this: K/V Dictionary?
MAP_GRID = {
    1: "The Crystal Caves",
    2: "The Cursed Forest",
    3: "The Dark Tower",
    4: "The Dragon's Den",
    5: "The Enchanted Garden",
    6: "The Ghost Ship",
    7: "The Goblin King's Castle",
    8: "The Haunted Mansion",
    9: "The Invisible City",
    10: "The Island of the Dead",
    11: "The Land of Ice and Snow",
    12: "The Land of the Fire Giants",
    13: "The Lightning Fields",
    14: "The Lost City",
    15: "The Misty Mountains",
    16: "The Necromancer's Tomb",
    17: "The Ocean of Storms",
    18: "The Palace of the Faerie Queen",
    19: "The Pool of the Forgotten Dead",
    20: "The Ruins of the Ancient City",
    21: "The Secret Laboratory",
    22: "The Sewers of the City",
    23: "The Temple of the Sun God",
    24: "The Temple of the Moon Goddess",
    25: "The Time Warp",
    26: "The Valley of the Dead",
    27: "The Volcano of Fire",
    28: "The Wasteland",
    29: "The Waterfall of Eternal Youth",
    30: "The Well of Souls",
    31: "The Witch's Cauldron",
    32: "The Wizard's Tower",
    33: "The Xyzzy Dimension",
    34: "The Yellow Desert",
    35: "The Ziggurat of the Moon",
    36: "The Ziggurat of the Sun",
    37: "The Zodiac Temple",
    38: "The Zombie's Lair",
    39: "The Abyss",
    40: "The Blackhole",
    41: "The Crystal Palace",
    42: "The Cursed Castle",
    43: "The Dark Forest",
    44: "The Dragon's Lair",
    45: "The Enchanted Castle",
    46: "The Ghost Town",
    47: "The Goblin King's Kingdom",
    48: "The Haunted Woods",
    49: "The Invisible Castle",
    50: "The Island of the Undead",
    51: "The Land of Ice and Fire",
    52: "The Land of the Ice Giants",
    53: "The Lightning Forest",
    54: "The Lost Kingdom",
    55: "The Misty Swamp",
    56: "The Necromancer's Crypt",
    57: "The Ocean of Storms",
    58: "The Palace of the Elf Queen",
    59: "The Pool of the Cursed Dead",
    60: "The Ruins of the Lost City",
    61: "The Secret Mine",
    62: "The Sewers of the Castle",
    63: "The Temple of the Earth Goddess",
    64: "The Temple of the Air God",
    65: "The Time Loop",
    66: "The Valley of the Lost Souls",
    67: "The Volcano of Ice",
    68: "The Wasteland of the Undead",
    69: "The Waterfall of Eternal Life",
    70: "The Well of Wishes",
    71: "The Witch's Dungeon",
    72: "The Wizard's Castle",
    73: "The Xyzzy Dimension of Illusions",
    74: "The Yellow Savannah",
    75: "The Ziggurat of the Dragon",
    76: "The Ziggurat of the Phoenix",
    77: "The Zodiac Temple of Time",
    78: "The Zombie's Haunt",
    79: "The Abyss of the Lost",
    80: "The Blackhole of Despair",
    81: "Umbral Stone"
}

CURRENT_POSITION = 40

# List of Enemy Types
ENEMY_LIST = [Goblin, Rat, Skeleton, Zombie, Dragon, Knight, Wizard, Orc, Troll, Giant]

# List of Loot
LOOT_LIST = [MinorHealthPotion, StandardHealthPotion, FullHealthRestore, MaxHealthUp, WeaponUp]
OBJECTIVE = UmbraSword

"""
Player Setup
"""

def player_class_selection(player_class):
    """
    Sets the HP/DMG values for the player class
    """
    global PLAYER_HP
    global PLAYER_DMG
    global PLAYER_MAX_HP
    global CURRENT_PLAYER_CLASS

    if player_class == 'Warrior':
        PLAYER_HP = 150
        PLAYER_MAX_HP = PLAYER_HP
        PLAYER_DMG = randint(5, 7)
        print(emoji.emojize(f"HP: :red_heart:  {PLAYER_HP} | DMG: :crossed_swords:  {PLAYER_DMG}"))
        print(f"The {player_class} has a higher base damage and good max DMG (6-31).")

    elif player_class == 'Mage':
        PLAYER_HP = 85
        PLAYER_MAX_HP = PLAYER_HP
        PLAYER_DMG = randint(2, 3)
        print(emoji.emojize(f"HP: :red_heart:  {PLAYER_HP} | DMG: :crossed_swords:  {PLAYER_DMG}"))
        print(f"The {player_class} has a lower base damage but is more consistent (3-9).")

    elif player_class == 'Rogue':
        PLAYER_HP = 120
        PLAYER_MAX_HP = PLAYER_HP
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

def search_area():
    """
    When the player searches, roll a 1/100 dice roll
    and return a random item based on the score.
    There is also a chance that the player finds
    a monster by re-calling the encounter dice roll
    """
    global PLAYER_HP
    global PLAYER_MAX_HP
    global PLAYER_DMG
    global PLAYER_HAS_WIN_CONDITION
    global OBJECTIVE
    
    find_chance = legendary_weighted_dice_roll()
    print(f"You scout the area, and score {find_chance}")

    # Choose a random class enemy from the ENEMY_LIST
    if find_chance < 100:
        randomised_loot_choice = random.choice(LOOT_LIST)
    else:
        randomised_loot_choice = OBJECTIVE

    # Creates an instance of the chosen class enemy and assigns it to instanced_enemy with some base DMG and HP
    instanced_loot = randomised_loot_choice("Loot", randint(1, 6))

    # Conditions update Global Vars (Player HP/DMG/Win Condition)
    value_to_apply = instanced_loot.calculate_mod_value()
    if 'HP' in instanced_loot.name and PLAYER_HP < PLAYER_MAX_HP:
        PLAYER_HP = PLAYER_HP + value_to_apply
        console.print(f"You find a [yellow]HP Potion[/] restoring: [green]{value_to_apply}[/]")
        console.print(f"Your HP is now: [red]{PLAYER_HP}[/]\n")
    # elif instanced_loot.name == 'Standard HP Potion':
    #     PLAYER_HP = PLAYER_HP + value_to_apply
    # elif instanced_loot.name == 'Full HP Restore':
    #     PLAYER_HP = PLAYER_HP + value_to_apply
    elif instanced_loot.name == 'Max Health Up':
        PLAYER_MAX_HP = PLAYER_MAX_HP * 1.25
        console.print(f"You Find a [yellow]{ instanced_loot.name }![/]")
        console.print(f"Your Max HP is now: [red]{PLAYER_MAX_HP}[/] (+25%)\n")
    elif instanced_loot.name == 'Weapon Upgrade':
        PLAYER_DMG = PLAYER_DMG + value_to_apply
        console.print(f"You Find a [yellow]{ instanced_loot.name }![/]")
        console.print(f"Your Base DMG is now: [blue]{PLAYER_DMG}[/]\n")
    elif instanced_loot.name == 'Umbra Sword':
        PLAYER_HAS_WIN_CONDITION = True


# Player Navigation
def player_nav(move):
    """
    Allows the users to choose where to move next
    """
    global CURRENT_POSITION
    console.print(f"[bold]You are currently in :[/] [blue]{MAP_GRID[CURRENT_POSITION]}\n[/]")
    
    if move == 'Left':
        # error handling in here
        CURRENT_POSITION -= 1
        console.print(f"You Moved: [blue]{move}[/]")
    if move == 'Right':
        # error handling in here
        CURRENT_POSITION += 1
        console.print(f"You Moved: [blue]{move}[/]")
    if move == 'Up':
        # error handling in here
        if CURRENT_POSITION >= 9:
            CURRENT_POSITION -= 9
            console.print(f"You Moved: [blue]{move}[/]")
        else:
            print("You cannot go that way.")
    if move == 'Down':
        # error handling in here
        if CURRENT_POSITION <= 72:
            CURRENT_POSITION += 9
            console.print(f"You Moved: [blue]{move}[/]")
        else:
            print("You cannot go that way.")
    if move == 'Search':
        # Search function here
        search_area()

    # print(f"You are now in: {MAP_GRID[CURRENT_POSITION]}")
    return move

def player_enters_location():
    """
    Checks when the player moves, if a monster appears or not
    """
    global PLAYER_ENCOUNTER
    global MONSTER_HP
    global MONSTER_DMG
    global ENEMY_LIST

    encounter = med_weighted_dice_roll()
    if encounter > 20:
        print(f"Your dice roll scored {encounter} and a monster appears!")
        PLAYER_ENCOUNTER = True
        # Choose a random class enemy from the ENEMY_LIST
        encounter_enemy_choice = random.choice(ENEMY_LIST)

        # Creates an instance of the chosen class enemy and assigns it to instanced_enemy with some base DMG and HP
        instanced_enemy = encounter_enemy_choice("ENEMY", randint(1, 6), randint(1, 6))

        # Calculates the HP of the instanced enemy
        MONSTER_HP = instanced_enemy.calculate_monster_hp()
        MONSTER_DMG = instanced_enemy.base_dmg

        # Prints the name of the instanced enemy and its HP and DMG
        console.print(f"It's a [red]{ instanced_enemy.name }[/]!\nHP: [blue]{MONSTER_HP}[/] | DMG: [purple]{MONSTER_DMG}[/]")
        
        # print(f"Encounter: {PLAYER_ENCOUNTER}") <- This can be removed
        # print(f"The Monster HP is: {MONSTER_HP}") <- This can be removed
        return PLAYER_ENCOUNTER
    else:
        print(f"Your dice roll scored {encounter}...safe...for now.")
        print("Do you want to move or search the area?\n")


# Main Combat functions
def monster_attack(dmg):
    """Attack Loop for Monster Encounters"""
    # Need to make monster Damage variable
    global PLAYER_HP
    global PLAYER_DMG
    global PLAYER_ENCOUNTER

    console.print(emoji.emojize(f"Your Stats are: :red_heart:  [red]{PLAYER_HP}[/] | :crossed_swords:  [blue]{PLAYER_DMG}[/]\n"))
    console.print(emoji.emojize(f"The Monster attacks you for: :crossed_swords:  [purple]{MONSTER_DMG}[/]\n"))
    PLAYER_HP = PLAYER_HP - dmg
    console.print(emoji.emojize(f"Your HP is: :red_heart:  [red]{PLAYER_HP}[/]\n"))
    if PLAYER_HP <= 0:
        console.print(emoji.emojize(f"You were slain by the monster: :headstone:  HP:[bold]{PLAYER_HP}[/] :headstone:  \n"))
        print("Returning to Main Menu")
        PLAYER_ENCOUNTER = False
        # print(f"Encounter: {PLAYER_ENCOUNTER}")
        main()
    return PLAYER_HP

def player_attack(dmg):
    """Attack Loop for Monster Encounters"""
    # Needs some more thought about how the Monster HP/DMG is stored
    global CURRENT_PLAYER_CLASS
    global MONSTER_HP
    global PLAYER_ENCOUNTER

    # Checks the class of the player and adds a 'skill' randomised number to their base damage
    if CURRENT_PLAYER_CLASS == 'Warrior':
        dmg = dmg + med_weighted_dice_roll()

    elif CURRENT_PLAYER_CLASS == 'Mage':
        dmg = dmg + low_weighted_dice_roll()

    elif CURRENT_PLAYER_CLASS == 'Rogue':
        dmg = dmg + high_weighted_dice_roll()

    console.print(emoji.emojize(f"The Monsters HP is: :blue_heart:  [blue]{MONSTER_HP}[/]\n"))
    console.print(emoji.emojize(f"You Attack the Monster for : :crossed_swords:  [bold]{dmg}[/]\n"))
    MONSTER_HP = MONSTER_HP - dmg
    console.print(emoji.emojize(f"The Monsters HP is: :blue_heart:  [blue]{MONSTER_HP}[/]\n"))
    if MONSTER_HP <= 0:
        console.print(emoji.emojize(f"The Monster is dead: :face_with_crossed-out_eyes: Enemy HP:  [bold]{MONSTER_HP}[/]\n"))
        PLAYER_ENCOUNTER = False
        # print(f"Encounter: {PLAYER_ENCOUNTER}")
        # Reassigning move value so the player stays in same place after combat
        move = None
        player_nav(move)

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
        move_list = ["Left", "Right", "Up", "Down", "Search"]
        command_menu = TerminalMenu(move_list)
        display_move_list = command_menu.show()
        print(f"You have selected {move_list[display_move_list]}!")
        player_nav(move_list[display_move_list])
        player_enters_location()
        if PLAYER_ENCOUNTER is True:
            while MONSTER_HP > 0:
                monster_attack(MONSTER_DMG)
                player_attack(PLAYER_DMG)


if __name__ == "__main__":
    main()

