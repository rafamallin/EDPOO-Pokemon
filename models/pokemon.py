from enum import Enum
import random
import math

from settings.base import *
from settings.tipos import tipos

def calcular_hp(base, iv, ev, level):
    hp = math.floor(((2 * base + iv + math.floor(ev / 4)) * level) / 100) + level + 10
    return hp

def calcular_status(base, iv, ev, level):
    stauts = math.floor(((2 * base + iv + math.floor(ev / 4)) * level) / 100) + 5
    return stauts

class Pokemon:
    def __init__(self):
        self.especie = random.choice(list(Especie))
        self.nickname = self.especie.name
        self.tipo = tipos[self.especie.name]
        
        if self.especie.value <= 5:
            self.nivel = random.randint(1, 15)
        else:
            self.nivel = random.randint(16, 35)

        self.hp = calcular_hp(
            hp_base[self.especie.name],
            random.randint(0, 31), 
            random.randint(0, 255), 
            self.nivel
        )

        self.attack = calcular_status(
            attack_base[self.especie.name],
            random.randint(0, 31),
            random.randint(0, 255),
            self.nivel
        )

        self.defense = calcular_status(
            defense_base[self.especie.name],
            random.randint(0, 31),
            random.randint(0, 255),
            self.nivel
        )

        self.spAttack = calcular_status(
            sp_attack_base[self.especie.name],
            random.randint(0, 31),
            random.randint(0, 255),
            self.nivel
        )

        self.spDefense = calcular_status(
            sp_defense_base[self.especie.name],
            random.randint(0, 31),
            random.randint(0, 255),
            self.nivel
        )

        self.speed = calcular_status(
            speed_base[self.especie.name],
            random.randint(0, 31),
            random.randint(0, 255),
            self.nivel
        )

        if random.randint(1, 4096) == 1:
            self.shiny = True
        else:
            self.shiny = False

        self.golpes = []

    def __str__(self):
        return (f"{self.nickname} | Lvl:{self.nivel} "
                f"[HP: {self.hp} - ATK: {self.attack} - DEF: {self.defense} | "
                f"SATK: {self.spAttack} - SDEF: {self.spDefense} - SPD: {self.speed} | "
                f"Tipo: {', '.join([str(x) for x in self.tipo])} | "
                f"Shiny: {'Sim' if self.shiny else 'Não'}]")
    
class PokemonAliado(Pokemon):
    def __init__(self):
        super().__init__()

    def subirNivel(self):
        if self.nivel >= 100:
            print("Está no nível máximo")
        else:
            self.nivel += 1
            self.hp += 1
            self.attack += 1
            self.spAttack += 1
            self.defense += 1
            self.spDefense += 1
            self.speed += 1

    def aprenderAtaque(self, ataque):
        self.golpes.append(ataque)
    
class PokemonInimigo(Pokemon):
    def __init__(self):
        super().__init__()
    
class Especie(Enum):
    BULBASAUR = 1
    CHARMANDER = 2
    SQUIRTLE = 3
    ODDISH = 4
    POLIWAG = 5
    IVYSAUR = 6
    CHARMELEON = 7
    WARTORTLE = 8
    GLOOM = 9
    POLIWHIRL = 10