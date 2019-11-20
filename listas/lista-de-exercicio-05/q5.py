def somaImposto(taxaImposto, custo):
    custoTotal = ((taxaImposto / 100) * custo) + custo
    return custoTotal

taxa_imposto = float(input('Digite o imposto em porcentagem: '))
custo = float(input('Digite preço do produto: '))
custo_total = somaImposto(taxa_imposto, custo)
print('O valor do produto com o imposto incluso é: R$ {:.2f}'.format(custo_total))
