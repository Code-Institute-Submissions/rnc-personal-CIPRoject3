# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from simple_term_menu import TerminalMenu

# Global Information about the player
PLAYER_HP = 25
PLAYER_DMG = 5

# Gloabl Information about monsters (consider revising)
MONSTER_HP = 1
MONSTER_DMG = 1

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
    #If Statement about the Monsters Condition (is it dead?)
    # Is there a terminal library for colored terminal text?
    return MONSTER_HP

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
    player_attack(PLAYER_DMG)
  

if __name__ == "__main__":
    main()
