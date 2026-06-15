from utils.funções_auxiliares import cabecario, limparTela, pausar

from cadastros.cad_golpe import cadastrarGolpe
from cadastros.cad_item import cadastrarItem
from cadastros.cad_pokemon import cadastrarPokemon, cadastrarPokemonAdv
from cadastros.cad_treinador import cadastrarTreinador
from cadastros. vizualizacao import visualizarDados
from settings import vars

# ================= MAIN =================

def main():
    opcao = -1
    while opcao != 0:
        #================
        #  TELA INICIAL
        #================
        cabecario()
        print("Seja bem vindo!!".center(50))
        print("-" * 50)
        print("Vamos cadastrar o seu treinador para iniciar o Jogo! :)")
        pausar()

        #=======================
        #  CADASTRAR TREINADOR
        #=======================
        cadastrarTreinador()

        #===========================
        #  GERA POKEMON ADVERSÁRIO
        #===========================
        cabecario()
        print("Pkemon adversário".center(50))
        print("-" * 50)
        print(f"{vars.treinadorCadastrado[-1].nome}, iremos te mostrar agora o teu pokmeon adversário!")
        print("Após isso, você poderá escolher o Pokémon para utilizar na batalha!")
        pausar()
        
        cadastrarPokemonAdv()

        #==========================
        #  ESCOLHA POKEMON ALIADO
        #==========================
        cabecario()
        print("Pokemon Aliado".center(50))
        print("-" * 50)
        print(f"{vars.treinadorCadastrado[-1].nome}, você precisa derrotar o incrível {vars.pokemonsAdversarios[-1].nickname} | Lvl {vars.pokemonsAdversarios[-1].nivel}!")
        print("Iremos te dar 3 opções de Pokémons. Escolha com sabedoria qual irá usar!")
        pausar()

        cadastrarPokemon()  

        #=====================
        #  ESCOLHA DOS ITENS
        #=====================
        cabecario()
        print("Itens".center(50))
        print("-" * 50)
        print(f"{vars.treinadorCadastrado[-1].nome}, agora iremos te mostrar 8 itens.")
        print(f"Escolha 4 para usar na batalha.")
        pausar()

        cadastrarItem()     

        # print("1. Cadastrar Golpe")
        # print("2. Cadastrar Item")
        # print("3. Cadastrar Pokémon")
        # print("4. Cadastrar Treinador")
        # print("5. Visualizar Cadastros")
        # print("0. Sair")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            opcao = -1

        if opcao == 1:
            cadastrarGolpe()
        elif opcao == 2:
            cadastrarItem()
        elif opcao == 3:
            cadastrarPokemon()
        # elif opcao == 4:
            
        elif opcao == 5:
            visualizarDados()
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção inválida!")
            pausar()

if __name__ == "__main__":
    main()