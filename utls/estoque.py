import datetime
from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

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

    @staticmethod
    def adicionar_fornecedor(nome,contato):
        fornecedor = Fornecedor(nome = nome,contato = contato)
        session.add(fornecedor)
        session.commit()
        print(f'o fornecedor {nome} foi adicionado')
    

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    codigo = Column(String, unique=True)
    qtd = Column(Integer)
    lote = Column(String)
    data_entrada = Column(Date, default=datetime.date.today)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    @staticmethod
    def adicionar_produto(nome, codigo, qtd, lote, fornecedor_id,data_entrada=None):
        if data_entrada is None:
            data_entrada = datetime.date.today()
        produto = Produto(nome=nome, codigo=codigo, qtd=qtd, lote=lote, data_entrada=data_entrada, fornecedor_id = fornecedor_id)
        session.add(produto)
        session.commit()
        print(f"Produto {nome} adicionado com sucesso!")

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

# Criar as tabelas no banco
Base.metadata.create_all(bind=db)
