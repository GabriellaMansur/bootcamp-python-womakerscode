# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = "Prata"
        self.modelo = "Gol"
        self.velocidade = 100
        self.velocidade_max = 200

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 5

    def desacelerar(self):
        if not self.ligado:
            return
        else:
            self.velocidade -= 5



# Crie uma instância da classe carro.
carro1 = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro1.ligar()
print('O carro está ligado?{}'.format(carro1.ligado))
print(f'Velocidade inicial {carro1.velocidade}')

for _ in range(3):
    carro1.acelerar()

print(f'Velocidade após acelerar {carro1.velocidade}')
# Faça o carro "parar" utilizando os métodos da sua classe.
carro1.desacelerar()
print(f'Desacelerou: {carro1.velocidade}')
carro1.desligar()
print(f'Desligou: {carro1.velocidade}')

