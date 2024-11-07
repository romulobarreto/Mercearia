from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, ItensVendidos: Produtos, vendedor, comprador, QuantVendida, data = datetime.now()):
        self.ItensVendidos = ItensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.QuantVendida = QuantVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco, nascimento = datetime):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
        self.nascimento = nascimento

class Funcionario(Pessoa):
    def __init__(self, matricula, nome, telefone, cpf, email, endereco, nascimento = datetime):
     self.matricula = matricula
     super(Funcionario, self). __init__(nome, telefone, cpf, email, endereco, nascimento)