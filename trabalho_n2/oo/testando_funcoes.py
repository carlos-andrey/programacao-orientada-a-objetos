from	teste_conta	import	cria_conta,	deposita,	saca,	extrato
conta = cria_conta('123-9', 'João', 500, 1000)
deposita(conta, 50)
saca(conta, 25)
extrato(conta)
#faltou a 8