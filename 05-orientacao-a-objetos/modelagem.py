from estacionamento import *
from random import randint

#inicializa duas listas com motos e carros
carros = []
for i in range(10):
    placa = randint(1000, 9999)
    carros.append(Carro(placa))

motos = []
for i in range (20):
    placa = range(1000, 9999)
    motos.append(Moto(placa))

# inicializa o estacionamento
estacionamento = Estacionamento(5, 5)
print(estacionamento)

# estaciona 4 carrps
for i in range(4):
    estacionamento.estacionar_carro(carros[i])
print(estacionamento)

# estaciona 6 motos
for i in range(6):
    estacionamento.estacionar_moto(motos[i])
print(estacionamento)


# um carro sai do estacionamento e libera uma vaga
estacionamento.remover_carro(carros[0])
print(estacionamento)