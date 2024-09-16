#Crie uma classe que modele um tamagotchi (Bichinho Eletrônico):

#Atributos: Nome, Fome, Saúde e Idade
# Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagotchi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class Ursinho:
    def __init__(self, nome, idade, humor = 'Satisfeito', fome = 50, saude = 50):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = humor

    
    def mudar_nome(self, nome_novo):
        self.nome = nome_novo
        return (f'O novo nome do seu ursinho eh {self.nome}!')
    
    def alimentar(self):
        if self.fome >= 100:
            print('O ursinho ja esta satisfeito e nao precisa comer mais por agora!!')
        else:
            self.fome += 25
            return f'O ursinho foi alimentado! Fome atual: {self.fome}'
    
    def curar(self):
        if self.saude >= 100:
            print('O ursinho ja esta curado!!')
        else:
            self.saude += 25
            return f'O ursinho foi curado! Saúde atual: {self.saude}'
    
    def envelhecer(self):
        self.idade += 1
        return f'O ursinho cresceu! Idade atual: {self.idade}'

    def infos_gerais(self):
        if self.saude + self.fome >= 150:
            self.humor = 'Feliz'
        elif self.saude + self.fome >= 100 and self.saude + self.fome < 150:
            self.humor = 'Satisfeito'
        else:
            self.humor = 'Triste'
        print(f'Nome:{self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Saude: {self.saude}')
        print(f'Fome: {self.fome}')
        print(f'Humor: {self.humor}')

tamagotchi = Ursinho('Pedroaldo', 5)
tamagotchi.infos_gerais()
tamagotchi.alimentar()
tamagotchi.curar()
tamagotchi.envelhecer()
tamagotchi.infos_gerais()








