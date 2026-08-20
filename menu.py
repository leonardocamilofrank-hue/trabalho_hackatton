from funcoes import *

def menu():

    while True:

        print("\n")
        print("=" * 45)
        print("       SISTEMA DE RECICLAGEM")
        print("=" * 45)

        print("1 - Cadastrar item")
        print("2 - Listar itens")
        print("3 - Cadastrar ponto de coleta")
        print("4 - Listar pontos de coleta")
        print("5 - Registrar coleta")
        print("6 - Listar coletas")
        print("7 - Relatório")
        print("8 - Remover item")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_itens()

        elif opcao == "2":
            mostrar_itens()

        elif opcao == "3":
            cadastrar_ponto()

        elif opcao == "4":
            mostrar_pontos()

        elif opcao == "5":
            registrar_coleta()

        elif opcao == "6":
            listar_coletas()

        elif opcao == "7":
            relatorio()

        elif opcao == "8":
            remover_item()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")