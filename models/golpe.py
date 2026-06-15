from enum import Enum

class Golpe:
    def __init__(self, nome, tipo, categoria, poder=0, precisao=100, PP=10,
                 efeito_secundario=False, condicao=None):
        self.nome = nome
        # self.tipo = tipo
        self.categoria = categoria
        self.poder = poder
        self.precisao = precisao
        self.PP = PP
        self.efeito_secundario = efeito_secundario
        self.condicao = condicao

    def __str__(self):
        return f"{self.nome} Pwr:{self.poder} PP:{self.PP}"
    
class Categoria(Enum):
    FISICO = 1
    ESPECIAL = 2
    STATUS = 3

class Condicoes(Enum):
    POISON = 1
    PARALYSIS = 2
    BURN = 3
    FREEZE = 4
    SLEEP = 5