class Computador:
    def __init__(self, marca, modelo,componentes, anos_uso, cor):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor
    def mostrarMarca(self):
        print(f'{self.marca}')
    def adicionarComponentes(self,novo_componente):
        self.componentes.append(novo_componente)
    def mostrarComponentes(self):
        print(f'{self.componentes}')
    def mostrar_anos_de_uso(self):
        if self.anos_uso < 6:
            print(f'{self.anos_uso}')
        else:
            print('Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora')
    def envelhecer(self):
        self.anos_uso += 1
