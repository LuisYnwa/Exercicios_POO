 #Faça um programa completo utilizando classes e métodos que:

#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos: tipoCombustivel, valorLitro, quantidadeCombustivel

#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class Bombacombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel): #quantidadeCombustivel eh medida por litro e diz quanto possui disponivel na bomba
    #1 litro = R$5 nos testes
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, dinheiro):
        quantos_litros = dinheiro / self.valorLitro
        print(f'Com o preco do litro a R${self.valorLitro}, voce abasteceu {quantos_litros:.1f} litros com {self.tipoCombustivel}!')
        self.quantidadeCombustivel -= quantos_litros

    def abastecerPorLitro(self, litroso):
        valor_final = litroso * self.valorLitro
        print(f'Voce colocou {litroso} litros de {self.tipoCombustivel} por R${valor_final}')
        self.quantidadeCombustivel -= litroso

    def alterarValor(self, valor_novo):
        self.valorLitro = valor_novo
        print(f'Valor alterado com sucesso para {self.valorLitro}!')

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
        print(f'Tipo de combustivel alterado com sucesso para {self.tipoCombustivel}!')

    def AbastecerBomba(self, abastecimento): #antigo alterarQuantidadeCombustivel do enunciado
        self.quantidadeCombustivel += abastecimento
        print(f'A bomba de combustivel foi abastecida com sucesso e agora conta com {self.quantidadeCombustivel} litros no total!')

carro_aditivado = Bombacombustivel('Aditivada', 5, 100)
caminhao = Bombacombustivel('Diesel', 3, 350)
carro_aditivado.abastecerPorLitro(10)
caminhao.abastecerPorLitro(50)
carro_aditivado.alterarCombustivel('Gasosa Comum')
carro_aditivado.abastecerPorValor(30)
carro_aditivado.AbastecerBomba(50)
caminhao.alterarValor(7)
caminhao.abastecerPorValor(21)


