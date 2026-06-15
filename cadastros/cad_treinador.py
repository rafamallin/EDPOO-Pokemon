from utils.funções_auxiliares import cabecario, limparTela, pausar, escolher_enum

from models.treinador import Treinador, Classe, Genero
from settings import vars

def cadastrarTreinador():
    cabecario()
    print("Cadastro de treinador".center(50))
    print("-" * 50)

    nome = input("Me diga: Qual o teu nome? - ENTRADA: ")
    
    print("\nE de qual classe você quer ser??")
    classe = escolher_enum(Classe)

    print("\nE o teu gênero? Qual é?")
    genero = escolher_enum(Genero)

    tr = Treinador(nome.lower().capitalize(), classe, genero)

    vars.treinadorCadastrado.append(tr)
    print("\nTREINADOR CADASTRADO COM SUCESSO")
    pausar()