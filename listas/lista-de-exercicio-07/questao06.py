class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def mudar_valor_lado(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura
    def retornar_valor_lado(self):
        return self.base, self.altura
    def calcular_area(self):
        self.area = self.altura * self.base
        return self.area
    def calcular_perimetro(self):
        self.perimetro = (self.altura + self.base) * 2
        return self.perimetro
base = int(input('Informe, em metros, a primeira medida do local: '))
altura = int(input('Informe, em metros, a segunda medida do local: '))

comodo1 = Retangulo(base, altura)      
piso = comodo1.calcular_area()
rodape = comodo1.calcular_perimetro()
print(f'Serão necessarios {piso} metros quadrados para o piso.')  
print(f'Serão necessarios {rodape/2} metros quadrados para o rodapé.')


