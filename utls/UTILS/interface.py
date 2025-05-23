import utls.UTILS.estoque as e
from utls.UTILS.estoque import Produto, Fornecedor, ler_texto, ler_inteiro
import os
def limpa_tela():
    print(os.system('cls'))
    return


def interface():
    while True:
        limpa_tela()
        numero = int(input('1 - Fornecedor \n2 - Categoria \n3 - Marca \n4 - Produto \n5 - Estoque\n'))
        if numero == 1:
            limpa_tela()
            fornecedor = int(input('1- adicionar Fornecedor \n2- Listar todos os produtos do fornecedor pelo id\n3- Mudar contato fornecedor\n'))
            if fornecedor == 1:
                nome = ler_texto('Insira o nome do fornecedor: ', 1, 50)
                contato = ler_inteiro('insira o numero para contato com o fornecedor: ', 11,11)
                fornecedor = Fornecedor(nome,contato)
                limpa_tela()
                fornecedor.adicionar()
                input('pressione Enter para continuar...')
            elif fornecedor == 2:
                limpa_tela()
                e.Fornecedor.produto_fornecedor()
                input('pressione Enter para continuar...')
                limpa_tela()

            elif fornecedor == 3:
                limpa_tela()
                e.Fornecedor.atualiza_contato()
                input('pressione Enter para continuar...')
                limpa_tela()
        elif numero == 2:
            limpa_tela()
            categoria = int(input('1- Adicionar uma categoria \n2- Marcas por categoria\n'))
            if categoria == 1:
                limpa_tela()
                e.Categoria.adicionar()
                input('Pressione Enter para continuar')
                limpa_tela()

            elif categoria == 2:
                limpa_tela()
                e.Categoria.marca_categoria()
                input('Pressione Enter para continuar')
                limpa_tela()

        elif numero == 3:
            limpa_tela()
            marca = int(input('1- Adicionar uma marca \n2- Produtos por marca\n'))
            if marca == 1:
                limpa_tela()
                e.Marca.adicionar()
                input('pressione Enter para continuar...')
                limpa_tela()

            if marca == 2:
                limpa_tela()
                e.Marca.produto_marca()
                input('pressione Enter para continuar...')
                limpa_tela()

        elif numero == 4:
            limpa_tela()
            produto = int(input('1- Adicionar produto \n2- Remover produto \n3- buscar especifica\n'))
            if produto == 1:
                limpa_tela()
                nome_produto = input('nome do produto: ')
                qtd = int(input('quantidade: '))
                lote = input('codigo do lote: ')
                fornecedor = int(input('Digite o codigo do fornecedor: '))
                marca = int(input('Digite o codigo da marca do produto: '))
                novo_produto = Produto(
                    nome=nome_produto,
                    qtd=qtd,
                    lote=lote,
                    fornecedor_id=fornecedor,
                    marca_id=marca
                )

                novo_produto.adicionar()
                input('pressione Enter para continuar...')
                limpa_tela()

            elif produto == 2:
                limpa_tela()
                e.Produto.remover()


                input('pressione Enter para continuar...')
                limpa_tela()

            elif produto == 3:
                limpa_tela()
                e.Produto.buscar_por_codigo()
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

