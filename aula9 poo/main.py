from usuario import cliente
from banco import conta

cliente1 = cliente('davi', 11815729406, 26)
conta1 = conta('davi', 300, 20000, 50, 0)

print(conta1.saldo)
conta1.sacar(35)
print(conta1.saldo)
conta1.depositar(150)
print(conta1.saldo)
