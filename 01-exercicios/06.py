velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

distancia = float(input('Digite quantos quilometros tem o percuso da sua viagem: '))

tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

print(f'O tempo da sua viagem é: \n Avião: {tempo_aviao:.2f}h \n Carro: {tempo_carro:.2f} h \n Ônibus: {tempo_onibus:.2f} h' )