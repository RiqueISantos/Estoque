from utls import estoque
#exemplo de uso !
#-------------------------------------------------------------------------------------------------------------------
estoque.Categoria.adicionar_categoria('TEC')

estoque.Fornecedor.adicionar_fornecedor('Gilson', '116532456')

estoque.Produto.adicionar_produto('teclado', '123', 25, 'h098',1, 1)

estoque.Produto.listar_estoque()

estoque.Produto.buscar_por_codigo('123')