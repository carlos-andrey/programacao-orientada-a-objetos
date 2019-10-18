altura = float(input('Informe sua altura: '))
sexo = str(input('Informe seu sexo (m/f): '))
if (sexo == 'm' ):
    peso_ideal = (72.7 * altura) - 58
    print('Seu peso ideal é {:.2f}'.format(peso_ideal))

elif (sexo == 'f' ):
    peso_ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal é {:.2f}'.format(peso_ideal))