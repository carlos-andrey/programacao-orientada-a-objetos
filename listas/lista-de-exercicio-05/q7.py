def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso > 0:
        multa = (3/100) * valor_prestacao
        juros = ((0.1/100) * valor_prestacao) * dias_atraso
        valor_total = valor_prestacao + multa  + juros
    else:
        valor_total = valor_prestacao
    return valor_total


while prestacao < 0 or prestacao > 0:
  prestacao = float(input('Informe valor da prestação: R$'))
  atraso = int(input('Informe numero de dias de atraso: '))
  valor_prestacao = valorPagamento(prestacao, atraso)
  print('O valor da prestação a ser pago é R${:.2f}'.format(valor_prestacao))