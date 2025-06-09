# filepath: c:\Users\PcAlex\Desktop\atividadePy\Sistema_Estoque.py
#SISTEMA DE ESTOQUE
#Menu principal
import interface

def menu():
    while True:
        print("\n ---- MENU ESTOQUE ---- ")
        print("1 - Adicionar item: ")
        print("2 - Listar estoque: ")
        print("3 - Alterar item: ")
        print("4 - Excluir item: ")
        print("0 - Sair do Sistema")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            print("Função de adicionar item ainda não implementada na interface.")
        elif (opcao == "2"):
            print("Função de listar estoque ainda não implementada na interface.")
        elif (opcao == "3"):
            print("Função de alterar item ainda não implementada na interface.")
        elif (opcao == "4"):
            print("Função de excluir item ainda não implementada na interface.")
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")

menu()