nome_aluno = input('Informe o nome do aluno: ')
with open('chamada.txt', 'r') as nomes:
    lista_nomes = nomes.readlines()
    index = 0
    for linhas in lista_nomes:
        #if linhas == nome_aluno:
        print(linhas)
