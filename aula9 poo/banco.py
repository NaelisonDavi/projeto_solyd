class conta:

    def __init__(self, cliente, saldo, limite, sacar, depositar):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, dinheiro):
        self.saldo -= dinheiro

    def depositar(self, dinheiro):
        self.saldo += dinheiro
