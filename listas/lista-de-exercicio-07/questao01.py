class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocaCor(self, novaCor):
        self.cor = novaCor
    def mostraCor(self):
        print(f'{self.cor}')
