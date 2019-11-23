def desenha_moldura(colunas, linhas):
  if colunas == '':
    colunas = 1
  elif linhas == '':
   linhas = 1
  elif int(colunas) > 20:
    colunas = 20
  elif int(linhas) > 20:
    linhas = 20

  print('+' ,int(colunas) * '-', '+')
  for x in range(1, int(linhas) + 1):
    print('|', int(colunas) * ' ', '|')
  print('+' ,int(colunas) * '-', '+')
