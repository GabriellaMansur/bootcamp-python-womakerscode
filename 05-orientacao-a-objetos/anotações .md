## Classes e objetos

### Classes

* Classes são criadas com a palavra passe `class`
* Convenção para nomes de classes em Python: **PascalCasing**.
* `__init__` é o método especial que é sempre chamdo quando um novo objeto da classe é criada
* `__init__()` é chamado de método construtor
* o primeiro parâmetro dos métodos de uma classe é chamdo de `self`, representa a instância sobra a qual o método vai atuar, é usado para se referir a coisas que são do próprio objeto
    * `self` dá acesso a atributos e a outros método daquela mesma instância

```python 
class Televisao:
    def __init__(self): 
        self.ligada = False
        self.canal = 3

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False
```

* Chamando o método contrutor
    * Não é necessário chamar o `self`
    ```python
        tv_sala = Televisao()
        tv_sala.ligar()
        tv_sala.canal = 7 
    ```

* Quando tentamos imprimir o conteúdo de um objeto em python ele retone o endereço de memória
    * `__str__` é um método especial que permite  crirar uma representação em string para uma instância que tenha o tipo definiod pela nossa classe. A função abaixo com `__str__(self) -> str` diz que uma string será retornada
    ```python
        def __str__(self) -> str:
        return f'Televisao - ligada {self.ligada} - canal{self.canal} - volume {self.volume}'
        ```

## Modelagem de um sistema orientado a objetos

 * Modelagem é o processo de identificar oa atores, os dados necessários e o tipo de interação que está ocorrendo. Para um sistema, é necessário conhecer suas regras de negócio

## Construtores

* São métodos especiais que são chamados durante a instanciação de objetos. Sua função é inicializar valores aos dados que são membros da classe quando uma instância é criada.
    * Para toda classe o contrutor existe, mesmo que você não crie o interpretador do python cria um implicitamente
    * O construtor padrão é o `__init__(self)` que só recebe o self como parâmetro. Apesar disso, ele pode ser customizado para receber parâmetros, deixando de ser padrão

```python
# construtor padrão
class MinhaClasse1:
    def __init__(self):
        print('MinhaClasse1: chamou o construtor padrão')

class MinhaClasse2:
    pass # não faz nada

# construtor parametrizado
class MinhaClasse3:
    def __init__(self, param):
        print(f'MinhaClasse3: chamou o construtor paramametrizado com o parâmetro {param}')

objeto1 - MinhaClasse1()
objeto2 - MinhaClasse2()
objeto3 - MinhaClasse3('meu objeto')
```

## Destrutores

* Análogos aos construtores com objetivo oposto: são executados quando um objeto é destruído
    * Seu função pe liberar a memória que o objeto estava usando quando ela não é mais necessária
* O nome de um método destrutor é `__del__(self)`
    * Em geral, não é comum ver destrutores em códigos Python porque eles são executados automaticamente.

## Atributos de visibilidade e encapsulamento

### Encapsulamento
* Em Pythom, os métoos e atributos declaraodos em uma classe são públicos, podem ser acessados por outros códigos externos à classe. Sendo assim, alguns atributos e métodos só existem na paea paea seu funcinamento interno e se forem alterados, podem geral mal funcionamento no código
* Existem duas convenções (regras de encapsulamento) que são utilizadas em Python para se iniciar nomes de métodos e atributos:
    * **Protegidos**: Atributos e métodos que têm seus métodos iniciados com __(_underscore_) não devem ser acessados pelo mundo externo a não ser que o usuário saiba exatamenete o que está fazendo, ou seja, ainda pode exixstir algum caso de uso em que faço sentido ter acesso a esse método/atributo
    * **Privados**: Atributos e métodos que têm seus nomes iniciados com __(_undercore_) não devem ser acessados pelo mundo externo de nenhuma forma

* Existe uma forma de controlar um pouco melhor como um usuário vai acessar os atributos de uma classe, que é através de **propriedades**
    * Propriedades nos dão acesso a variáveis que se parecem com atributos, mas na verdade usam métodos por trás dos panos. Elas podem ser definidas pelo uso do _decorator_ `@property`. Esse decorator cria o método `getter` da propriedade
    * Para alterar o valor de uma propriedade externa à classe, é preciso criar o método `setter`

```python
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
```

## Herança e Hernça Múltipla (mixins)

### Herança
* A sintaxe para indicar a herança é colocar o nome da classe pai dentro do parênteses da classe filha `class ClasseFilha(ClassePai)`
    * Exemplo:
```python
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
 ```
* Os métodos e variaveis da classe pai podem ser acessados com a função `super()`
* Atributos privados não podem ser alterados em classes filhas
* Em Python, todas as classes herdam da classe object. Isso faz com que toda classe já comece com vários métodos e atributos.
* A função `dir` mostra os atributos e métodos de um determinado objeto ou classe. Note que as propriedades privadas aparecem aqui também, mas com nomes diferentes
* Como testar se um objeto é uma instância de determinada classe? Usando o método `isinstance(objeto, classe)`
    * Continuando com o exemplo anterior:
```python
print('O objeto estudante é uma instância da classe Estudante? ', isinstance(estudante, Estudante))
print('O objeto estudante é uma instância da classe Pessoa? ', isinstance(estudante, Pessoa))
```
* `issubclass(classe1, classe2) é um teste ebtre classes` => a segunda classe é uma subclasse da primeira classe?
```python
print('A classe Estudante é uma sub-classe de Pessoa? ', issubclass(Estudante, Pessoa))
print('A classe Pessoa é uma sub-classe de Estudante? ', issubclass(Pessoa, Estudante))
```

### Herança Múltipla
* Hernaça múltipla, em Python, significa que uma claase pode herdar mais de uma classe pai. As vezes, classes que herdam de mais de uma classe são chamadas de mixins.
* O caso de uso mais legítimo é na criação de um _framework_

## Classes Abstratas e Biblioteca ABC
* Poder ser considerada como um modelo para crirar outras classes
* Ao crirar os métoos e propriedades de uma classe abastrata, eles devem obrigatoriamente
* Método abstrato tem uma delcração, mas não tem um implementação
* Não é possível criar um objeto diretamente da classe abstrata. Para isso, devemos, necessariamente, crirar uma outra classe que herdeira da classe abstrata, sobreescreve todos os métodos e propriedades, e assim é possivel instanciar dessa classe filha
* Python tem o módulo `ABC` _(Abstratct Base Classes)_ que fornece a funcionalidad de classes abstratas. A classe abstrata precisa herdar de `ABC` e métodos abstratos são marcados com o _decorator_ `@abstractmethod`
* Uma classe filha derivada de uma classe abstrata precisa implementar todos os métodos e propriedades abstratas. Caso contrário, não é possível criar objetos da classe filha.
* Exemplo:
```python
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
```
* **Por que usar classes abstratas?**
    * Ao criar classes abstratas, você define uma interface comum para que todas as classes filhas sigam, ou seja, as classes abstratas são usadas para definir a API de suas classes filhas. 
    * Outro caso de uso é o trabalho em uma equipe/empresa grande que vai precisar criar componentes que fazem coisas semelhantes em diferentes partes do software. Geralmente, um arquiteto define a API que deve ser seguida pelos diferentes componentes

## Erros e exceções
* Há dois tipos de erros, os eros de sintaxe e as exceções. As exceções são erros relacionados à lógico do programa.
* **Exceções** são relacionadas a lógicca de execução, ou seja, durante a execução de uma linha do programa.
* É possível tornar o seu programa mais robusto através do tratamento de exceções. Ou seja, podemos deixar indicar no nosso código o que fazer quando uma exceção acontecer para evitar que a execução seja interrompida.
* Para issso, utilizamos as palavras chave `try`, `catch` e `finally`
    * Colocamos o código que pode lançar exceções dentro do bloco `try`
    * Utilizamos o bloco `catch` para capturar e tratar qualquer exceção que possa vir a ser lançada pelo código no bloco `try`.
    * Podemos adicionar um bloco `else` com código que só vai ser executado se nenhuma exceção acontecer
    * Se existe alguma coisa que precisa ser executada indepedendo ou não do erro acontecer, podemos utilizar opcionalmente o bloco `finally` 
```python
try:
    # Algum código.... 
except:
    # Bloco opcional para lidar com uma exceção (se necessário)
else:
    # Código para ser executado se não ocorrer nenhuma exceção no try
finally:
    # Código para sempre ser executado independente de acontecer
    # alguma exceção ou não
```