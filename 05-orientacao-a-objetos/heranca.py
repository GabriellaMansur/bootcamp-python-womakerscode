# Pessoa é a classe base
class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self.tipo = 'Pessoa'

    def falar_oi(self):
        print('Oi" Meu nome pe '.format(self._nome))

    def falar_tipo(self):
        print('Meu tipo é {}'.format(self._tipo))

pessoa = Pessoa('Naira')
pessoa.falar_oi()
pessoa.falar_tipo()
print()


class Estudante(Pessoa): # nome da classe base entre parênteses
    def __init__(self, name, curso):
        super().__init__(name) # chamando construtor da classe base
        self._curso = curso

    def falar_curso(self):
        print(f'Eu, {self._nome}, estudo o curso {self.curso}') # self._nome é herdade da classe base

    def falar_tipo(self):
        self._tipo = 'Estudante'
        return super().falar_tipo() 
    
estudante = Estudante('Yasmin', 'Introdução ao Python')
estudante.falar_oi() # o método "falar_oi" é herdado da classe base
estudante.falar_tipo() # o método "falar_tipo" é herdado da classe base, e sobrescrito na classe derivada
estudante.falar_curso()
print()