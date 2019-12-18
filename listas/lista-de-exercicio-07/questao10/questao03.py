'''Questão 03. Crie uma classe que modele um cavalo. Atributos: nome, cor, cansaco,
distancia_percorrida. Metodos: cavalgar, trotar, descancar e ver_status. 
Cansaço começa em zero e vai ate dez, sendo que  cavalgar adiciona 2 em cansaco,
e trotar adiciona 1. O cavalo consegue cavalgar ate atigir 5 de cansaco e trotar
ate atingir 10, depois disso, ele só podera descancar. Cada descanço reduz 1 de 
cansaço ara cada dez minutos de descanco. Distancia percorrida começa em zero e 
Incrementa dez metro para cada cavalgada, e cinco para cada trote. '''
class Cavalo:
    def __init__(self, nome, cor, cansaco, distancia_percorrida):
        self.nome = nome
        self.cor = cor
        self.cansaco= cansaco
        self.distancia_percorrida = distancia_percorrida
    def cavalgar(self):
        if self.cansaco >= 5:
            print(f'{self.nome} não consegue cavalgar.')
        else:    
            self.cansaco += 2
            self.distancia_percorrida += 10
    def trotar(self):
        if self.cansaco == 10:
            print(f'{self.nome} não consegue trotar.')
        else:    
            self.cansaco += 1
            self.distancia_percorrida += 5
    def descancar(self, duracao):
        self.cansaco = self.cansaco - (duracao/10)
    def ver_status(self):
        print(f'{self.nome}, cor: {self.cor}, cansaço: {self.cansaco} percorreu: {self.distancia_percorrida} metros')
