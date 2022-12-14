# ENEMY_LIST = [Goblin, Rat, Skeleton, Zombie, Dragon, Knight, Wizard, Orc, Troll, Giant ]
class Loot():
    """Creates an instance of Loot"""
    def __init__(self, name, mod_value):
        self.name = name
        self.mod_value = mod_value

    def calculate_mod_value(self):
        """
        Returns Loots HP
        """
        return self.mod_value


class MinorHealthPotion(Loot):
    """Creates an instance of Minor HP Potion and sets the the Restore value"""
    def __init__(self, name, mod_value):
        super().__init__(name, mod_value)
        self.name = "Minor HP Potion"
        self.mod_value = 6 + mod_value


class StandardHealthPotion(Loot):
    """Creates an instance of Standard HP Potion and sets the Restore value"""
    def __init__(self, name, mod_value):
        super().__init__(name, mod_value)
        self.name = "Standard HP Potion"
        self.mod_value = 2 + mod_value


class FullHealthRestore(Loot):
    """Creates an instance of Full HP Restore: This sets the players health back to its default"""
    def __init__(self, name, mod_value):
        super().__init__(name, mod_value)
        self.name = "Full HP Restore"
        self.mod_value = 15 + mod_value


class MaxHealthUp(Loot):
    """Creates an instance of Max Health Up and sets the unique HP/DMG values"""
    def __init__(self, name, mod_value):
        super().__init__(name, mod_value)
        self.name = "Max Health Up"
        self.mod_value = 10 + mod_value


class WeaponUp(Loot):
    """Creates an instance of Dragon and sets the unique HP/DMG values""" 
    def __init__(self, name, mod_value):
        super().__init__(name, mod_value)
        self.name = "Weapon Upgrade"
        self.mod_value = 6 + mod_value


class UmbraSword(Loot):
    """
    Creates an instance of UmbraSword and sets the unique HP/DMG values
    This is items that triggers part of the win condition
    """ 
    def __init__(self, name, mod_value):
        super().__init__(name, mod_value)
        self.name = "Umbra Sword"
        self.mod_value = 25 + mod_value