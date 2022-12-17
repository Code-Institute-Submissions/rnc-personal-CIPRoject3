# PROJECT 3 - Python - MicroRPG 
----------------------

MicroRPG is a terminal based "MUD" text adventure written in Python that recreates the early Role Playing Games when computers first became popular with home users.
Players can choose from different classes (Warrior, Mage, Rogue) that each have different attributes for their health ("HP") and How much Base Damage they can do to monsters ("DMG").

The Game takes place in a virtual map that is made up of a 9 by 9 grid area.
Users have 5 controls to move in 1 of 4 directions (up, down, left, right) or search the area they are in.

Users can find a series of different items in the world that either restore different amounts of health, increase their maximum health, restore all of their health or increase their base Damage.

The objective of the game is to find a rare sword ("The Umbra Sword"), once the users finds this, the quest is over.

Along the way, players will encounter different monsters that also vary in their health and damage values. Some present more of a challenge than others so be wary!

<div align="center">
<img  width="600" height="600" src="https://images2.imgbox.com/68/95/XCH3JsaH_o.png">)
</div>

----------------------
##  FEATURES

### - Classes

When the application loads , the first output asks the player to choose one of the three classes. When a users makes a selection, some global Variables are updated to reflect HP/Damage. These are:

- PLAYER_HP: This tracks the players current HP and can be decreased during combat and restored using items when they are discovered but cannot exceed the PLAYER_MAX_HP value. It is initialised with a placeholder value, which is overrwritten once a class is chosen.

- PLAYER_MAX_HP: This is the maximum health value of the player. At start this will be the same as their current health but it can be increased when items are discovered. It is initialised with a placeholder value, which is overrwritten once a class is chosen.

- PLAYER_DMG: This is the base damage of the player for this 'quest' (instance of the game). it is a random number between a certain range, depending on the class. It is modified during combat by dicerolls, which also vary by class. It is initialised with a random value, which is overrwritten once a class is chosen.

- CURRENT_PLAYER_CLASS: This records the players class and does not change during play but is used in calculations during combat

- PLAYER_HAS_WIN_CONDITION: The win condition is set to false on starting the game. The game ends once this is True and can only be updated in one way.

The application also initialises some Global Variables that relate to the enemy. These are:
MONSTER_HP, MONSTER_DMG. They both start at a random value but real values are generated fromthe Monster class that appears on each 'encounter'.

The player health is a fixed value but the base damage is a randomised number between differing ranges, depending on the class. The Min/Max Damage values are not stored in a variable as the number is randomised each time the player attacks a monster (see COMBAT)

Some basic information about those values is provided below:

-----------------------
<div align="center">

**Warrior**

<img src="https://images2.imgbox.com/51/e0/Hazk8BwX_o.png" width="320">


HP: 				150

Base Damage:		5 - 7

Min/Max Damage:		6 -31


Generally recommended for first time players, the Warrior provides a good middle ground of health and damage and is generally the class that can survive the longest.

</div>

-----------------------

<div align="center">

**Mage**

<img src="https://images2.imgbox.com/f1/8b/v8D5inMM_o.png" width="320">


HP: 				100

Base Damage:		2 - 13

Min/Max Damage:		3 -24


The mage has less health than the warrior but has a chance to start with higher base damage, making him stronger in combat.
</div>

-----------------------

<div align="center">

**Rogue**

<img src="https://images2.imgbox.com/4a/a5/0BWVZXpy_o.png" width="320">


HP: 				85

Base Damage:		3 - 5

Min/Max Damage:		4 - 50


The Rogue has the lowest health and good base damage but has the chance to do very high damage in combat. Please see notes on combat further

</div>

-----------------------


### - Navigation:

- Players can choose a direction from the terminal menu (up, down, left, right)
- Each time the player selects one of these options, their position in the map is updated using the MAP_GRID variable, which is a dictionary containing the number and name of the location the player is in
- Each time a player enters a new location, a function is called which rolls a virtual dice with 24 'sides'. This returns the encounter variable and if it is over 20 then a monster is spawned. 
- The monster is a random choice from a List of different Subclasses from the Monster Class, which is stored in the monsters.py file.
- The monsters DMG and HP also come from their Subclass in the Monsters.py file and are more static than the Players values but the DMG value is randomised once to represent the strength of that particular monster(can change is that monster is encountered again).
- More information on monsters is provided in the Combat Section.
-----------------------

### - Search

- The player can search the area for items. This calls the search_area function and rolls a virtual 100 sided die. Depending on the score that is returned there is a chance that one of the 6 items will be found. Originally the item was also randomised but this made the game unbalanced as there was a chance for always getting an item and getting the more valuable items. It was therefore changed to be a specific range of scores for certain items, with lowr chances for the the most valuable items.

- The item that triggers the win condition is included in this roll but has a 1% chance to appear

- If an item is found then a new instance is created from is Item class in the items.py file. it is passed some randomised values and then the actual values are generated when the Instanced item is created. The base values for the items properties are stored in the respective subclasses. The values are fixed and then modified by the random value that is passed by the 'randomised_loot_chance' / 'instanced_loot' variable.

- If the dice roll returns a score not listed then it simply returns a generic message

- If an item is created for the player then various messages are displayed to the terminal and the logic for each item is contained within the search function. For example the Health Restore works out if the player is missing any health and only applies if health is missing. The win condition variable is also updated here if the player recieves the corresponding item.

- Once the player finds the sword, the list of options displayed in the terminal are changed and the search is no longer available to them by design. This is to provide a bit of stress if the user is low on HP but has the Sword and prevents them from healing or improving their damage, which also encourages a bit of exploration too.

- This is a duplicate of the main game loop, due to the library being used for the multi-select style terminal, there is not a goods way to edit the options (or at least I wasn'table to find one, trying to manipulate the array in the usual ways ('.pop() etc') didn't work for me.
-----------------------

### - The Map

- The user can look at their map to get an idea of where they are i nrelation to the Sword and the location they are meant to take it to.

- This returns two values forthe location and sword respectively . This is done by subtracting the location from the players current position and converting it to n absolute value using the abs() function to display it as a positive number.

- The user map function also does the same calculation to generate some clues about where to go, without giving too much away. If the player needs to decrease the CURRENT_POSITION value to get closer, it tells them to either go 'West' or 'Up' and if they need to increment the vlaue it will suggest 'East' or 'South' to them. part of the game loop is figurinng out the shape of the map and how this feature works so the players position is reported back to them, but only by name and how far away they are.

-----------------------
### - Items

- As described above, items are found based on using the search command and the score returned from the dice roll function 'legendary_weighted_dice_roll' which gives the items a % chance to appear
- The items are instanced in a similar way to the monsters, by calling a Class and Subclass from the items.py file. Items only have one important value for the player, which is the 'mod_value'. This is the randomised value passed when an item is instanced. The items all have base values to return, which is then added to the randomised value passed, in order to keep the gameplay varied.
- The player receives a message about the item the received and the effect it had.
- The returned value from the subclass is "universal" in that it is just an integer and does not directly update any variables. The item that was generated  in the search function also dictates how the returned value is used. E.g The WeaponUp item adds the returned integer to the players Base Damage, where as the health potions add it to the players health.

The Item stats are here for reference:
<div align="center">

**Small HP Potion**

<img src="https://images2.imgbox.com/1c/60/IcuwPFA8_o.png" width="320">

Restores 6 + d6 HP to the player if they have lost health.
Referred to as "MinorHealthPotion" in the items.py file.

**Regular HP Potion**

<img src="https://images2.imgbox.com/d4/97/SCH0SlMM_o.png" width="320">

Restores 12 + d6 HP to the player if they have lost health.
Referred to as "StandardHealthPotion" in the items.py file.


**HP Restore**

<img src="https://images2.imgbox.com/9c/8c/WOfhUJmg_o.png" width="320">

Restores the players health to whatever their Base HP was. Does not include their new HP value if it has been increase. E.g Warrior starts with 150 so that is the value their health will be set to, even if it has been upgraded.
Referred to as "FullHealthRestore" in the items.py file.


**Max HP Increase**

<img src="https://images2.imgbox.com/7f/53/G5cZJymI_o.png" width="320">

Increases the players max base health by 25%, but does not restore any lost health E.g The Warrior starts with 150 so upon collecting this item his base health becomes 187.5 but the actual HP at the time may be lower. The Character can then heal up to this new maximum value.
Referred to as "MaxHealthUp" in the items.py file.


**Base DMG Increase**

<img src="https://images2.imgbox.com/51/f4/E1JdCa0C_o.png" width="320">

Increases the players max base damage by 6 + d6 (randomised when the item is instanced from the Item > Subclass in the items.py file).
Referred to as "WeaponUp" in the items.py file.


**Umbra Sword**

<img src="https://images2.imgbox.com/74/2f/AO80eKzU_o.png" width="320">

Sets the PLAYER_HAS_WIN_CONDITION variable to true
Referred to as "UmbraSword" in the items.py file and 'OBJECTIVE' in the run.py file.
This item only appears in a specific location and the player must search to obtain it.
The item needs to be brought to the Location indicated by the map.

</div>

-----------------------
### -  Combat

- The once the player_enters_location is called, following them choosing a direction to go in. The dice roll that checks if a monster should spawn updates the players state, stored in a Global variable (PLAYER_ENCOUNTER). Once this is set to True, combat begins and while the Monsters HP is above 0, the functions are called until either the player or the monster is dead.

- A few different conditions were tested for 'being in combat' and although checking if the monsters health is greater than 0 might suggest that the player always wins, the monster does always attack first and the DMG values for monsters are high in some cases so there is enough of a challenge for the player.

- The application replicates the style seen in very early text based games where the combat was resolved automatically when it occurs. The Monster Attacks first, followed by the player.This is acheived via a while loop in the main function, calling 2 different functions in the appropriate order(monster_attack and player_attack). In a future version, I would like to make the combat turn based, using the terminal menu library to allow the aplyer to make choices like "Defend" or have them store items and be able to choose to use them (e.g Pokemon style 'battler' games.)

- The damage the player does is governed by their base damage stat + a dice roll. The dice roll depends on which class the player has selected calling a different function to represent each of these.

- The Players damage is radnomised more than the Monsters damage, to represent "Skill" and a different damage number is generated each time the player attacks the monster.

- Once the player exits combat, they are taken back to the navigation menu. The player is free to search the area again but this will also roll the same dice as entering a new location and there is a chance that another monster will spawn and the combat loop will occur as normal. This is primarily to prevent 'search spamming' in order to find lots of items. It is technically possible but this is a reasonably good deterrent. The win condition was updated specifically for this reason so the Sword item only appears in a certain location.
-----------------------
### - Monster Glossary / Reference

<div align="center">

**Goblin**

<img src="https://images2.imgbox.com/8f/5f/TGCrtfiH_o.png" width="320">

HP:     6 + d6

DMG:    4 + d6


**Rat**

<img src="https://images2.imgbox.com/48/9b/8GyVUw7K_o.png" width="320">

HP:     2 + d6

DMG:    1 + d6


**Zombie**

<img src="https://images2.imgbox.com/38/f3/BgmoDSC4_o.png" width="320">

HP:     15 + d6

DMG:    1 + d6


**Skeleton**

<img src="https://images2.imgbox.com/ee/e8/clBA4xf7_o.png" width="320">

HP:     10 + d6

DMG:    3 + d6


**Dragon**

<img src="https://images2.imgbox.com/4c/08/FAbOvwqv_o.png" width="320">

HP:     75 + d6

DMG:    15 + d6


**Knight**

<img src="https://images2.imgbox.com/06/d6/eYz5x8bf_o.png" width="320">

HP:     25 + d6

DMG:    18 + d6

**Wizard**

<img src="https://images2.imgbox.com/1e/8e/c91PHS7x_o.png" width="320">

HP:     12 + d6

DMG:    16 + d6


**Orc**

<img src="https://images2.imgbox.com/4e/7f/4aYynITn_o.png" width="320">

HP:     20 + d6

DMG:    8 + d6


**Troll**

<img src="https://images2.imgbox.com/5d/05/fmKE6nED_o.png" width="320">

HP:     16 + d6

DMG:    8 + d6


**Giant**

<img src="https://images2.imgbox.com/19/6f/oT1S2YEo_o.png" width="320">

HP:     100 + d6

DMG:    25 + d6

</div>

-----------------------
### - Win Conditions

- The win condition was altered a few times during development but the final version simply requires a player to find the "Umbra Sword" item and return it to its rightful place.
- The Sword spawns in a randomised location inside the MAP_GRID array/dictionary
- The Swords 'Resting Place' is also randomly generated from the same MAP_GRID object
- Once the Sword is returned, the game ends.


----------------------
## TESTING

- The application has had some very thorough testing (approx 700 games!)
- The external libraries used have also been tested in advance in Heroku and there doesnt appear to be any issues. See note about Firefox Compatibility for the Emoji library below.

----------------------
## BUGS

There were a few bugs during development, all of which were resolved by the end of the project. 

There is one small bug but it is harder to replicate. Occasionally when the win condition is met, the player will be attacked by a monster, just after they Win. It has only happened once and not since.

There also seem to be a browser bug in Firefox where the Emoji library icons display as cutoff / split in half. I did try to debug this but the same issue doesnt occur in Chrome/Edge/Safari and doesnt seem to be a known issue with the library so a Chromium/IOS browser is highly recommended, though it doesnt alter the functionality of the application.

----------------------
## DEPLOYMENT

The site was deployed to Heroku following the below steps:
- Using pip freeze > requirements.txt
- I also had to manually find the version of one of the librarys I used and enter it into the requirements file as it would not automatically generate a file with it in. 
- Creating a new App in Heroku
- The app does not use any special config vars or config data 
- The Node JS ands Python Buildpacks were set up from the Buuldpacks submenu (i that order)
- The Github repository was then connected to the 'main' branch

The live link can be found here - [MicroRPG - A Python Adventure](https://ci-project3-mini-rpg.herokuapp.com/)   

----------------------
## CREDITS   

All Readme Iamages generated using Midjourney: https://midjourney.com/home/?callbackUrl=%2Fapp%2F

Simple Terminal Library: https://pypi.org/project/simple-term-menu/

Rich Terminal: https://github.com/Textualize/rich

Emojify: https://pypi.org/project/emoji/


----------------------
## Thoughts / Possible Features / Misc Notes

- There were quite a few additional features that I wanted to implmenent during the project but decided against over complicating things
- A turn based system would be good for the combat loop and I feel like this could be done using the terminal library I have used for the navigation
- A persistent Inventory could be done with a List than is Appended when an item is found. Potentially this would need ot be a disctionary to store unique items and their quantity?
- The game is not that well balanced but provides enough of a challenge that you can be taken out by a large monster or repeated smaller ones
- I would have like to add different attacks or abilities for each monster, which I think could be done within their Subclass and different functions that share parameters/arguments
- Overall I was quite happy with the project as I managed to debug things on my own and didn't have to refer back to many notes throughout and managed to make progress fairly rapidly.
- I thought it would be fun to present the readme in the style of the old Dungeon's and Dragons rule books with Character and Monster Stats and Artwork but tried to make sure plenty of information about the app works was included too.

---------------------