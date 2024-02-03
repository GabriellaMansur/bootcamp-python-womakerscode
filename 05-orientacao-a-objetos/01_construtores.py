# construtor padrão
class MinhaClasse1:
    def __init__(self):
        print('MinhaClasse1: chamou o construtor padrão')

class MinhaClasse2:
    pass #não faz nada

# construtor parametrizado
class MinhaClasse3:
    def __init__(self, param):
        print(f'MinhaClasse3: chamou o construtor paramametrizado com o parâmetro {param}')


objeto1 - MinhaClasse1()
objeto2 - MinhaClasse2()
objeto3 - MinhaClasse3('meu objeto')