arquivo_amazon = open('amazon.csv')

casos_acre = 0	
casos_ceara = 0
casos_amazonas = 0
casos_mato_grosso = 0
for linha in arquivo_amazon:
	linha = linha.strip('\n')
	ano, estado, mes, numero, data = linha.split(',')
	numero = numero.replace(".", "")
	estado= estado.replace('"','')
	#print("ano {}, mes {}, numero {}, data {}".format(ano, mes, numero, data))
	if estado == 'Acre' and ano == '2015':
		casos_acre = casos_acre + int(numero)

	elif estado == 'Ceara' and ano == '2014':
		casos_ceara = casos_ceara + int(numero)

	elif estado == 'Amazonas':
		casos_amazonas = casos_amazonas + int(numero)

	elif estado == 'Mato Grosso':
		if int(ano) >= 2010: 
			casos_mato_grosso = casos_mato_grosso + int(numero)

print("Queimadas no Acre em 2015: {}".format(casos_acre))		
print("Queimadas no Ceara em 2014: {}".format(casos_ceara))
print("Queimadas no Amazonas: {}".format(casos_amazonas))
print("Queimadas no Mato Grosso ate de 2010 : {}".format(casos_mato_grosso))
