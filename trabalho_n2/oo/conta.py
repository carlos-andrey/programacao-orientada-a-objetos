import datetime
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime(self):
        print('Data de abertura: {}'.format(self.data_abertura))
        for transacao in self.transacoes:
            print('*',transacao)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf 

class Conta:
    def __init__(self, numero, titular, saldo, limite, data):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data = data
        self.histrico = Historico()

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.histrico.transacoes.append('Sacou :{}'.format(valor))
            return True
    def deposita(self, valor):
        self.saldo += valor
        self.histrico.transacoes.append('Depositou: {}'.format(valor))
    def extrato(self):
        print(f'Nome: {self.titular.nome}\nSobrenome: {self.titular.sobrenome}\nCPF: {self.titular.cpf}\nNumero: {self.numero}\nSaldo: {self.saldo}')
        self.histrico.transacoes.append('Tirou extrato')
        
    def tranfere_para(self, destino, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor 
            destino.saldo += valor
            self.histrico.transacoes.append('Tranferiu: {} para {}'.format(valor, destino.titular.nome))
            return True