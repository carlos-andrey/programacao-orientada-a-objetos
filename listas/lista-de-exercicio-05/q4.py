def inteiro(numero):
    if numero > 0:
        conjunto = 'P'
    else :
        conjunto = 'N'
    return conjunto
numero = int(input('Digite um numero: '))

resultado = inteiro(numero)
print(resultado)
