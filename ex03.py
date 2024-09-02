#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
class Retangulo:
    def __init__(self, LadoA, LadoB):
        self.Muda_lado(LadoA, LadoB)


    def Muda_lado(self, LadoA, LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB


    #def retorna_lado(self):
        #return self.LadoA, self.LadoB

    def calcula_area(self):
        return self.LadoA * self.LadoB

    def calcula_perimetro(self):
        return (self.LadoA * 2) + (self.LadoB * 2)


resultado = Retangulo(5, 10)
resultado_area = resultado.calcula_area() #importante mandar a funcao para uma variavel para nao acabar  printando o index do objeto ao inves do resultado em si
resultado_perimetro = resultado.calcula_perimetro()
print(f'Você precisará de {resultado_area} metros de pisos e {resultado_perimetro} metros de rodapé para construir o local')

resultado.Muda_lado(10, 8)
#outra forma valida de printar, dessa vez chamando os metodos junto com a variavel resultado dentro da frase
print(f'Você precisará de {resultado.calcula_area()} metros de pisos e {resultado.calcula_perimetro()} metros de rodapé para construir o local')
