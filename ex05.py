#Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo=0): #o __init__ eh o construtor no python 
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def Alterar_nome(self, alteracao):
        self.nome = alteracao

    def depositar(self, deposito):
        self.saldo += deposito
        return deposito

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque
            return saque
        else:
            print("Saldo insuficiente, por gentileza tente outra operacao")
            return 0

conta_final = ContaCorrente('10981', 'Cleber Machado', 600)
print(f'O nome do(a) correntista eh {conta_final.nome}, com o numero da conta sendo {conta_final.numero_conta} e possuindo R${conta_final.saldo} de saldo bancario')
sacada = conta_final.sacar(420)
print(f'O(a) correntista {conta_final.nome} sacou R${sacada} e agora possui R${conta_final.saldo} em sua conta')


conta_final = ContaCorrente('10684', 'Larissa')
print(f'O nome do(a) correntista eh {conta_final.nome}, com o numero da conta sendo {conta_final.numero_conta} e possuindo R${conta_final.saldo} de saldo bancario')
sacada = conta_final.sacar(100)
deposito = conta_final.depositar(250)
print(f'O(a) correntista {conta_final.nome} depositou R${deposito} e agora possui R${conta_final.saldo} em sua conta')
deposito = conta_final.depositar(371)
print(f'O(a) correntista {conta_final.nome} depositou R${deposito} e agora possui R${conta_final.saldo} em sua conta')


