from utls import estoque

estoque.Fornecedor.adicionar_fornecedor('Peladin', '40028922')
estoque.Produto.listar_estoque()
estoque.Produto.buscar_por_codigo('TECL01')
estoque.Produto.listar_estoque()