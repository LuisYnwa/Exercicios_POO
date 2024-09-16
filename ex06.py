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
            return self.volume 

    def aumentar_volume(self, quantidade_aumentada):
        if self.volume + quantidade_aumentada >= 100:
            print('Nao sera possivel aumentar o volume pois o volume da TV passara do limite estipulado')
            return self.volume
        else:
            self.volume += quantidade_aumentada
            return self.volume
        
    def mudar_canal(self, canal_mudado):
        if canal_mudado > 5:
            print('Esse codigo de canal nao esta disponivel em nossa rede!')
            return self.canal
        else:
            self.canal = canal_mudado 


    
teste_TV = TV(4)
abaixa = teste_TV.abaixar_volume(30)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {abaixa}%')
aumenta = teste_TV.aumentar_volume(160)
mudanca_canal = teste_TV.mudar_canal(2)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')
aumenta = teste_TV.aumentar_volume(50)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')
mudanca_canal = teste_TV.mudar_canal(1)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')
mudanca_canal = teste_TV.mudar_canal(8)
print(f'Voce esta no canal {teste_TV.canal} e o volume da tv esta em {aumenta}%')




