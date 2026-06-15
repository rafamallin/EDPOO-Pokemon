import os

# ================= FUNÇÕES AUXILIARES =================

def cabecario():
    limparTela()
    print("=" * 50)
    print("POKEMON".center(50))
    print("=" * 50)

def limparTela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

def escolher_enum(enum_cls):
    """Exibe opções de um Enum e retorna a escolha do usuário"""
    for i, e in enumerate(enum_cls, start=1):
        print(f"{i}. {e.name}")
    while True:
        try:
            escolha = int(input("Escolha: "))
            if 1 <= escolha <= len(enum_cls):
                return list(enum_cls)[escolha - 1]
        except ValueError:
            pass
        print("Opção inválida, tente novamente.")
