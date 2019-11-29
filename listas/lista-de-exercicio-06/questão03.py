def copia_texto(origem, destino):
    with open(origem,'r') as fonte:
        saida = fonte.readlines()
        with open(destino,'w') as receptasculo:
            index = 0
            for linhas in saida:   
                if linhas.find('//') != 0 :#procura linhas que não tenham //
                    print(saida[index].strip('\n'), file = receptasculo)#printa as linhas encontradas
                index += 1