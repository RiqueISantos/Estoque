import datetime
from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from abc import ABCMeta, abstractmethod
from sqlalchemy.ext.declarative import DeclarativeMeta

# Definir a metaclasse combinada para suporte a classes abstratas
class DeclarativeABCMeta(DeclarativeMeta, ABCMeta):
    pass

# Base unificada para todas as classes
Base = declarative_base(metaclass=DeclarativeABCMeta)

# Configuração do banco
db = create_engine('sqlite:///estoque.db')
Session = sessionmaker(bind=db)
session = Session()

# ------------------------------------------
class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True)
    contato = Column(String)
    produtos = relationship('Produto', back_populates='fornecedor')

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


# ------------------------------------------
class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

    marcas = relationship('Marca', backref='categoria')

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


# ------------------------------------------
class Marca(Base):
    __tablename__ = 'marca'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String)
    id_categoria = Column(Integer, ForeignKey('categorias.id'))

    produtos = relationship('Produto', back_populates='marca')

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


# ------------------------------------------
class Item(Base):
    __abstract__ = True  # Não será mapeada

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    data_cadastro = Column(Date, default=datetime.date.today)

    @abstractmethod
    def adicionar(self, session):
        pass

    @abstractmethod
    def remover(self, session):
        pass


# ------------------------------------------
class Produto(Item):
    __tablename__ = 'produtos'

    codigo = Column(String, unique=True)
    qtd = Column(Integer)
    lote = Column(String)
    data_entrada = Column(Date, default=datetime.date.today)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    marca_id = Column(Integer, ForeignKey('marca.id'))

    fornecedor = relationship('Fornecedor', back_populates='produtos')
    marca = relationship('Marca', back_populates='produtos')

    @staticmethod
    def adicionar(nome, codigo, qtd, lote, fornecedor_id, marca_id):
        produto = Produto(nome=nome, codigo=codigo, qtd=qtd, lote=lote, 
                        fornecedor_id=fornecedor_id, marca_id=marca_id)
        session.add(produto)
        session.commit()
        print(f"Produto {nome} adicionado com sucesso!")
        
    # Método de instância
    def remover(self, session):
        session.delete(self)
        session.commit()
        print(f"Produto {self.nome} removido com sucesso!")

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


# ------------------------------------------
# Criar as tabelas no banco
Base.metadata.create_all(bind=db)
