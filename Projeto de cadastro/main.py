"""
Docstring:

"""

import menu
import receber
import os

pessoas = []

while True:
    menu.telaMenu()
    opcao = receber.receberInteiro()

    if opcao == 0:
        break
    elif opcao == 1:
         nome = receber.receberString()
         pessoas.append(nome)
         print("Pessoa cadastrada com sucesso!")
         input("Pressione Entre para continuar....")
         os.system('cls')  # Limpa a tela
    elif opcao == 2:
        if not pessoas:
            print("Não há  pessoas cadastrada:")
        else:
            print("Lista de pessoas cadastradas:")
            for pessoa in pessoas:
                print(pessoa)
        input("Pressione Enter para continuar...")
        os.system('cls')

    else:
        print("Opção invalida")
        input("Tecla enter para continuar")
        os.system('cls')
           
















