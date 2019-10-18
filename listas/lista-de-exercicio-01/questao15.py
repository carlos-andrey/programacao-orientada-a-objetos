salario_hora = float(input('Informe salario ganho por hora: '))
horas = int(input('Informe numero de horas trabalhadas por mês: '))


salario_total = salario_hora * horas
print('Seu salario bruto é R$ {}.'.format(salario_total))
inss = (8/100) * salario_total
print('Serão pagos R$ {:.2f} ao INSS.'.format(inss))
sindicato = (5/100) * salario_total
print('Serão pagos R$ {:.2f} ao sindicato.'.format(sindicato))
ir = (11/100)  * salario_total
print('Serão pagos R$ {:.2f} de imposto de renda.'.format(ir))
descontos = inss + sindicato + ir 
salario_liquido = salario_total - descontos
print('Seu salario liquido é {:.2f}'.format(salario_liquido))