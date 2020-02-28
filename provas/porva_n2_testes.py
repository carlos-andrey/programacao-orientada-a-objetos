from prova_n2_classes import Pessoa, Cliente, Vendedor, Compra 
import datetime
pessoa1 = Pessoa('Damião', 52)
print(pessoa1)
print(pessoa1.is_adulto())

vendedor1 = Vendedor('Wanderson',22, 800)
print(vendedor1)
print(vendedor1.is_adulto())

compra1 = Compra(vendedor1,datetime.datetime.now(), 2)
compra2 = Compra(vendedor1,datetime.datetime.now(), 2)

cliente1 = Cliente('Pedro', 15)
print(cliente1)
print(cliente1.is_adulto())
cliente1.registrar_compra(compra1)
cliente1.registrar_compra(compra2)
cliente1.total_compras()
