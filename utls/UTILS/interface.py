import utls.UTILS.estoque as e
from utls.UTILS.estoque import Produto, Fornecedor, ler_texto, ler_inteiro
import os
def limpa_tela():
    os.system('cls')
    return


def interface():
    while True:
        limpa_tela()
        print('Digite o menu que deseja acessar:')
        numero = int(input('1 - Fornecedor \n2 - Categoria \n3 - Marca \n4 - Produto \n5 - Estoque\n'))
        if numero == 1:
            limpa_tela()
            fornecedor = int(input('1- Adicionar Fornecedor \n2- Listar todos os produtos do fornecedor pelo id\n3- Mudar contato fornecedor\n'))
            if fornecedor == 1:
                limpa_tela()
                nome = ler_texto('Insira o nome do fornecedor: ', 1, 50).capitalize()
                contato = ler_inteiro('insira o numero para contato com o fornecedor: ', 11,11)
                fornecedor = Fornecedor(nome,contato)
                fornecedor.adicionar()
                input('\nPressione Enter para continuar...')
            elif fornecedor == 2:
                limpa_tela()
                e.Estoque.mostrar_fornecedores()
                e.Fornecedor.produto_fornecedor()
                input('\nPressione Enter para continuar...')
                limpa_tela()

            elif fornecedor == 3:
                limpa_tela()
                e.Estoque.mostrar_fornecedores()
                e.Fornecedor.atualiza_contato()
                input('\nPressione Enter para continuar...')
                limpa_tela()
        elif numero == 2:
            limpa_tela()
            categoria = int(input('1- Adicionar uma categoria \n2- Marcas por categoria\n'))
            if categoria == 1:
                limpa_tela()
                e.Categoria.adicionar()
                input('\nPressione Enter para continuar')
                limpa_tela()

            elif categoria == 2:
                limpa_tela()
                e.Estoque.listar_categorias()
                e.Categoria.marca_categoria()
                input('\nPressione Enter para continuar')
                limpa_tela()

        elif numero == 3:
            limpa_tela()
            marca = int(input('1- Adicionar uma marca \n2- Produtos por marca\n3- Listar marcas\n'))
            if marca == 1:
                limpa_tela()
                e.Marca.adicionar()
                input('\nPressione Enter para continuar...')
                limpa_tela()

            if marca == 2:
                limpa_tela()
                e.Marca.produto_marca()
                input('\nPressione Enter para continuar...')
                limpa_tela()

            if marca == 3:
                limpa_tela()
                input('FUNÇÃO NÃO CADASTRADA')
            
            

        elif numero == 4:
            limpa_tela()
            produto = int(input('1- Adicionar produto \n2- Remover produto \n3- Busca específica\n'))
            if produto == 1:
                limpa_tela()
                nome_produto = input('nome do produto: ').capitalize()
                qtd = int(input('quantidade: '))
                lote = input('codigo do lote: ').upper()
                limpa_tela()
                e.Estoque.mostrar_fornecedores()
                fornecedor = int(input('Digite o codigo do fornecedor deste produto: '))
                limpa_tela()

                e.Estoque.listar_categorias()
                
                e.Categoria.marca_categoria()
                marca = int(input('Digite o codigo da marca do produto: '))
                novo_produto = Produto(
                    nome=nome_produto,
                    qtd=qtd,
                    lote=lote,
                    fornecedor_id=fornecedor,
                    marca_id=marca
                )

                novo_produto.adicionar()
                input('\nPressione Enter para continuar...')
                limpa_tela()

            elif produto == 2:
                limpa_tela()
                e.Estoque.listar_estoque()
                e.Produto.remover()


                input('\nPressione Enter para continuar...')
                limpa_tela()

            elif produto == 3:
                limpa_tela()
                e.Produto.buscar_por_nome()
                input('\nPressione Enter para continuar...')
                limpa_tela()

        elif numero == 5:
            limpa_tela()
            estoque = int(input('1- Listar estoque\n2- Listar fornecedores\n'))
            if estoque == 1:
                limpa_tela()
                e.Estoque.listar_estoque()
                input('\nPressione Enter para continuar...')
                limpa_tela()
            elif estoque == 2:
                limpa_tela()
                e.Estoque.mostrar_fornecedores()
                input('\nPressione Enter para continuar...')
                limpa_tela()

