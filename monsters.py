# ENEMY_LIST = [Goblin, Rat, Skeleton, Zombie, Dragon, Knight, Wizard, Orc, Troll, Giant ]
class Monster():
    """Creates an instance of Monster"""
    def __init__(self, name, monster_hp, base_dmg):
        self.name = name
        self.monster_hp = monster_hp
        self.base_dmg = base_dmg

    def calculate_monster_hp(self):
        """
        Returns Monsters HP
        """
        return self.monster_hp


class Goblin(Monster):
    """Creates an instance of Goblin and sets the unique HP/DMG values"""
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Goblin"
        self.monster_hp = 6 + monster_hp
        self.base_dmg = 4 + base_dmg


class Rat(Monster):
    """Creates an instance of Rat and sets the unique HP/DMG values"""
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Rat"
        self.monster_hp = 2 + monster_hp
        self.base_dmg = 1 + base_dmg


class Zombie(Monster):
    """Creates an instance of Zombies and sets the unique HP/DMG values"""
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Zombie"
        self.monster_hp = 15 + monster_hp
        self.base_dmg = 1 + base_dmg

class Dragon(Monster):
    """Creates an instance of Dragon and sets the unique HP/DMG values""" 
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Dragon"
        self.monster_hp = 75 + monster_hp
        self.base_dmg = 15 + base_dmg


class Knight(Monster):
    """Creates an instance of Knight and sets the unique HP/DMG values""" 
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Knight"
        self.monster_hp = 25 + monster_hp
        self.base_dmg = 18 + base_dmg


class Wizard(Monster):
    """Creates an instance of Wizard and sets the unique HP/DMG values""" 
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Wizard"
        self.monster_hp = 12 + monster_hp
        self.base_dmg = 16 + base_dmg


class Orc(Monster):
    """Creates an instance of Orc and sets the unique HP/DMG values""" 
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Orc"
        self.monster_hp = 20 + monster_hp
        self.base_dmg = 8 + base_dmg


class Troll(Monster):
    """Creates an instance of Troll and sets the unique HP/DMG values""" 
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Troll"
        self.monster_hp = 16 + monster_hp
        self.base_dmg = 8 + base_dmg


class Giant(Monster):
    """Creates an instance of Giant and sets the unique HP/DMG values""" 
    def __init__(self, name, monster_hp, base_dmg):
        super().__init__(name, monster_hp, base_dmg)
        self.name = "Giant"
        self.monster_hp = 100 + monster_hp
        self.base_dmg = 35 + base_dmg

        
