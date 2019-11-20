def sequencia(numero,numeros):
  for linha in range(1, numero + 1) :
    numeros.append(linha)
    print(str(numeros.type()))

numero = int(input('Digite um numero : '))
numeros = []

sequencia(numero, numeros)