from utils.funções_auxiliares import cabecario, pausar, escolher_enum

from models.item import Item
from models.golpe import Condicoes
from settings import vars

def cadastrarItem():
    cabecario()
    print("Itens".center(50))
    print("-" * 50)

    escolhaItem = []
    i = 0

    while i < 8:
        novo_item = Item()
        repetido = False
        for x in escolhaItem:
            if x.nome == novo_item.nome:
                repetido = True

        if not repetido:
            print(f"{i + 1}. {novo_item}")
            escolhaItem.append(novo_item)
            i += 1

    qnt_escolha = 0
    while qnt_escolha < 4:
        while True:
            escolha = int(input(f"\nEscolha o item {qnt_escolha + 1}: "))
            if escolha >= 1 and escolha <= 8:
                vars.treinadorCadastrado[-1].itensCadastrados.append(escolhaItem[escolha - 1])
                qnt_escolha += 1
                break
            else:
                print("ESCOLHA INVÁLIDA!")

    print("\nEscolha de itens feita com sucesso!!")
    print("O seus itens escolhidos foram: ")
    for i, item in enumerate(vars.treinadorCadastrado[-1].itensCadastrados):
        print(f"{i + 1}. {item}")