def embaralha_palavra(palavra):  
  import random
  palavra_embaralhada = list(palavra)
  random.shuffle(palavra_embaralhada)
  palavra_padronizada = ''.join(palavra_embaralhada)
  return str(palavra_padronizada.upper())

