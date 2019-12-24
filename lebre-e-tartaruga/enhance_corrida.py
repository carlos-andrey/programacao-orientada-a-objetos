import random

class Tartaruga:
    def __init__(self, cor, posicao):
        self.cor = cor
        self.posicao = posicao
    def caminhar_rapidamente(self):
        self.posicao += 3
        return self.posicao
    def escorrega(self):
        self.posicao -= 6
        return self.posicao
    def caminha_lentamente(self):
        self.posicao += 1
        return self.posicao
class Lebre:
    def __init__(self, cor, posicao):
        self.cor = cor
        self.posicao = posicao
    def dorme(self):
        self.posicao += 0
        return self.posicao
    def salto_grande(self):
        self.posicao += 9
        return self.posicao
    def escorrega_bastante(self):
        self.posicao -= 12
        return self.posicao
    def salto_pequeno(self):
        self.posicao += 1
        return self.posicao
    def escorrega_pouco(self):
        self.posicao -= 2        
        return self.posicao