class Tamaguchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    def retornar_fome(self):
        return self.fome
    def retornar_saude(self):
        return self.saude
    def retornar_idade(self):
        return self.idade
    def comer(self):
        if self.fome < 10:
            self.fome += 1
    def tomar_injecao(self):
        if self.saude < 10:
            self.saude += 1
    def envelhecer(self):
        self.idade += 1
        self.fome -= 1
        self.saude -= 1
