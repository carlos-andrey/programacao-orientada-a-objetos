horas_trabalhadas = float (input("Digite a quantidade de horas trabalhadas: "))
dinheiro_hora = float (input("Digite a quantidade recebida por hora de trabalho: "))
salario_bruto = horas_trabalhadas * dinheiro_hora


if salario_bruto <= 900:
    print("salario bruto: R$ {:.2f}".format(salario_bruto))

    INSS = salario_bruto * 0.10
    print("(-) INSS: R$ {:.2f}".format(INSS))
    FGTS = salario_bruto * 0.11
    print("FGTS: R$ {:.2f}".format(FGTS))
    print("Total de descontos: R$ {:.2f}".formart(INSS))
    salario_liquido = salario_bruto - INSS
    print("Salario liquido: R$ {:.2f}".format(salario_liquido))
elif salario_bruto > 901 and salario_bruto <=1500:
    print("salario bruto: R$ {:.2f}".format(salario_bruto))
    IR = salario_bruto *0.05
    print("(-) IR: R$ {:.2f}".format(IR))
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$ {:.2f}".format(INSS))
    FGTS = salario_bruto * 0.11
    print("FGTS: R$ {:.2f}".format(FGTS))
    print("Total de descontos: R$ {:.2f}".format(INSS + IR))
    salario_liquido = salario_bruto - (INSS + IR)
    print("Salario liquido: R$ {:.2f}".format(salario_liquido))
elif salario_bruto > 1501 and salario_bruto <=2500:
    print("salario bruto: R$ {:.2f}".format(salario_bruto))
    IR = salario_bruto *0.10
    print("(-) IR: R$ {:.2f}".format(IR))
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$ {:.2f}".format(INSS))
    FGTS = salario_bruto * 0.11
    print("FGTS: R$ {:.2f}".format(FGTS))
    print("Total de descontos: R$ {:.2f}".format(INSS + IR))
    salario_liquido = salario_bruto - (INSS + IR)
    print("Salario liquido: R$ {:.2f}".format(salario_liquido))
elif salario_bruto > 2500:
    print("salario bruto: R$ {:.2f}".format(salario_bruto))
    IR = salario_bruto *0.20
    print("(-) IR: R$ {:.2f}".format(IR))
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$ {:.2f}".format(INSS))
    FGTS = salario_bruto * 0.11
    print("FGTS: R$ {:.2f}".format(FGTS))
    print("Total de descontos: R$ {:.2f}".format(INSS + IR))
    salario_liquido = salario_bruto - (INSS + IR)
    print("Salario liquido: R$ {:.2f}".format(salario_liquido))

    