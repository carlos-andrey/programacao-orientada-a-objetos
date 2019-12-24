import random

class Tartaruga:
    def __init__(self, cor, posicao):
        self.cor = cor
        self.posicao = posicao
    def caminhar_rapidamente(self):
        self.posicao += 3
    def escorrega(self):
        self.posicao -= 6
    def caminha_lentamente(self):
        self.posicao += 1
class Lebre:
    def __init__(self, cor, posicao):
        self.cor = cor
        self.posicao = posicao
    def dorme(self):
        self.posicao += 0
    def salto_grande(self):
        self.posicao += 9
    def escorrega_bastante(self):
        self.posicao -= 12
    def salto_pequeno(self):
        self.posicao += 1
    def escorrega_pouco(self):
        self.posicao -= 2        
i = 0
tar1 = Tartaruga('verde', 1)
leb1 = Tartaruga('branco', 1)