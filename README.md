Gerenciador de Produtos (Python)

Sistema simples de gerenciamento de produtos feito em Python.
Utiliza arquivos .txt como banco de dados, trabalha com listas + dicionários, e agora possui:

✅ cadastro
✅ listagem
✅ remoção
✅ busca
✅ edição
✅ ordenação
✅ modularização (funções separadas em arquivo externo)

Funcionalidades
1. Cadastrar produtos

O usuário informa:

Nome

Preço

Estoque

Os dados são salvos em um arquivo produtos.txt e também carregados na lista durante a execução.

2. Listar produtos

Exibe a tabela:

ID   NOME            PREÇO       ESTOQUE
1    Mouse           70.00       10
2    Teclado         150.00      5


Com formatação alinhada.

3. Remover produtos

Remove um produto usando o ID.
Após remover, o arquivo é reescrito com os itens atualizados.

4. Buscar produtos

Busca por parte ou pelo nome completo.

Exemplo:

Pesquisar por "mo":

Resultados da busca:
1   Mouse        70.00      10

5. Editar produtos

Permite alterar:

Nome

Preço

Estoque

E grava automaticamente no arquivo.

6. Ordenar produtos

Opção para ordenar por:

✅ Nome (A → Z)
✅ Preço (menor → maior)
✅ Estoque (maior → menor)

Usa sorted() e lambda, deixando tudo ordenado sem alterar a lista original.

Tecnologias usadas

Python 3

Manipulação de arquivos (open)

Listas e dicionários

Funções e modularização

Manipulação de exceções (try/except)

Ordenação com sorted, lambda e reverse=True

Como executar

No terminal:

python gerenciador_produtos.py
