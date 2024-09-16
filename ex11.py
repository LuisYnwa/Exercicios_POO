#Implemente uma classe chamada Carro com as seguintes propriedades:

#Um veículo tem um certo consumo de combustível (medidos em km / liter) e uma certa quantidade de combustível no tanque.
#O consumo é especificado no construtor e o nível de combustível inicial é 0.
#Forneça um método move( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
#Forneça um método getGasoline( ), que retorna o nível atual de combustível.
#Forneça um método addGasoline( ), para abastecer o tanque. 

class Car:
    def __init__(self, consume, gas_level = 0): #gas_level determined by liters 
        self.consume = consume
        self.gas_level = gas_level

    def move(self, kilometers):

    
    def showGasoline(self): #GetGasoline
        print(f'You currently have {self.gas_level} liters in fuel tank')
    
    def addGasoline(self, liters):
        self.gas_level += liters
        print(f'You ve added {liters} to the tank and now have {self.gas_level} liters avaible ')

fiesta = Car(10)
fiesta.addGasoline(20) #200kms until stop 
