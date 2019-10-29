turno = str (input('Digite o turno de estudo(M para Matutino, V para Vespertino e N para Noturno): '))


if turno == ('M') or turno == ('m'):
    print('Bom Dia!')
elif turno == ('V') or turno == ('v'):
    print('Boa Tarde!')
elif turno == ('N') or turno == ('n'):
    print('Boa Noite!')
else:
    print('Valor invalido!')