class Pessoa:
    def falar_oi(self):
        self.nome = "gabi"
        print(f'Oi, meu nome é {self.nome}')

    @property
    def nome(self):
        return self.__nome

pessoa = Pessoa()
pessoa.falar_oi()

