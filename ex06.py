#Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
#A CORRIGIR

class TV:
    def __init__(self, canal, volume=50):
        self.canal = canal
        self.volume = volume
    
    def abaixar_volume(self, quantidade_reduzida):
        if quantidade_reduzida >= self.volume:
            print('Nao sera possivel abaixar o volume pois a TV ja esta no mudo, tente aumenta-lo')
        else:
            self.volume -= quantidade_reduzida
            return self.volume #tentar quantida-reduzida se nao der certo

    def aumentar_volume(self, quantidade_aumentada):
        if self.volume >= 100:
            print('Nao sera possivel aumentar o volume pois a TV ja esta no no maximo, tente abaixa-lo')
        else:
            self.volume += quantidade_aumentada
            return self.volume
        
    #def mudar_canal(self, canal_mudado):


    
teste_TV = TV(4)
abaixa = teste_TV.abaixar_volume(30)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {abaixa}%')
aumenta = teste_TV.aumentar_volume(60)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')
aumenta = teste_TV.aumentar_volume(60)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')
abaixa = teste_TV.abaixar_volume(150)
