#Classe Pessoa: Crie uma classe que modele uma pessoa:

#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

#A CORRIGIR
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        #self.envelhecer(idade)
        #self.envelhecer(altura)
        
    def envelhecer(self, idade, altura):
        self.idade = idade
        self.altura = altura
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1 

    def engordar(self, peso):
        self.peso = peso
        peso += 1

    def emagrecer(self, peso):
        self.peso = peso
        peso -= 1
    
    def crescer(self, altura):
        self.altura
        altura += 1.0 

dados_finais = Pessoa('Rafaelo', 23, 81, 1.87)
print(f'A pessoa {} envelheceu {} ano(s)')
print(f'E por estar na fase de crescimento, ela cresceu {}cm ao todo!')