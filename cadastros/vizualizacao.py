from utils.funções_auxiliares import limparTela, pausar

from settings import vars

# ================= VISUALIZAÇÃO =================

def visualizarDados():
    limparTela()
    print("=== DADOS GERAIS ===\n")

    print("[GOLPES]")
    for g in vars.golpesCadastrados:
        print("-", g)

    # print("\n[ITENS]")
    # for i in vars.itensCadastrados:
    #     print("-", i)

    print("\n[POKÉMONS]")
    for p in vars.treinadorCadastrado[-1].pokemonsCadastrados:
        print("-", p)

    print("\n[TREINADORES]")
    for t in vars.treinadorCadastrado:
        print(t)

    pausar()