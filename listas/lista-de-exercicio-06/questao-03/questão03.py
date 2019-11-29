def copia_texto(origem, destino):
    with open(origem,'r') as fonte:
        saida = fonte.readlines()
        with open(destino,'w') as receptasculo:
            index = 0
            for linhas in saida:   
                if linhas.find('//') == 0 :
                    print(saida[index], file = receptasculo)
                index += 1
x = input('Arquivo de origem(.txt): ')
y = input('Arquivo de destino(.txt): ') 

copia_texto(x, y)