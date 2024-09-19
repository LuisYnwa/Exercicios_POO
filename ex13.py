#Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
#Exemplo de uso:
#harry=funcionário("Harry",25000)
#harry.aumentarSalario(10)
class Funcionario:
    def __init__(self, nome, salario, vendas):
        self.nome = nome
        self.salario = salario
        self.vendas = vendas

    def aumento_salarial(self, porcentagem):
        conversao_porcentagem = porcentagem / 100
        promocao = self.salario * (conversao_porcentagem + 1.00)
        print(f'Devido ao seu desempenho, o funcionario {self.nome} recebeu um aumento salarial para R${promocao:.2f}! ')


trabalhador1 = Funcionario('Carlos', 1500, 80)
trabalhador2 = Funcionario('Andreia', 1800, 250)
trabalhador3 = Funcionario('Daniel', 3000, 110)

def calculo_aumento(funcionario):
    if funcionario.vendas >= 0 and funcionario.vendas <= 100:
        funcionario.aumento_salarial(10)

    elif funcionario.vendas > 100 and funcionario.vendas <= 200:
        funcionario.aumento_salarial(25)

    else:
        funcionario.aumento_salarial(40)

calculo_aumento(trabalhador1)
calculo_aumento(trabalhador2)
calculo_aumento(trabalhador3)