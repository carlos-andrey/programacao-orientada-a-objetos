from conta import Conta, Cliente, Data
data1 = Data( '02','janeiro', 2016)
data2 = Data( '04','janeiro', 2016)

cliente1 = Cliente('Jozé', 'Freitas', '000.000.000-00' )
cliente2 = Cliente('João', 'Alves', '000.000.000-01')
cliente2 = Cliente('Pedro', 'Matias', '000.000.000-02')
conta1 = Conta('123-4', cliente1, 120, 1000, data1)
conta2 = Conta('123-5', cliente1, 100, 1000, data2)
conta1.saca(20)
conta1.extrato()
conta1.deposita(100)
conta1.extrato()
conta1.tranfere_para(conta2, 75)
conta1.histrico.imprime()