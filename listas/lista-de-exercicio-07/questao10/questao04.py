'''Crie uma classe uma classe uma classe que modele uma lista de exercicios.
 Atributos: numero_quastoes, existe. Metodos: fazer_lista'''

class Lista:
    def __init__(self, numero_questoes, existe):
        self.numero_questoes = numero_questoes
        self.existe = existe
        if self.existe.lower() == 'existe':
            self.existe = True
        else:
            self.existe = False
    def fazer_lista(self):
        if self.existe == True:
            print('Faça a lista!')
        else:
            print('Mesmo assim, faça a lista.')    

lista1 = Lista(0, 'não existe')
lista1.fazer_lista()    