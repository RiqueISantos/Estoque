import datetime

from bokeh.layouts import column
from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from abc import ABC, abstractmethod

'''class Item(ABC):
    @staticmethod
    @abstractmethod
    def adicionar(*args,**kwargs):
        pass
    @staticmethod
    @abstractmethod
    def remover(codigo):
        pass'''

# Configuração do banco
db = create_engine('sqlite:///estoque.db')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String,unique = True)
    contato = Column(String)

    produtos = relationship('Produto', backref = 'fornecedores')

    @staticmethod
    def adicionar(nome,contato):
        fornecedor = Fornecedor(nome = nome,contato = contato)
        session.add(fornecedor)
        session.commit()
        print(f'o fornecedor {nome} foi adicionado')

    @staticmethod
    def produto_fornecedor(id_fornecedor):
        fornecedor = session.query(Fornecedor).filter_by(id = id_fornecedor).first()
        if not fornecedor:
            print(f'fornecedor com id {id_fornecedor} não cadastrado no sistema')
            return
        print(f'Produtos do {fornecedor.nome}:')
        for produto in fornecedor.produtos:
            print(f'{produto.nome} - lote: {produto.lote}')
    
class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key = True, autoincrement = True)
    nome = Column(String)

    @staticmethod
    def adicionar(nome):
        categoria = Categoria(nome = nome)
        session.add(categoria)
        session.commit()
        print(f'categoria {nome} foi adicionada')


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
    def adicionar(nome, codigo, qtd, lote, fornecedor_id,marca_id,data_entrada=None):
        if data_entrada is None:
            data_entrada = datetime.date.today()
        produto = Produto(nome=nome, codigo=codigo, qtd=qtd, lote=lote, data_entrada=data_entrada, fornecedor_id = fornecedor_id,marca_id = marca_id)
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
        print(f'O produto {produto.nome} com codigo {codigo} foi removido corretamente')

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

class Marca(Base):
    __tablename__ = 'marca'
    id = Column(Integer, autoincrement = True, primary_key = True)
    nome = Column(String)
    id_categoria = Column(Integer,ForeignKey('categorias.id'))

    produtos = relationship('Produto', backref = 'marca')

    @staticmethod
    def adicionar(nome,id_categoria):
        marca = Marca(nome = nome, id_categoria = id_categoria)
        session.add(marca)
        session.commit()
        print(f'a marca {nome} foi adicionada')


    @staticmethod
    def produto_marca(nome_marca):
        marca = session.query(Marca).filter_by(nome=nome_marca).first()
        if not marca:
            print(f'a marca {nome_marca} não está registrada no sistema')
            return
        for produto in marca.produtos:
            print(f'{produto.nome} - {produto.codigo}')

# Criar as tabelas no banco
Base.metadata.create_all(bind=db)
