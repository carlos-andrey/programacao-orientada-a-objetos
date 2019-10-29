produto1 = float (input('Preço do primeiro produto: '))
produto2 = float (input('Preço do segundo produto: '))
produto3 = float (input('Preço do terceiro produto: '))


if produto1 < produto2 and produto1 < produto3:
    print('O primeiro produto e mais barato e por consequencia o certo a se comprar')
elif produto2 < produto1 and produto2 < produto3:
    print('O segundo produto e mais barato e por consequencia o certo a se comprar')
elif produto3 < produto2 and produto3 < produto:
    print('O terceiro produto e mais barato e por consequencia o certo a se comprar')