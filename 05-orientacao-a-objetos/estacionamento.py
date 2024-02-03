class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

class Moto:
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False


class Vaga:
    def __init__(self, identificador, tipo):
        self.id = identificador
        self.livre = True

        if tipo is not 'carro' and tipo is not 'moto':
            raise ValueError(f'O tipo de vaga {tipo} não foi reconhecido')

        self.tipo = tipo
        self.placa = None

    def ocupar(self, placa):
        if self.livre is False:
            raise ValueError(f'A vaga {self.identificador} já está ocupada')

        self.placa = placa
        self.livre = False 

    def desocupar(self, placa):
        if self.livre is True:
            raise ValueError(f'A vaga {self.identificador} já está livre')

        self.placa = None
        self.livre = True


class Estacionamento:
    def __init__(self, total_vagas_livres_carro, total_vagas_livres_moto):
        self.carro_para_vaga = {}
        self.moto_para_vaga = {}
        self.total_vagas_livres_carro = total_vagas_livres_carro
        self.total_vagas_livres_moto = total_vagas_livres_moto
        self.inicializar_vagas()

    def inicializar_vagas(self):
        self.vagas_carro = {} #id da vaga p/ o objeto de vaga de carro
        self.vagas_moto = {}

        tipo = 'carro'
        for i in range(self.total_vagas_livres_carro): # i vai de 0 a 4
            self.vagas_carro[i] = Vaga(i, tipo) #i: é o id, tipo: é o tipo carro

        primeiro_id_motos = self.total_vagas_livres_carro
        ultimo_id_motos = primeiro_id_motos + self.total_vagas_livres_moto
        tipo = 'moto'
        for j in range(primeiro_id_motos, ultimo_id_motos):
            self.vagas[j] = Vaga(j, tipo)

    def estacionar_carro(self, carro: Carro):
        if carro.estacionado is True:
            raise ValueError(f'O carro {carro.placa} já está estacionado.')

        id_da_proxima_vaga, tipo = self.burcar_ida_da_proxima_vaga_livre('carro') #gera o id da próxima vaga
        if id_da_proxima_vaga is None:
            raise ValueError(f'Não há mais gavas de carro disponíveis no estacionamento.')
        elif id_da_proxima_vaga is not None and tipo is 'carro':
            vaga = self.vagas_carro[id_da_proxima_vaga]
            vaga.ocupar(carro.placa)
            carro.estacionar()
            self.carro_para_vaga[carro.placa] = vaga.id #permite achar imediatamente em qual vaga está o carro
            self.total_vagas_livres_carro -= 1 # reduz o número de vagas livres
        else:
            raise RuntimeError(f'Erro interno - não foi possível recuperar a próxima vaga de carro')

        print(f'Carro {carro.placa} estacionado na vaga {vaga.id} do tipo {vaga.tipo}')