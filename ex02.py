class Quadrado:
    def __init__(self, lado):
        self.Muda_lado(lado)

    def Muda_lado(self, lado):
        self.lado = lado

    def Retorna_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado * self.lado

resultado = Quadrado(4)
print(resultado.calcula_area())
resultado.Muda_lado(5)
print(resultado.calcula_area())

