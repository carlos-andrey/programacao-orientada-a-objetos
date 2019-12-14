class Pokemon:
    def __init__(self, nome, tipo, descrição, ataques, nivel, poder_luta, brilhante):
        self.nome = nome
        self.tipo = tipo
        self.descrição = descrição
        self.ataques = ataques
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante = brilhante
    def mostrar_ataques(self):
        print(*self.ataques)
    def subir_nivel(self):
        self.nivel += 1
        self.poder_luta += 1
    def mostrar_poder_luta(self):
        print(self.poder_luta)
    def e_brilhante(self):
        if self.brilhante.lower() == 'brilhante':
            self.brilhante = True
            print(self.brilhante)
        else:
            self.brilhante = False                
            print(self.brilhante)
    def adicionar_ataque(self, novo_ataque):
        self.ataques.append(novo_ataque)
