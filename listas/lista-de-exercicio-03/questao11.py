salario = float (input('Digite o salario: '))


if salario <= 280:
    novo_salario = salario * 1.20
    reajuste = novo_salario - salario

    print('Salario atual: {:.2f} '.format(salario))
    print('Percentual de ajuste salarial 20%')
    print('Valor do aumento igual a {:.2f}'.format(reajuste))
    print('Salario ajustado: {:.2f}'.format(novo_salario))
elif salario > 281 and salario <= 700:
    novo_salario = salario * 1.15
    reajuste = novo_salario - salario

    print('Salario atual: {:.2f} '.format(salario))
    print('Percentual de ajuste salarial 15%')
    print('Valor do aumento igual a {:.2f} '.format(reajuste))
    print('Salario ajustado: {:.2f} '.format(novo_salario))
elif salario >701 and salario <=1500:
    novo_salario = salario * 1.10
    reajuste = novo_salario - salario

    print('Salario atual: {:.2f} '.format(salario))
    print('Percentual de ajuste salarial 10%')
    print('Valor do aumento igual a {:.2f} '.format(reajuste))
    print('Salario ajustado: {:.2f} '.formart(novo_salario))
elif salario >= 1500:
    novo_salario = salario * 1.05
    reajuste = novo_salario - salario

    print('Salario atual: {:.2f} '.format(salario))
    print('Percentual de ajuste salarial 5%')
    print('Valor do aumento igual a: {:.2f} '.format(reajuste))
    print('Salario ajustado: {:.2f} '.format(novo_salario))
    