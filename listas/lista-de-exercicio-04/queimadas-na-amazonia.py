arquivo_amazon = open('amazon.csv')

entrada_estado = input('Informe estado de interesse: ')
entrada_ano = input('Informe ano de interesse: ')
queimadas = 0


for linha in arquivo_amazon:
	linha = linha.strip('\n')
	ano, estado, mes, numero, data = linha.split(',')
	numero = numero.replace(".", "")
	estado= estado.replace('"','')
	while estado == entrada_estado and ano == entrada_ano:
		queimadas = queimadas + int(numero)

		
	

print('As queimadas em {} no ano {} foram {}'.format(entrada_estado, entrada_ano, queimadas))
