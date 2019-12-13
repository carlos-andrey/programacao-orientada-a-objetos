def valida_ip(lista_ips):
    with open(lista_ips, 'r') as lista:
        ips = lista.readlines()
        with open('ips_validos.txt', 'w') as validos:
            with open('ips_invalidos.txt', 'w') as invalidos:
                index = 0
                for linha in ips:
                    octeto = ips[index].split('.')
                    for intervalo in range(0, len(octeto)):
                        if int(octeto[intervalo]) > 255:
                            print(ips[index], file = invalidos)
                        elif int(octeto[intervalo]) < 255:
                            print(ips[index], file = validos)
                    index += 1 
x = input('Informe nome do arquivo de ips:')
valida_ip(x)