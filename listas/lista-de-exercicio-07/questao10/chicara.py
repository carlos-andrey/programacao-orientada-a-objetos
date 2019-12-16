class Chicara:
    def __init__(self, capacidade, cor, conteudo):
        self.capacidade = capacidade
        self.cor = cor
        self.conteudo = conteudo
    def encher_chicara(self, de_que):
        self.conteudo = de_que
    def ver_conteudo(self):
        print(f'{self.conteudo}')
    def esvasiar_chicara(self):
        self.conteudo = ''
    
chicara1 = Chicara('250ml', 'marrom', '')
chicara1.ver_conteudo()
chicara1.encher_chicara('café')
chicara1.ver_conteudo()
chicara1.esvasiar_chicara()
chicara1.ver_conteudo()