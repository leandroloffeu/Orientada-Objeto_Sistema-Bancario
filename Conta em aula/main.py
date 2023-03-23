from cliente import Cliente
from conta import *
from cliente import *

if __name__ == '__main__':
    cliente1 = Cliente('João','Pedro','000.000.000-00')
    conta1 = Conta('123-5', 'Nilton Junior',2000.00,50000.00 )
    cliente2 = Cliente('Breno','Viana','111.111.100-00')
    conta2 = Conta('123-5', 'cliente',100.00,200.00 )

    conta1.deposita (50)
    conta2.transfere_para(conta1,50)
    conta1.extrato()
    conta2.extrato()
    conta1.sacar(50)
    conta1.sacar(10)
    conta1.historico.imprime()
    