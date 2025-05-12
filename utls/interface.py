import utls.estoque as e
import os
def limpa_tela():
    print(os.system('cls'))


def interface():
    while True:
        numero = int(input('1 - Fornecedor \n2 - Categoria \n3 - Marca \n4 - Produto \n5 - Estoque\n'))
        if numero == 1:
            limpa_tela()
            fornecedor = int(input('1- adicionar Fornecedor \n2- Listar todos os produtos do fornecedor pelo id\n'))
            if fornecedor == 1:
                limpa_tela()
                nome = input('Insira o nome do fornecedor: ')
                contato = input('insira o numero para contato com o fornecedor: ')
                e.Fornecedor.adicionar(nome,contato)
            elif fornecedor == 2:
                limpa_tela()
                numero_fornecedor = int(input('Digite o número do id do fornecedor que você queira consultar: '))
                e.Fornecedor.produto_fornecedor(numero_fornecedor)
                input('pressione Enter para continuar...')
                limpa_tela()

        elif numero == 2:
            limpa_tela()
            categoria = int(input('1- Adicionar uma categoria \n2- Marcas por categoria\n'))
            if categoria == 1:
                nome_categoria = input('Nome da categoria: ')
                e.Categoria.adicionar(nome_categoria)
                input('Pressione Enter para continuar')
                limpa_tela()

            elif categoria == 2:
                nome_cat = input('Insira o nome da categoria que você deseja: ')
                e.Categoria.marca_categoria(nome_cat)
                input('Pressione Enter para continuar')
                limpa_tela()

        elif numero == 3:
            limpa_tela()
            marca = int(input('1- Adicionar uma marca \n2- Produtos por marca\n'))
            if marca == 1:
                nome_marca = input('Insira o nome da marca: ')
                numero_categoria = int(input(f'Insira o numero da categoria que deseja incluir a {nome_marca}: '))
                e.Marca.adicionar(nome_marca,numero_categoria)
                input('pressione Enter para continuar...')
                limpa_tela()

            if marca == 2:
                nome_marca2 = input('Digite o nome da marca que deseja ver os produtos: ')
                e.Marca.produto_marca(nome_marca2)
                input('pressione Enter para continuar...')
                limpa_tela()

        elif numero == 4:
            limpa_tela()
            produto = int(input('1- Adicionar produto \n2- Remover produto \n3- buscar especifica\n'))
            if produto == 1:
                limpa_tela()
                nome_produto = input('nome do produto: ')
                codigo_produto = input('codigo do produto: ')
                qtd = int(input('quantidade: '))
                lote = input('codigo do lote: ')
                fornecedor = int(input('Digite o codigo do fornecedor: '))
                marca = int(input('Digite o codigo da marca do produto: '))
                e.Produto.adicionar(nome_produto,codigo_produto,qtd,lote,fornecedor,marca)
                input('pressione Enter para continuar...')
                limpa_tela()

            elif produto == 2:
                limpa_tela()
                id = int(input('digite o id do produto para remover: '))
                e.Produto.remover(id)
                input('pressione Enter para continuar...')
                limpa_tela()

            elif produto == 3:
                limpa_tela()
                codigo_p = input('insira o codigo do produto: ')
                e.Produto.buscar_por_codigo(codigo_p)
                input('pressione Enter para continuar...')
                limpa_tela()

        elif numero == 5:
            limpa_tela()
            estoque = input('1- listar estoque\n2- listar fornecedores\n')
            if estoque == '1':
                limpa_tela()
                e.Estoque.listar_estoque()
                input('pressione Enter para continuar...')
                limpa_tela()
            elif estoque == '2':
                limpa_tela()
                e.Estoque.mostrar_fornecedores()
                input('pressione Enter para continuar...')
                limpa_tela()

