from enum import Enum
import random

from settings.itens_status import *

class Item:
    def __init__(self):
        self.nome = random.choice(list(Itens))
        self.tipo = item_categoria[self.nome.name]
        self.hp_restore = hp_restore[self.nome.name]
        self.heal_status = heal_stauts[self.nome.name]

    def __str__(self):
        return f"{self.nome.name.replace("_", " ")} ({self.tipo.replace("_", " ")})"

class Itens(Enum):
    POTION = 1
    SUPER_POTION = 2
    HYPER_POTION = 3
    MAX_POTION = 4
    ANTIDOTE = 5
    PARALYZE_HEAL = 6
    AWAKENING = 7
    BURN_HEAL = 8
    ICE_HEAL = 9
    FULL_HEAL = 10