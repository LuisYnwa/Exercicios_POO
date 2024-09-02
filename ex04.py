#Classe Pessoa: Crie uma classe que modele uma pessoa:

#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1 

    def engordar(self, kgs):
        self.peso += kgs

    def emagrecer(self, kgs):
        self.peso -= kgs
    
    def crescer(self, cms):
        self.altura += cms

dados_finais = Pessoa('Rafaelo', 18, 81, 187)
dados_finais.envelhecer(5)
print(f'A pessoa {dados_finais.nome} envelheceu para {dados_finais.idade} ano(s)')
print(f'E por estar na fase de crescimento, ela cresceu para {dados_finais.altura}cm ao todo!')

dados_finais2 = Pessoa('Jenilson', 11, 70, 165)
dados_finais2.envelhecer(5)
print(f'A pessoa {dados_finais2.nome} envelheceu para {dados_finais2.idade} ano(s)')
print(f'E por estar na fase de crescimento, ela cresceu para {dados_finais2.altura}cm ao todo!')
