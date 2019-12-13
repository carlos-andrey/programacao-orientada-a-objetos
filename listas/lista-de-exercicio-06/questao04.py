def calcula_media(nomes, notas):
    with open(nomes, 'r') as alunos:
        nome_aluno = alunos.readlines()
        with open(notas, 'r') as notas:
            lista_notas = notas.readlines()
            with open('medias.txt', 'w') as notas_medias:
                for linha in range(0, len(lista_notas)):
                    media = lista_notas[linha].split(' ')
                    soma_final = 0
                    for elemento in range(0, len(media)):
                        soma = media[elemento].replace('"', ' ')                         
                        soma_final += int(soma)
                    print('{} {:.2f}'.format(nome_aluno[linha].strip('\n'), soma_final / len(soma)), file = notas_medias)
x = input('Informe nome do arquivo de alunos: ')
y = input('Informe nome do arquivo de notas: ')

calcula_media(x, y)