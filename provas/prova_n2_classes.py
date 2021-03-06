import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return (f'Nome: {self.nome}, Idade {self.idade}')
    def is_adulto(self):
        if self.idade >= 18:
            return True
        else:
            return False
class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []
    def registrar_compra(self, compra):
        self.compras.append(compra)
    def get_data_ultima_compra(self):
        pass
    def total_compras(self):
        total = 0
        for item in self.compras:   
            total += item.valor
        print(f'Total de compras: {total} reais')
class Compra:
    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.valor = valor
        self.data = data
