with open('fonte.txt','r') as fonte:
    saida = fonte.read()
    with open('entrada.txt','w') as receptasculo:
        print(saida, file = receptasculo)