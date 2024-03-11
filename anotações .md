# Apostila de Python

## Conceitos básicos

* Imprimir na tela

```python
print('Olá, mundo')
```

* Entrada

```python
numero_inteiro = int(input('Digite um número inteiro: '))
```

## Estruturas condicionais

* Os operadores condicionais são: `if`, `elif` e `else`

  * Sintaxe if else:

    ```python 
    if(condicao é `True`):
        operacoes
    elif(condicao é `True`):
        operacoes
    else:
        operacoes
    ```

## Laços de repetição

* `while`:

  * Sintaxe:

    ```python 
    while (condicao é `True`):
        operacao_repetida
    ```

    * Exemplo 1:

    ```python
    cont = 1
    while cont <= 5:
        print('Olá, mundo')
        cont += 1
    ```

    * Exemplo 2: enquanto o usuário não digitar o que pe solicitado, continuamos pedindo para ele digitar um novo valor

    ```python
    numero = float(input('Digite um número maior que 77: '))
    while numero <= 77:
        numero = float(input('Número menor ou igual a 77. Digite um número maior que 77: '))
    print('Legal, o número digitado foi', numero)
    ```

## Listas

* Problema gerador: a média de um aluno, a partir das notas informadas por ele.
* Listas são uma estrutura de dados definidas como um **conjunto de objetos** que podem ser de diversos tipos. Veja abaixo um exemplo de como são declaradas:

```python 
lista_numeros = [2, 4, 3, 8, 13]
lista_strings = ['Banana', 'Maçã', 'Uva', 'Manga']
lista_num_strings = [1, 'José', -7]
lista_de_listas = [5, 13, [7, 5], True]
```

* Para acessar elementos específicos de um listas, devemos indicar qual é o **índice** respectivo ao elemento, ou seja, qual pe a posição do elemento dentro da lista. Esse processo é chamado de **indexação**.

```python
minha_lista = ["a", "b", "c"]

#para acessar uma posição i da lista:
minha_lista[i]
```

* Também é possível acessar os últimos elemento de uma lista usando índices negativos

  * Último elemento tem índice -1: `minha_lista[-1]`

  * Penúltimo tenm índice -2: `minha_lista[-2]`
    * E assim por diante
* Acessando pedaços da lista (isso é chamado de *slicing* em Python), basta indicar o intervalo de índices separados por `:` (o intervalo é aberto). Veja:
  * `minha_lista[1:3]` => seleciona sos elementos de índice 1 até  índice 2
  * `minha_lista[:4]` =>  primeiro elemento até o índice 3
  * `minha_lista[3:]` => índice 3 até o final 
    * `minha_lista[:]` => seleciona toda a lista

### Operações com listas

* Soma
  * Ao somar, os elementos são concatenados, na ordem dada, para formar uma lista maior

    ```python
        lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]

        lista3 = lista1 + lista2

        # lista 3 = 1, 2, 3, 4, 5, 6
    ```

* Multiplicação 
  * Ao multiplicar uma liats por um número inteiro os elementos são repetidos na ordem em que aparecem:

    ```python
        lista1 * 3

        #lista1 = 1, 2, 3, 1, 2, 3, 1, 2, 3,
    ```

* Strings = > lista de caracteres

    ```python
        list("Gabi")
        # 'G', 'a', 'b', 'i'
    ```

### Funções de listas

* `append()` => adiciona um elemento no final da lista (só é possível fazer um por vez)

```python
#lista vazia
lista = []

# 5 e 10 foram adiconados na lista vazia
lista.append(5)
lista.append(10)
```

* `insert(posicao, elemento)` => adiciona um lemento em uma posição específica (só é possível fazer um por vez)

```python
# adiconando a strinf morando na posição 2
lista.insert(2, 'morango')
```

* Para redefinrir um elemento da lista individualmente:

```python
#redefininfo elemento da posição 2
lista[2] = 'laranja'
```

* `remove()` => para remover um elemento da lista (remove apenas a primeira aparição do elemento)

```python
lista.remove(10)
```

* `pop()` => remove um elemento de determinado índice

```python
#removendo elemento do índice 3
lista.pop(3)
```

* `sorted()` => para ordenar a lista (só funciona para listas com o mesmo tipo de dados)

```python
lista_numeros = [4, 5, 8, 1, 9]

# para ordenar essa lista
sorted(lista_numeros)
```

* Para inverter a ordem dos elementos, adicionar `[::-1]` no final da lista

```python
lista_numeros[::-1]
```

* `index()` => para mostrar qual é a posição (índice) de determinado elemento (retorna apenas a primeira aparição do elemento)
```python
lista_numeros = [4, 5, 8, 1, 9]

# para mostrar em qual posição está o 8
lista_numeros.index(8)
```
* `extend()` => para incorporar uma lista à outra
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# para incorporara a lista2 na lista 1
lista1.extend(lista2)
```
* `clear()` => para limpar uma lista
* `count()` => número de vezes que um determinado elemento apararece na lista
* `copy()` => para copiar uma lista
* **Propriedades dos elementos de lista**:
    * `max()` => para encontrar o maior elemento
    ```python
    max(lista_numeros)
    ```
    * `min()` => para encontrar o menor elemento
    ```python
    min(lista_numeros)
    ```
    * `len()` => para encontrar o tamanho da lista (número de elementos)
    ```python
    len(lista_numeros)
    ```
  * `sum()` => para somar os elementos da lista
    ```python
    sum(lista_numeros)
    ```
    * Exemplo 1:
    ```python
    # média usando sum() e len()
    media = sum(lista_numeros) / len(lista_numeros)
    ```
    * Exemplo 2:
    ```python
    num_notas = int(input('Digite o número de notas: '))

    # lista de notas vazia inicializada
    notas = []

    cont = 1
    while cont <= num_notas:
        # pega uma nota do usuário
        nota_atual = float(input('Digite uma nota: '))
        notas.append(nota_atual)
        cont += 1

    media = sum(notas) / len(notas)
    print('\nA média é: ', media)
    ```
## Iterador(for)
* Laços são utilizados quando desejamos repeti operações taé que determinada condição seja atingida. Entretanto, é possível entender o `for` como sendo um operador utilizado para **percorrer elementos de uma lista** (ou qualquer objeto **iterável**). Por isso, em Python, o `for` pode ser entendido como uma **função iteradora**
* Sua estrutura é:
```python
for item in lista:
    operacao_feita_para_cada_item
```
* Exemplo:
```python
# percorre todos os elementos da lista e os mostra na tela
lista_numeros = [4, 5, 8, 1, 9]
for item in lista_numeros
    print(item)
```
* Exemplo de uso:
```python
# separando números positivos e negativos de uma lista de números
lista_num = [-10, 2, -6, 4.2, -8, 3.14, -6, 0]
lista_num_pos = []
lista_num_neg = []
lista_num_neutro = []

for elemento in lista_num:
  if elemento < 0:
    lista_num_neg.append(elemento)
  elif elemento > 0:
    lista_num_pos.append(elemento)
  else:
    lista_num_neutro.append(elemento)

print(lista_num_pos)
print(lista_num_neg)
print(lista_num_neutro)
```
## Compreensão de listas
* *list comprehension* é uma estruturna com a qual é possível construir novas listas a partir de outras listas de forma bem condensada.
* A sintaxe é:
```python
[operacao_sobre_os_items for item in lista_base]
```

## Strings
* Como já vimos string representam dados textuais e nada mais é do que uma **coleção de caracteres**
* Para saber o tamanho de uma string:
```python
nome = "Gabriella"
len(nome)
```
* Strings também são objetos iteráveis
```python
for i in nome:
    print(i)

# dá pra fazer o mesmo com o range() e o len()
for i in range(len(nome)):
    print(nome[i])
```
* Nós conseguimos alterar caracteres (ou palavras) com o método "replace()":
```python
nome = nome.replace('G', 'g')
```
* Podemos tranformar uma strinf em uma lista e fazer ela se comportar como uma
```python
list(nome)

nome_lista = list(nome)
```
* Tranformando a lista de volta em string
```python
"".join(nome_lista)
```
* **Funções de strings**:
    * `.lower()`
    * `.upper()`
    * `.tile()`
    * `.capitalize()`
    * `.split()`
    * `.strip()`
    * `isdigit()`
    * `isalpha()`
    * `isalnum()`
    * `isspace()`  

### Formatação de strings

* Para formatar datas:

```python
dia, mes, ano = 7, 4, 2023

"{:02d}/{:02d}/{:04d}".format(dia, mes, ano)

```
* Para floats:
```python

preco = 1299.90

"{:.2f}".format(preco)
```

## Tuplas

* São estrutura de dados e sua princial diferença entre listas é que as tuplas são **imutáveis**
* Suas semelhanças com as listas são:
    * Podem guardar diferentes tipos de dados
    * São indexadas (podemos acessar elementos por índices)
    * São iteráveis (podemos percorrer com o `for`)
* Já que não podemos mudar nada nelas, **para que servem as tuplas?**
    * É uma forma de sinalizar que esses dados não deveriam ser alterados
    * É um meio de garantir que os elementos estarão em uma ordem específica
    * O o acesso a elementos de uma tupla é bem mais rápido
* Tuplas são inicializadas com uma sequência de valores entre parênteses

```python
tupla = (1, 3, "ada", False)
```

* Também é possível definir tuplas sem parênteses

```python
# tuple unpacking

x, y = 2, 3

# x = 2
# y = 3
```
## Dicionários

* Outra estrutura de dados importante em Python são os dicionários. Ele também é uma coleção de dados. A diferença é que um dicionário é definico por dpois elementos: uma **chave** e um **valor**
  * A **chave** é utilizada como se fosse um índice paara identificar seus respectivos valores. Elas podem ser de qualquer tipo que é **imutável**: int, float, string, booleano, tuplas, etc
    * O **valor** pode ser qualquer dado, um int, um float, uma str, um bool, uma lista, uma tupla, outro dicionário...
* Dicionários são inicializados entre chaves:

```python
dicionario = {"chave": valor}
```

* **Para acesssar elementos**
    * dicionario.values()
    * dicionario.items()
    * dicionario.keys()
    * dicionario[indice]
  * del dicionario[índice]
    * dicionario.pop(índice)

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

## Django Web (framework)

* Fundamentos de arquitetura e o padrão MVT
* Ele usa o MVT (Model View Template)
  * Model é a camada de dados, ela define a estrutura do bando de dados
* View lida com a lógica do processamento
  * Template do Django define como o noddos dados serão mostrados para os usuários
* **Diferença entre MTV e MVC**
  * A MVC tem um controller que é responsável por receber e responder as solicitações do usuário. No MVT tem não tem uma camada específica para isso, quem faz esse controle é a view

### Django

* Montar páginas (templates)
* Interagir com diversos bancos de dados (ORM)
* Validar input dos usuários  (forms)
* Controlar acesso (authotization)
* Gerenciar a aplicação (admin)

* **Instalando o ambiente virtual e django**
  * Por que temos que usar o ambiente virtual? Para garantir que os nosso pacotes e intalação vão ser feitas todas localmente, assim vamos ter a garantia que tudo vai ter sido devidamente instalado em uma pasta. Os passos gerais são => instalação, criação e ativação do ambiente  virtual. Posteriormente para o projeto, só é necessário garantir que ele esteja ativado
    * **Intalação:** Entre no terminal no vs code e digite `pip install virtualenv`
    * **Criação:** `python -m venv [nome_do_ambiente]`
    * **Ativação:** entre dentro da pasta criada e digite  `.\Scripts\activate`
    * Depois é só ir em open folder, selecionar a pasta que criamos e abrir
    * Dentro da pasta instale o django usando o comando ``pip install django `
    * Crirar projeto, já dentro da pasta e com o ambiente virtual ativado, `django-admin strate`
