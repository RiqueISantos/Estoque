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

def commit_session():
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Erro ao salvar no banco: {e}")
        return

def ler_texto(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("Entrada vazia. Digite um valor válido.")
        elif len(entrada) < minimo:
            print(f"O texto deve ter pelo menos {minimo} caracteres.")
        elif len(entrada) > maximo:
            print(f"O texto deve ter no máximo {maximo} caracteres.")
        elif not entrada.isalpha():
            print("Apenas letras.")
        else:
            return entrada

def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        entrada = input(mensagem).strip()
        if not entrada.isdigit():
            print("Entrada inválida. Digite apenas números.")
            continue

        if len(entrada) < minimo or (maximo is not None and len(entrada) > maximo):
            print(f'O número deve conter entre {minimo} e {maximo} dígitos.')
            continue

        return int(entrada)

def texto_num(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("Entrada vazia. Digite um valor válido.")
        elif len(entrada) < minimo:
            print(f"O texto deve ter pelo menos {minimo} caracteres.")
        elif len(entrada) > maximo:
            print(f"O texto deve ter no máximo {maximo} caracteres.")
        else:
          return entrada


# ------------------------------------------
class Estoque:

    @classmethod
    def listar_categorias(cls):
        categorias = session.query(Categoria).all()
        if not categorias:
            print('Não existe categorias cadastradas')
            return
        for c in categorias:
            print(f'{c.id} - {c.nome}')

    

    @classmethod
    def mostrar_fornecedores(cls):
        fornecedores = session.query(Fornecedor).all()
        if not fornecedores:
            print('Não há fornecedores cadastrados')
            return
        for f in fornecedores:
            print(f'id: {f.id} - cpf: {f.cpf} - nome: {f.nome} - contato: {f.contato}')

    @classmethod
    def listar_estoque(cls):
        produtos = session.query(Produto).all()

        if not produtos:
            print("O estoque está vazio.")
            return

        print('Produtos disponíveis:\n')
        for p in produtos:
            print(f'Id: {p.id}')
            print(f"Nome: {p.nome}")
            print(f"Quantidade: {p.qtd}")
            print(f"Lote: {p.lote}")
            print(f"Data de entrada: {p.data_cadastro}")
            print(f"Marca: {p.marca.nome}")
            print(f"Fornecedor: {p.fornecedor.nome}")
            print("-" * 20)



class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _cpf = Column(Integer,unique = True, nullable = False)
    nome = Column(String, unique=True, nullable=False)
    _contato = Column(Integer, nullable=False)
    produtos = relationship('Produto', back_populates='fornecedor')

    def __init__(self, nome,contato,cpf):
        self.nome = nome
        self._contato = contato
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo):
        self._cpf = novo

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, novo):
        self._contato = novo

    def adicionar(self):
        fornecedores = session.query(Fornecedor).filter_by(cpf=self._cpf).first()
        if not fornecedores:
            fornecedor = Fornecedor(cpf = self._cpf,nome=self.nome, contato=self._contato)
            session.add(fornecedor)
            commit_session()
            print(f'O fornecedor {self.nome} foi adicionado!')
            return
        print(f'fornecedor {self.nome} já cadastrado no sistema')

    @staticmethod
    def produto_fornecedor():
        id_for = ler_inteiro('Digite o número do id do fornecedor que você queira consultar: ',1,100)
        fornecedor = session.query(Fornecedor).filter_by(id=id_for).first()
        if not fornecedor:
            print(f'Fornecedor com id {id_for} não cadastrado no sistema')
            return
        print(f'\nProdutos do {fornecedor.nome}:')
        for p in fornecedor.produtos:
            print(f'Id: {p.id}')
            print(f"Nome: {p.nome}")
            print(f"Quantidade: {p.qtd}")
            print(f"Lote: {p.lote}")
            print(f"Data de entrada: {p.data_cadastro}")
            print(f"Marca: {p.marca.nome}")
            print(f"Fornecedor: {p.fornecedor.nome}")
            print("-" * 20)







    @staticmethod
    def atualiza_contato():
        id_fornecedor = ler_inteiro('Digite o ID do fornecedor que deseja atualizar o cadastro: ',1,100)
        fornecedor = session.query(Fornecedor).filter_by(id = id_fornecedor).first()
        if fornecedor:
            contato_novo = ler_inteiro('Digite o novo contato do forncedor: ',11,11)
            fornecedor.contato = contato_novo
            print('Contato atualizado com sucesso!')
            session.commit()
        else:
            print('Fornecedor não foi encontrado')




# ------------------------------------------
class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    marcas = relationship('Marca', backref='categoria')

    @staticmethod
    def adicionar():
        nome = ler_texto('Nome da categoria: ',2,50).capitalize()
        categorias = session.query(Categoria).filter_by(nome=nome).first()
        if not categorias:
            categoria = Categoria(nome=nome)
            session.add(categoria)
            commit_session()
            print(f'Categoria {nome} foi adicionada')
            return
        print(f'categoria {nome} já foi adicionada')

    @staticmethod
    def marca_categoria():
        Estoque.listar_categorias()
        id_cat = ler_inteiro('Digite o id da categoria: ',1)
        categoria = session.query(Categoria).filter_by(id = id_cat ).first()
        if not categoria:
            print(f'Nenhuma categoria com o id "{id_cat}" encontrada!')
            return
        
        if categoria.marcas:
            print(f'\nMarcas disponíveis em {categoria.nome}:')
            for marca in categoria.marcas:
                print(f'{marca.id} - {marca.nome}')
        else:
            print(f'Nenhuma marca cadastrada na categoria {categoria.nome}!')



# ------------------------------------------
class Marca(Base):
    __tablename__ = 'marca'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(50), nullable=False)
    id_categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    produtos = relationship('Produto', back_populates='marca')

    @staticmethod
    def adicionar():
        nome = ler_texto('Insira o nome da marca: ',2,50).capitalize()
        print('\nCategorias disponíveis:')
        Estoque.listar_categorias()
        id_categoria = ler_inteiro(f'\nInsira o numero da categoria que deseja incluir a marca {nome}: ',1,100)
        marcas = session.query(Marca).filter_by(nome=nome).first()
        if not marcas:
            id_categorias = session.query(Categoria).filter_by(id=id_categoria).first()
            if id_categorias:
                marca = Marca(nome=nome, id_categoria=id_categoria)
                session.add(marca)
                session.commit()
                print(f'A marca {nome} foi adicionada!')
                return
            else:
                print(f'A categoria não existe.')
                return
        print(f'Marca {nome} já foi cadastrada!')

    @staticmethod
    def produto_marca():
            nome_marca = ler_texto('\nDigite o nome da marca que deseja ver os produtos: ',2,50).capitalize()
            marca = session.query(Marca).filter_by(nome=nome_marca).first()
            if not marca:
                print(f'A marca {nome_marca} não está registrada no sistema.')
                return
            
            if marca.produtos:
                print(f'\nProdutos da marca {nome_marca}:')
                for p in marca.produtos:
                    print(f'Id: {p.id}')
                    print(f"Nome: {p.nome}")
                    print(f"Quantidade: {p.qtd}")
                    print(f"Lote: {p.lote}")
                    print(f"Data de entrada: {p.data_cadastro}")
                    print(f"Marca: {p.marca.nome}")
                    print("-" * 20)
            else:
                print(f'Nenhum produto encontrado na marca {nome_marca}!')



# ------------------------------------------
class Item(Base):
    __abstract__ = True  # Não será mapeada

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    data_cadastro = Column(Date, default=datetime.date.today, nullable=False)

    @abstractmethod
    def adicionar(self):
        pass

    @abstractmethod
    def remover(self):
        pass


# ------------------------------------------
class Produto(Item):
    __tablename__ = 'produtos'

    qtd = Column(Integer, nullable=False)
    lote = Column(String, nullable=False)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'), nullable=False)
    marca_id = Column(Integer, ForeignKey('marca.id'), nullable=False)

    fornecedor = relationship('Fornecedor', back_populates='produtos')
    marca = relationship('Marca', back_populates='produtos')

    def __init__(self, nome, qtd, lote, fornecedor_id, marca_id):
        self.nome = nome
        self.qtd = qtd
        self.lote = lote
        self.fornecedor_id = fornecedor_id
        self.marca_id = marca_id

    def adicionar(self):
        produtos = session.query(Produto).filter_by(nome=self.nome,marca_id = self.marca_id,fornecedor_id = self.fornecedor_id).first()
        if not produtos:
            fornecedores = session.query(Fornecedor).filter_by(id = self.fornecedor_id).first()
            if fornecedores:
                marcas = session.query(Marca).filter_by(id = self.marca_id).first()
                if marcas:
                    session.add(self)
                    session.commit()
                    print(f"Produto {self.nome} adicionado com sucesso!")
                else:
                    print(f'Marca não foi cadastrada')
            else:
                print(f'Fornecedor não foi cadastrado')
        else:
            print(f'Produto já foi adicionado no sistema')

    @staticmethod
    def remover():
        id_removido = ler_inteiro('Digite o id do produto para remover: ',1,100)
        produto_remover = session.query(Produto).filter_by(id=id_removido).first()
        if produto_remover:
            nomep = produto_remover.nome
            marcap = produto_remover.marca.nome
            session.delete(produto_remover)
            session.commit()
            print(f"Produto {nomep} - {marcap} removido com sucesso!")
            return
        print(f'Produto não encontrado')


    @staticmethod
    def buscar_por_nome():
        nome = ler_texto('Insira o nome do produto: ',2,50).capitalize()
        pdt = session.query(Produto).filter_by(nome=nome).all()

        if pdt:
            for p in pdt:
                print(f'Id: {p.id}')
                print(f"Nome: {p.nome}")
                print(f"Quantidade: {p.qtd}")
                print(f"Lote: {p.lote}")
                print(f"Data de entrada: {p.data_cadastro}")
                print(f"Marca: {p.marca.nome}")
                print(f"Fornecedor: {p.fornecedor.nome}")
                print("-" * 20)
        else:
            print(f"Nenhum produto com o nome {nome} foi encontrado.")


# ------------------------------------------
# Criar as tabelas no banco
Base.metadata.create_all(bind=db)
