from abc import ABC, abstractmethod

class ClasseAbstrata(ABC):
    @abstractmethod
    def metodo_abstrato(self):
        pass

    @property
    @abstractmethod
    def propriedade_abstrata(self):
        pass

class ClasseDerivada(ClasseAbstrata):
    #sobrescrevendo o método abstrato
    def metodo_abstrato(self):
        print('Bom dia!')

    #sobrescrevendo a propriedade abstrata
    @property
    def propriedade_abstrata(self):
        return 'Dia'