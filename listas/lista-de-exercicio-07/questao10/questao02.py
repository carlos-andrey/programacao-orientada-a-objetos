'''Questão 2. Modele uma paixonite, sendo que essa possua ao menos o atributo nome, 
e ao menos um metodo que utilize o atributo nome. '''

class Crush:
    def __init__(self, nome):
        self.nome = nome
    def iludir(self):
        print(f'{self.nome} só ilude.')

crush1 = Crush('Pedro')
crush1.iludir()