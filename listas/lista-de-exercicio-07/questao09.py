class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
    def comer(self, comida):
        self.bucho.append(comida)
    def ver_bucho(self):
        print(f'{self.nome} comeu {self.bucho}')
    def digerir(self):
        self.bucho = []

nome = input('Você acaba de adquirir um macaco potencialmente canibal. Qual nome deseja dar a ele? \n')
macaco1 = Macaco(nome, [])
comida = input(f'{nome} esta com fome. O que você dara para {nome} comer?\n')
macaco1.comer(comida)
macaco1.ver_bucho()
comida = input(f'{nome} continua com fome. O que você dara para {nome} comer?\n')
macaco1.comer(comida)
macaco1.ver_bucho()
nome2 = input(f'Apareceu outro macaco.Vamos chamalo de...(?)\n')
macaco2 = Macaco(nome2, [])
comida = input(f'{nome2} esta com fome. O que você dara para {nome2} comer?\n')
macaco2.comer(comida)
macaco2.ver_bucho()
print(f'Quando você se distraiu {nome} comeu {nome2}. Parece que você não  alimentou o suficiente.')
macaco1.comer(macaco1)
macaco1.ver_bucho()