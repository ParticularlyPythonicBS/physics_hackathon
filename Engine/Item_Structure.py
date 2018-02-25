import numpy as np
import numpy.random as random
import game_functions as game
from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, Item_Name, **kwargs):
        pass

class Equippable(Item):
    def __init__(self, owner):
        pass

    @abstractmethod
    def equip(character):
        pass

    @abstractmethod
    def unequip(character):
        pass


class Consumable(Item):
    def __init__(self):
        pass

    def consume(character):
        pass

class Weapon(Equippable):
    def __init__(self, **kwargs):
        self.one_handed=False
        self.two_handed=False


class Armor(Equippable):
    def __init__(self):
        pass

class Shield(Equippable):
    def __init__(self):
        pass

