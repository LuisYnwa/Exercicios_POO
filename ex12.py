 #Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento: 
    def __init__(self, saldo, taxa_juros): #calculo usando a logica de juros compostos  
        self.saldo = saldo
        self.taxa_juros = taxa_juros 
    
    def adicione_juros(self):
        juros_convertido = self.taxa_juros / 100
        acrescimo = self.saldo * (juros_convertido + 1.00)
        rendimento = acrescimo - self.saldo
        self.saldo = acrescimo 
        print(f'Voce deixou seu dinheiro na poupanca e com a taxa de juros a {self.taxa_juros}%, com isso, rendeu R${rendimento:.2f} e agora possui {self.saldo:.2f} no saldo final da conta!')
        

conta_poupanca = ContaInvestimento(1000, 10)
conta_poupanca.adicione_juros()
conta_poupanca.adicione_juros()
conta_poupanca.adicione_juros()
conta_poupanca.adicione_juros()
conta_poupanca.adicione_juros()