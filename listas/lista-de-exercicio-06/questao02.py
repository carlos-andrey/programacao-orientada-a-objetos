import random

nomes = ['Jonatham', 'Mary', 'Edward', 'Alphonse', 'Peter', 'Tony', 'Stephen', 'Natasha', 'Vivian', 'Wanessa',
 'Fancesca', 'Alexander', 'Simon', 'Rafael', 'Clarissa', 'Isabelle', 'Maia', 'Winry', 'Marta']
sobrenomes = ['Cage', 'Jones', 'Elric', 'De Assis', 'Pan', 'Stark', 'Herondele', 'Romanoff', 'Bellevi', 'Freitas', 
'Bariciello', 'Ligthwood', 'Lewis', 'Godson', 'Fairchild', 'Lombarde', 'Wolves', 'Smith']

n = int(input('Informe o numero de linhas: '))

with open('Saida2.txt','w') as saida:
    for linhas in range(0, n):
        altura = random.randint(100, 210)
        idade = random.randint(1, 101)
        nome = random.randint(0, len(nomes)-1)
        sobrenome = random.randint(0, len(sobrenomes)-1)
        print('{} {}, {} Anos, {}M'.format(nomes[nome], sobrenomes[sobrenome], idade, (altura / 100)), file = saida)