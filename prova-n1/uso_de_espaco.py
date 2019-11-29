from funcoes import converte_tamanho
from funcoes import percentual
with open('usuarios.txt', 'r') as usuarios:
    lista_usuarios = usuarios.readlines()
    with open('relatorio.txt', 'w') as relatorio:
        print('ACME Inc.    Uso de espaço em disco pelos usúario', file = relatorio)
        print(70 * '-', file = relatorio)
        print('Nr.      Usuario      Espaço utilizado       % ''do uso', file = relatorio)
        tamanho_total = 0
        tamanho = 0
        for linha in range (0, len(lista_usuarios)):
            espaco = lista_usuarios[linha].split()
            tamanho_utilizado =  int(espaco[1])
            tamanho_total = tamanho_total + tamanho_utilizado
            print('{}       {}      {:.2f} MB           {:.2f}%'.format(linha + 1, espaco[0].strip('\n'),converte_tamanho(tamanho_utilizado),percentual(tamanho_total, tamanho_utilizado)),file= relatorio)
        print('Espaço total ocupado: {:.2f} MB'.format(converte_tamanho(tamanho_total)), file = relatorio)
        print('Espaço médio ocupado: {:.2f} MB'.format(converte_tamanho(tamanho_total)/len(lista_usuarios)), file= relatorio)
 
        