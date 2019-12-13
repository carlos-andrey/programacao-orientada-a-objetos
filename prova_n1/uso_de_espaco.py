import funcoes
usuarios = []
with open('usuarios.txt', 'r') as arquivo:
    posicao = 1

    for linha in arquivo:
        usuarios.append(linha.split())
    for usuario in usuarios:
        usuario.insert(0, posicao)
        resultado_convercao = funcoes.converte_tamanho(float(usuario[2]))
        usuario[2] = resultado_convercao
        total = resultado_convercao
        posicao += 1
    for usuario in usuarios:
        funcoes.percentual(usuario, total)
    media = total/len(usuarios)
    with open('relatorio.txt', 'w') as relatorio:
        print(usuarios, file= relatorio)