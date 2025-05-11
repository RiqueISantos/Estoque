from utls import estoque
#exemplo de uso !
#-------------------------------------------------------------------------------------------------------------------
estoque.Categoria.adicionar('TEC')

estoque.Marca.adicionar('dell', 1)
estoque.Marca.adicionar('samsung', 1)
estoque.Fornecedor.adicionar('Gilson', '116532456')
estoque.Produto.adicionar('teclado','123','25','h098',1,1)

estoque.Produto.listar_estoque()

estoque.Produto.buscar_por_codigo('123')

estoque.Produto.adicionar('mouse','158','30','h099',1,1)
estoque.Marca.produto_marca('sangsung')

estoque.Fornecedor.produto_fornecedor(1)
estoque.Categoria.marca_categoria('TEC')