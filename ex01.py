class Bola:
    def trocaCor(self, cor):
        self.cor = cor
    def mostraCor(self):
        print(self.cor)

bola = Bola()
bola.trocaCor("Amarelo")
bola.mostraCor()
