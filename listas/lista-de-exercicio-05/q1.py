def repeticao():
  for linha in range(1, numero + 1) :
   print(('{} '.format(linha))*linha)

numero = int(input('Digite um numero : '))
repeticao()