class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crecer(self):
        if self.idade < 21:
            self.altura += 0.5
    def envelhecer(self):
        self.crecer()
        self.idade += 1

