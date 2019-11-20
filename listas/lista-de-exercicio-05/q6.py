def converte_hora(hora_24,):
    hora_12 = hora_24 - 12
    if hora_12 <= 0:
        informacao = 'A'
    else:
        informacao = 'P'
    hora_12 = (str(hora_12)) + ' ' + informacao
    return hora_12
hora = float(input('Informe hora no formato 24: '))
nova_hora = converte_hora(hora)
print('{} na notação de 24 horas corresponde a {} na notação de 12 horas.'.format(hora,nova_hora))