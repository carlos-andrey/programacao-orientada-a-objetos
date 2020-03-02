def cria_conta(numero, titular, saldo, limite):
    """Função para criar uma conta"""
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    """Função para fazer um deposito"""
    conta['saldo'] += valor

def saca(conta, valor):
    """Função para fazer um saque"""
    conta['saldo'] -= valor

def extrato(conta):
    """Função para tirar extrato"""
    print('Numero : {} \nSaldo : {}'.format(conta['numero'], conta['saldo']))

help(deposita)
help(saca)
help(extrato)
help(cria_conta)
