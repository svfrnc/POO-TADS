# implementar classes em python para representar uma conta bancária
# A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e seu saldo e métodos
# para realizar as operações de depósito e saque.
# Escrever um programa para testar a classe.
class conta_bancaria:
    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.saldo = 0
    def depositar(self, v):
        self.saldo += v
    def sacar(self, v):
        self.saldo -= v

x = conta_bancaria()
x.titular = "sávio"
x.cpf = "072.332.453-23"
x.saldo = 999999
x.depositar(1)
x.sacar(10000)
print(x.saldo)
