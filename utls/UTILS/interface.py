import utls.UTILS.estoque as e
from utls.UTILS.estoque import Produto, Fornecedor, ler_texto, ler_inteiro, texto_num
import os
def limpa_tela():
    os.system('cls')
    return


def interface():
        while True:
            limpa_tela()
            print('Digite o menu que deseja acessar:')
            numero = ler_inteiro('1 - Fornecedor \n2 - Categoria \n3 - Marca \n4 - Produto \n5 - Estoque\n',1,5)
            if numero == 1:
                limpa_tela()
                fornecedor = ler_inteiro('1- Adicionar Fornecedor \n2- Listar todos os produtos do fornecedor pelo id\n3- Atualizar contato do fornecedor\n', 1, 3)
                if fornecedor == 1:
                    limpa_tela()
                    nome = ler_texto('Insira o nome do fornecedor: ', 1, 50).capitalize()
                    cpf = ler_inteiro(f'Insira o CPF de {nome}', 11,11)
                    contato = ler_inteiro('insira o numero para contato com o fornecedor: ', 11,11)
                    fornecedor = Fornecedor(nome,contato,cpf)
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

                categoria = ler_inteiro('1- Adicionar uma categoria \n2- Marcas por categoria\n', 1, 2)
                if categoria == 1:
                    limpa_tela()
                    e.Categoria.adicionar()
                    input('\nPressione Enter para continuar')
                    limpa_tela()
                elif categoria == 2:
                    limpa_tela()
                    e.Categoria.marca_categoria()
                    input('\nPressione Enter para continuar')
                    limpa_tela()

            elif numero == 3:
                    limpa_tela()
                    marca = ler_inteiro('1- Adicionar uma marca \n2- Produtos por marca\n3- Listar marcas\n', 1, 3)
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
                        e.Categoria.marca_categoria()
                        input('\nPressione Enter para continuar...')

            elif numero == 4:
                limpa_tela()
                produto = ler_inteiro('1- Adicionar produto \n2- Remover produto \n3- Busca específica\n', 1, 3)
                if produto == 1:
                    limpa_tela()
                    nome_produto = ler_texto('Nome do produto: ',2,50).capitalize()
                    qtd = ler_inteiro('Quantidade:',1)
                    lote = texto_num('Número do Lote:',3,50).upper()
                    limpa_tela()
                    e.Estoque.mostrar_fornecedores()
                    fornecedor = ler_inteiro('Digite o codigo do fornecedor deste produto: ',1,100)
                    limpa_tela()

                    e.Categoria.marca_categoria()
                    marca = ler_inteiro('Digite o codigo da marca do produto: ',1,100)
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
                estoque = ler_inteiro('1- Listar estoque\n2- Listar fornecedores\n', 1, 2)
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
