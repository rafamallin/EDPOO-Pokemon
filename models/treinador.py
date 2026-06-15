import random
from enum import Enum

class Treinador:
    def __init__(self, nome, classe, genero, rematch=False):
        self.nome = nome
        self.classe = classe
        self.genero = genero
        self.rematch = rematch
        self.pokemonsCadastrados = []
        self.itensCadastrados = []
        self.dinheiro = 0

    def __str__(self):
        pokes_str = "\n".join([f"  Slot {i+1}: {p}" for i, p in enumerate(self.pokemons) if p])
        return f"> {self.nome} ({self.classe})\n{pokes_str}"
    
class Classe(Enum):
    YOUNGSTER = 1
    BUG_CATCHER = 2
    LASS = 3
    PICNICKER = 4
    CAMPER = 5
    BIRD_KEEPER = 6
    SAILOR = 7
    CHANNELER = 8
    BLACK_BELT = 9
    HIKER = 10
    SUPER_NERD = 11
    SCIENTIST = 12
    GENTLEMAN = 13
    BEAUTY = 14
    BIKER = 15
    BURGLAR = 16
    SWIMMER = 17
    FISHERMAN = 18
    PSYCHIC = 19
    TAMER = 20
    ROCKET = 21

class Genero(Enum):
    MALE = 1
    FEMALE = 2