import random
'''Questão 5. Moele uma espada. Atributos: cor, comprimento, corte.
Metodos: Cortar e afiar. O atributo corte possui o valor inicial 10
e é decrementado pelo metodo cortar, sendo que volta ao valor maximo
com o metodo afiar.'''

class Espada:
    def __init__(self,nome, cor, comprimento, corte):
        self.nome = nome
        self.cor = cor
        self.comprimento = comprimento
        self.corte = corte
    def cortar(self, objeto_corte):
        self.tentativa = random.randint(1, 10)
        if self.tentativa <= 5:
            print(f'Você errou o {objeto_corte}. Tente de novo!')
        else:
            print(f'Você cortou o {objeto_corte}')
            self.corte -= 1
    def afiar(self):
        self.corte = 10
    def ver_atributos(self):
        print(f'{self.nome}, cor {self.cor}, {self.comprimento}CM de comprimento, {self.corte} de corte')

