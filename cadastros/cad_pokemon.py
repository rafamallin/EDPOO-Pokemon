from models.pokemon import PokemonAliado, PokemonInimigo
from utils.funções_auxiliares import cabecario, pausar
from settings import vars

import time

def cadastrarPokemon():
    cabecario()
    print("Pokemon Aliado".center(50))
    print("-" * 50)

    print(f"\nVocê irá enfrentar o {vars.pokemonsAdversarios[-1].nickname} | Lvl {vars.pokemonsAdversarios[-1].nivel}.")
    print("")
    escolhaPokemon = []

    i = 0
    while i < 3:
        poke = PokemonAliado()
        repetido = False

        for x in escolhaPokemon:
            if x.especie == poke.especie:
                repetido = True

        if not repetido:
            print(f"{i + 1}. {poke}")
            escolhaPokemon.append(poke)
            i += 1

    while True:
        escolha = int(input("\nEscolha o teu pokemon: "))
        if escolha >= 1 and escolha <= 3:
            vars.treinadorCadastrado[-1].pokemonsCadastrados.append(escolhaPokemon[escolha - 1])
            break
        else:
            print("ESCOLHA INVÁLIDA!")

    print("")
    print("Pokémon escolhido com sucesso!")
    print(f"Seu pokemon será: {vars.treinadorCadastrado[-1].pokemonsCadastrados[-1]}")
    pausar()

def cadastrarPokemonAdv():
    cabecario()
    print("Pokemon Adversário".center(50))
    print("-" * 50)
    
    print("O teu pokémon adversário será", end='')
    for i in range(7):
        print(" .", end='', flush=True)
        time.sleep(1)
    
    Poke_adv = PokemonInimigo()
    vars.pokemonsAdversarios.append(Poke_adv)

    print(f"\n{Poke_adv}")
    pausar()