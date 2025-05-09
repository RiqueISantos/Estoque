import datetime

from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Configuração do banco
db = create_engine('sqlite:///estoque.db')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

# -------------------------------
class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    contato = Column(String)

    produtos = relationship('Produto', backref='fornecedor')  # corrigido: backref singular

    @staticmethod
    def adicionar(nome, contato):
        fornecedor = Fornecedor(nome=nome, contato=contato)
        session.add(fornecedor)
        session.commit()
        print(f'O fornecedor {nome} foi adicionado')

    @staticmethod
    def produto_fornecedor(id_fornecedor):
        fornecedor = session.query(Fornecedor).filter_by(id=id_fornecedor).first()
        if not fornecedor:
            print(f'Fornecedor com id {id_fornecedor} não cadastrado no sistema')
            return
        print(f'Produtos do {fornecedor.nome}:')
        for produto in fornecedor.produtos:
            print(f'{produto.nome} - lote: {produto.lote}')


# -------------------------------
class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

    marcas = relationship('Marca', backref='categoria')  # Corrigido: nome correto e backref ajustado

    @staticmethod
    def adicionar(nome):
        categoria = Categoria(nome=nome)
        session.add(categoria)
        session.commit()
        print(f'Categoria {nome} foi adicionada')

    @staticmethod
    def marca_categoria(nome_categoria):
        categoria = session.query(Categoria).filter_by(nome=nome_categoria).first()
        if not categoria:
            print(f'Nenhuma categoria com o nome {nome_categoria}')
            return
        print(f'Todas as marcas com a categoria {nome_categoria}:')
        for marca in categoria.marcas:
            print(marca.nome)


# -------------------------------
class Marca(Base):
    __tablename__ = 'marca'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String)
    id_categoria = Column(Integer, ForeignKey('categorias.id'))

    produtos = relationship('Produto', backref='marca')

    @staticmethod
    def adicionar(nome, id_categoria):
        marca = Marca(nome=nome, id_categoria=id_categoria)
        session.add(marca)
        session.commit()
        print(f'A marca {nome} foi adicionada')

    @staticmethod
    def produto_marca(nome_marca):
        marca = session.query(Marca).filter_by(nome=nome_marca).first()
        if not marca:
            print(f'A marca {nome_marca} não está registrada no sistema')
            return
        print(f'Produtos da marca {nome_marca}:')
        for produto in marca.produtos:
            print(f'{produto.nome} - {produto.codigo}')


# -------------------------------
class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    codigo = Column(String, unique=True)
    qtd = Column(Integer)
    lote = Column(String)
    data_entrada = Column(Date, default=datetime.date.today)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    marca_id = Column(Integer, ForeignKey('marca.id'))

    @staticmethod
    def adicionar(nome, codigo, qtd, lote, fornecedor_id, marca_id, data_entrada=None):
        if data_entrada is None:
            data_entrada = datetime.date.today()
        produto = Produto(
            nome=nome,
            codigo=codigo,
            qtd=qtd,
            lote=lote,
            data_entrada=data_entrada,
            fornecedor_id=fornecedor_id,
            marca_id=marca_id
        )
        session.add(produto)
        session.commit()
        print(f"Produto {nome} adicionado com sucesso!")

    @staticmethod
    def remover(codigo):
        produto = session.query(Produto).filter_by(codigo=codigo).first()
        if not produto:
            print(f'O produto {codigo} não foi cadastrado no sistema')
            return
        session.delete(produto)
        session.commit()
        print(f'O produto {produto.nome} com código {codigo} foi removido corretamente')

    @staticmethod
    def listar_estoque():
        produtos = session.query(Produto).all()
        if not produtos:
            print("O estoque está vazio.")
            return

        for p in produtos:
            print(f"Nome: {p.nome}")
            print(f"Código: {p.codigo}")
            print(f"Quantidade: {p.qtd}")
            print(f"Lote: {p.lote}")
            print(f"Data de entrada: {p.data_entrada}")
            print("-" * 20)

    @staticmethod
    def buscar_por_codigo(codigo):
        produto = session.query(Produto).filter_by(codigo=codigo).first()
        if produto:
            print(f"Nome: {produto.nome}")
            print(f"Código: {produto.codigo}")
            print(f"Quantidade: {produto.qtd}")
            print(f"Lote: {produto.lote}")
            print(f"Data de entrada: {produto.data_entrada}")
        else:
            print(f"Nenhum produto com o código {codigo} foi encontrado.")


# -------------------------------
# Criar as tabelas no banco
Base.metadata.create_all(bind=db)
