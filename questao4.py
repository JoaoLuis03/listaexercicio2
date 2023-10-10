class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}"
conta = ContaBancaria("Pedro")
print(conta.depositar(10000))
print(conta.sacar(5000))
print(conta.saldo)
