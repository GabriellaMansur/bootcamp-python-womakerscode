class Quadrado:
    def __init__(self, medida):
        self.altura = medida
        self.largura = medida
    
    @property # decorator
    def altura(self):
        return self.__medida # retorna uma variável que é privada
    
    # p/ alterar o valor tem que chmar o método setter
    @altura.setter
    def altura(self, valor):
        # executa algum tipo de validação
        self.__medida = valor # alterando valor da variável privada

    @property
    def largura(self):
        return self.__medida
    
    @largura.setter
    def largura(self, valor):
        #executa algum tipo de validação
        self.__medida = valor

    def area(self):
        return self.largura * self.altura