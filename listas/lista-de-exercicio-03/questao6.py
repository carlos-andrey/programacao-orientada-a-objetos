numero1 = float (input('Digite o primeiro numero: '))
numero2 = float (input('Digite o segundo numero: '))
numero3 = float (input('Digite o terceiro numero: '))


if numero1 > numero2 and numero1 > numero3:
    print('O numero maior é {}'.format(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print('O numero maior é {}'.format(numero2))
elif numero3 > numero2 and numero3 > numero1:
    print('O numero maior é {}'.format(numero3))