from time import sleep
from funcoes import cadastrar, listar, remover, buscar, editar, carregar, menu, ordenar
produtos = []
arq = 'produtos.txt'


carregar(produtos)

while True:
    menu()
    try:
        opc = int(input('Escolha uma opção: '))
    except (ValueError, TypeError):
        print('Opção inválida. Escolha uma opção: ')
        continue

    if opc == 0:
        print('Volte sempre!')
        break
    elif opc == 1:
        cadastrar(produtos)
        sleep(1)
    elif opc == 2:
        listar(produtos)
        sleep(1)
    elif opc == 3:
        remover(produtos)
        sleep(1)
    elif opc == 4:
        buscar(produtos)
        sleep(1)
    elif opc == 5:
        editar(produtos)
        sleep(1)
    elif opc == 6:
        ordenar(produtos)
        sleep(1)
    else:
        print('Opção inválida! Tente novamente: ')
        break