class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal =3
        self.canal_min = 1
        self.canal_max = 99
        self.volume_min = 0
        self.volume_max = 100
        self.volume = 30
    
    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.desligada: False
    
    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        
        if self.canal > self.canal_min:
            self.canal -= 1

    def aumentar_volume(self):
        if not self.ligada:
            return
        
        if self.volume < self.volume_max:
            self.volume += 10

    def reduzir_volume(self):
        if not self.ligada:
            return
        
        if self.volume > self.volume_min:
            self.volume -= 10

    def __str__(self) -> str:
        return f'Televisao - ligada {self.ligada} - canal{self.canal} - volume {self.volume}'
    
# Criando instância da classe televisão
tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()

for _ in range(3):
    tv_sala.aumentar_volume()

print('tv_sala volume: {}'.format(tv_sala.volume))

print('tv_sala:', tv_sala)


from datetime import date
# Dia é um objeto, ou seja, uma intância de classe date
dia = date(2019,2, 22)
print('Dia da semana:', dia.weekday())