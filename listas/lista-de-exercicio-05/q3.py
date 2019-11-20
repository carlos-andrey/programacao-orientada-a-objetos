def soma (n1, n2, n3):
  soma = n1 + n2 + n3
  return soma
n1 = int(input('Informe o primeiro numero : '))
n2 = int(input('Informe o primeiro segundo : '))
n3 = int(input('Informe o primeiro terceiro : '))

valor_soma = soma(n1, n2, n3)

print('A soma dos três numeros é {}'.format(valor_soma))