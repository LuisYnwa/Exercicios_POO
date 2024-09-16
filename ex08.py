#Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().

# Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class monki:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = ''

    def comer(self, comida):
        self.bucho += comida + ', '
    
    def verBucho(self):
        if self.bucho: #verifica de forma abreviada se ha algo no bucho dele 
            print(f'O macaco {self.nome} tem no bucho: {self.bucho}')
        else:
            print(f'O macaco {self.nome} ta de buxin vazio!!')

    def digerir(self):
        self.bucho = ''
        print(f'O macaco {self.nome} digeriu tudo!!')

macaco1 = monki('Delfo')
macaco2 = monki('Wukong')

macaco1.comer('banana')
macaco1.comer('maçã')
macaco1.comer('laranja')
macaco2.comer('manga')
macaco2.comer('abacaxi')
macaco2.comer('uva')

# Verificando o conteúdo do bucho após cada refeição
macaco1.verBucho()
macaco2.verBucho()

# Digerindo os alimentos
macaco1.digerir()
macaco2.digerir()

# Verificando o conteúdo do bucho após a digestão
macaco1.verBucho()
macaco2.verBucho()

# Fazendo um macaco comer o outro (macaco canibal)
macaco1.comer('Wukong')
macaco1.verBucho()
macaco1.digerir()