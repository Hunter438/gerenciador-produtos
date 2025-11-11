arq = 'produtos.txt'
def editar(produtos):
    listar(produtos)

    try:
        id_produto = int(input('Digite o ID do produto que deseja editar: '))
        pos = id_produto - 1

        if 0 <= pos < len(produtos):
            produto = produtos[pos]

        else:
            print('ID inválido.')
            return

    except ValueError:
        print('Entrada inválida. Digite apenas números.')
        return

    print('\nO que quer editar?')
    print('1 - Nome')
    print('2 - Preço')
    print('3 - Estoque')
    print('0 - Cancelar')

    try:
        opc = int(input('Escolha uma opção: '))
    except ValueError:
        print('Entrada inválida.')
        return

    if opc == 1:
        novo_nome = input('Novo nome: ')
        produto['nome'] = novo_nome
    elif opc == 2:
        try:
            novo_preco = float(input('Novo preço: '))
            produto['preco'] = novo_preco
        except ValueError:
            print('Valor inválido.')
    elif opc == 3:
        try:
            novo_estoque = int(input('Novo estoque: '))
            produto['estoque'] = novo_estoque
        except ValueError:
            print('Valor inválido.')
    elif opc == 0:
        print('Edição cancelada.')
        return
    else:
        print('Opção inválida.')
        return

    with open(arq, 'w') as arquivo:
        for p in produtos:
            arquivo.write(f"{p['nome']};{p['preco']:.2f};{p['estoque']}\n")
    print('\nProduto atualizado com sucesso!\n')
#função para cadastrar produtos
def cadastrar(produtos):
    while True:
        try:
            nome = input('Nome do produto: ')
            preco = float(input('Preço do produto: '))
            estoque = int(input('Estoque: '))
        except (ValueError):
            print('Erro ao tentar cadastrar o produto. Tente novamente')
            continue
        else:
            produto = {
                'nome': nome,
                'preco': preco,
                'estoque': estoque,
            }
            produtos.append(produto)
            print('Produto cadastrado!')
            with open(arq, 'a') as arquivo:
                arquivo.write(f'{nome};{preco};{estoque}\n')
            break
def buscar(produtos):
    termo = input('Digite o nome ou parte do nome do produto: ')
    encontrados = []
    for p in produtos:
        if termo.lower() in p['nome'].lower():
            encontrados.append(p)

    if not encontrados:
        print('Nenhum produto encontrado.')
    else:
        print(f'\nResultados da busca por {termo}: ')
        print(f"{'ID':<4}{'NOME':<15}{'PREÇO':<12}{'ESTOQUE':<10}")
        print('-' * 40)

        for i, item in enumerate(encontrados, start=1):
            print(f"{i:<4}{item['nome']:<15}{item['preco']:<12.2f}{item['estoque']:<10}")
#Função para mostrar lista dos produtos cadastrado
def listar(produtos):
    if not produtos:  #Verifica se a lista tem ou não itens
        print('Nenhum produto cadastrado.')
        return
    print('\nLISTA DE PRODUTOS')
    print(f"{'ID':<4}{'NOME':<15}{'PREÇO':<12}{'ESTOQUE':<10}")
    print('-' * 40)

    #laço para mostrar os itens da lista
    for i, p in enumerate(produtos, start=1):
        print(f"{i:<2}. {p['nome']:<15} {p['preco']:<12.2f} {p['estoque']:<10}")
    print('-' * 40)

#função para remover
def remover(produtos):
    if not produtos:
        print('Não existem produtos para remover.')
        return
    listar(produtos)
    try:
        pos = int(input('Digite o ID do produto que deseja remover: ')) - 1
        if 0 <= pos < len(produtos):
            produto_removido = produtos.pop(pos)
            print(f"{produto_removido['nome']} foi removido com sucesso!")

            with open(arq, 'w') as arquivo:
                for p in produtos:
                    arquivo.write(f"{p['nome']};{p['preco']};{p['estoque']}\n")
        else:
            print('Número inválido')
    except ValueError:
        print('Entrada inválida. Digite apenas números.')
def menu():
    print('-' * 30)
    print('GERENCIADOR DE PRODUTOS')
    print('-' * 30)
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Remover produto')
    print('4 - Buscar produto')
    print('5 - Editar produto')
    print('6 - Ordenar produtos')
    print('0 - Sair')


def carregar(produtos):
    try:
        with open(arq, 'r') as arquivo:
            for linha in arquivo:
                nome, preco, estoque = linha.strip().split(';')
                produto = {
                    'nome': nome,
                    'preco': float(preco),
                    'estoque': int(estoque)
                }
                produtos.append(produto)
    except FileNotFoundError:
        open(arq, 'a').close()

def ordenar(produtos):
    print('Como quer ordenar? ')
    print('1 - Por nome (A -> Z)')
    print('2 - Por preço (menor -> maior)')
    print('3 - Por estoque (maior -> menor)')
    print('0 - Cancelar')

    try:
        opc = int(input('Escolha uma opção: '))
    except ValueError:
        print('Entrada inválida.')
        return

    if opc == 0:
        print('Operação cancelada.')
        return
    if opc == 1:
        produtos_ordenados = sorted(produtos, key=lambda p: p['nome'])
    elif opc == 2:
        produtos_ordenados = sorted(produtos, key=lambda p: p['preco'])
    elif opc == 3:
        produtos_ordenados = sorted(produtos, key=lambda p: p['estoque'], reverse=True)
    else:
        print('Opção inválida.')
        return

    print('\nPRODUTOS ORDENADOS: ')
    print(f"{'ID':<4}{'NOME':<15}{'PREÇO':<12}{'ESTOQUE':<10}")
    print('-' * 40)

    for i, p in enumerate(produtos_ordenados, start=1):
        print(f"{i:<4}{p['nome']:<15}{p['preco']:<12.2f}{p['estoque']:<10}")