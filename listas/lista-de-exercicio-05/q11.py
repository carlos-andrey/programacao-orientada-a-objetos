def converte_data(data):
  meses = ['janeiro', 'fevereiro', 'março', 
  'abril', 'maio', 'junho', 
  'julho', 'agosto', 'setembro', 
  'outubro', 'novembro', 'dezembro']
  dia, mes, ano = data.split('/')
  indice = int(mes)

  if int(dia) < 1 or int(dia) > 31 or int(mes) < 1 or int(mes) > 12:
    nova_data = 'NULL' 
  else:  
    nova_data ='{} de {} de {}'.format(dia, meses[indice + 1], ano)
  return nova_data
  
