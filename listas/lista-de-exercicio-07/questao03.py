class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
    def mudar_valor_lado(self, novo_lado):
        self.tamanho_lado = novo_lado
    def retornar_valor_lado(self):
        return self.tamanho_lado
    def calcular_area(self):
        self.area = self.tamanho_lado**2
        return self.area

