numero1 = float (input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))


if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(numero1)
        print(numero2)
        print(numero3)
    if numero3 > numero2:
        print(numero1)
        print(numero3)
        print(numero2)
elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(numero2)
        print(numero1)
        print(numero3)
    if numero3 > numero1:
        print(numero2)
        print(numero3)
        print(numero1)
elif numero3 > numero2 and numero3 > numero1:
    if numero2 > numero1:
        print(numero3)
        print(numero2)
        print(numero1)
    if numero1 > numero2:
        print(numero3)
        print(numero1)
        print(numero2)
