
# 📚 Resumo de aulas da seção 5 do curso

## Classes

Por convenção, é utilizado PascalCase para a nomenclatura de classes

Para criar uma classe:

```python
class NomeDaClasse:
  ...
```

Classes são como moldes para serem reutilizados e organizar dados.

## `__init__`

```python
class Pessoa:
  def __init__(self, nome, sobrenome):
      self.nome = nome
      self.sobrenome = sobrenome

p1 = Pessoa('Guilherme', 'Yamada')
p2 = Pessoa('Giovanna', 'Yumi')

print(p1.nome)
```

Saída:
```python
Guilherme
```

No exemplo à cima, foi criado um molde para pessoa, contendo nome e sobrenome, podendo ser criado várias pessoas com esse molde.

self é necessário para a classe, indica o nome do argumento em que a pessoa x será salva.

## Método em instância de classes 

```python
class Pessoa:
    def __init__(self, nome, sobrenome):
      self.nome = nome
      self.sobrenome = sobrenome
    
    def correr(self):
        print(f'{self.nome} está correndo')

p1 = Pessoa('Guilherme', 'Yamada')
p2 = Pessoa('Giovanna', 'Yumi')

print(p1.nome)
p1.correr():
```
## Mantendo estado dentro da classe

As classes conseguem manter na 'memória' os estados de cada objeto da classe:

```python
class pet:
  def __init__(self, nome, bebendo=False):
    self.nome = nome
    self.bebendo = bebendo

  def beber(self):
    if self.bebendo:
      print(f'{self.nome} já esta bebendo...')
      return

    self.bebendo = True
    print(f'{self.nome} começou a beber')

  def parar_beber(self):
    if not self.bebendo:
      print(f'{self.nome} não está bebendo...')
      return
    
    self.bebendo = False
    print(f'{self.nome} parou de beber')
  
  def latir(self):
    if self.bebendo:
      print(f'{self.nome} está a beber, não consegue latir no momento')
      return
    
    print(f'{self.nome} latiu')

p1 = pet('Levi')
p2 = pet('Hana')

p1.beber()
p1.beber()
p1.latir()
p2.latir()
p1.parar_beber()
p1.latir()
```

Saída:

```python
Levi começou a beber
Levi já esta bebendo...
Hana latiu
Levi está a beber, não consegue latir no momento
Levi parou de beber
Levi latiu
```
Hana conseguiu latir, pois estava sem fazer nada, enquanto Levi precisou parar de beber para latir

## Atributo de classes

São valores que são atribuidos mais acima do escopo, que estão disponíveis para todas as instâncias

Exemplo:

```python
class falas:
    hora = 'oi'
    def __init__(self, nome):
       self.nome = nome
       self.hora = 'olá'
    def cumprimentar(self):
      print(f'{falas.hora}, me chamo {self.nome}')

p1 = falas('Guilherme')
p1.cumprimentar()
```

É possível usar a hora, utilizando a class.hora ou self.hora  
OBS: self.hora foi mudado no escopo do `__init__`

## `__dict__`e vars para atributos de instância

```python
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
  def faz_nada(self):
    ...
p1 = Pessoa('Guilherme', 23)
print(p1.__dict__)
print(vars(p1))
```
Saída:
```python
{'nome': 'Guilherme', 'idade': 23}
{'nome': 'Guilherme', 'idade': 23}   
```

com `__dict__` você pode acessar ou modificar o dicionário  
com vars, é mais legível e você pode acessar o dicionário

## Métodos de classe

Pode se criar moldes com alguma das instâncias como padrão

```python
class blabla:
    ...
@classmethod
def sem_nome(cls,idade):
    return cls('Anônimo', idade)

p1 = Pessoa.sem_nome(23)
print(p1.nome, p1.idade)
```
Saída:

```python
Anônimo, 23
```

## Diferença entre method, classmethod e staticmethod

method:
Recebe self, acessa atributos da instância.
→ Usado para comportamentos do objeto.

@classmethod:
Recebe cls, acessa atributos da classe.
→ Usado para fábricas ou lógica comum a todas as instâncias.

@staticmethod:
Não recebe self nem cls, é só uma função comum dentro da classe.
→ Usado para utilitários relacionados à classe, mas independentes dela.

## Property - getter pythonico

O que é um getter?
O getter serve para proteger o acesso direto ao atributo
Podendo dar liberdade de mudar uma implementação interna sem mudar a interface pública
Também chamado de encapsulamento

Property é o modo pythonico de se utilizar um getter

```python
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def cor(self):
        return self.cor_tinta
```

Deste modo é possível chamar caneta.cor (inferface pública),
sem acessar internamente a interna.

## property+setter getter e setter pythonicos

Consenso geral: caso a instância ou método possua um atributo nomeado com _ na frente, é um aviso para não se utilizar diretamente o valor.

setter sempre vem acompanhado do getter

setter 

Ele permite adicionar validação, regras de negócio ou lógica extra ao definir um valor, sem que o usuário perceba que está usando um método.

```python
class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):  # Getter
        return self._preco

    @preco.setter
    def preco(self, valor):  # Setter
        if valor < 0:
            raise ValueError('O preço não pode ser negativo')
        self._preco = valor
p1 = Produto('chaveiro')
p1.preco = 10
```

setter está entrando como uma regra para redefinição, além da chamada dele ser mais interativa.


## Encapsulamento (modificadores de acesso:public, protected, private)
Python não tem esses modficadores, mas consegue utilizar métodos para simulalos.

public(sem underline):  
pode ser utilizado em qual quer lugar

protected(um underline):
não deve ser usado fora da classe ou em suas subclasses

private(dois underlines):
Só deve ser utilizado na classe em que foi declarada

## Relações entre classes: Associação, agregação e composição

Associação:
Duas classes independentes, onde uma utiliza a outra, mas nenhuma depende da outra para existir.

Agregação:
Duas classes independentes, onde uma possui a outra, mas a parte pode existir separadamente do todo.

Composição:
Uma classe possui e controla a outra, e a parte não existe separadamente — sua vida depende do todo.



<p align="center">
  <img <img src="https://github.com/user-attachments/assets/5bce3995-f6c9-4e4a-bbef-af709cb0ebf1" /> alt="Imagem de lógica">
</p>

<p align="center">
  <em>[imagem retirada do site 'python.pages', em 19/07/2025]</em>
</p>

## Notas sobre classes

**Inicializar com atributos ainda indefinidos:**
```python
class Pc:
    def __init__(self, versao):
        self._versao = versao
        self._placa = None
        self._marca = None
```

Quando usar isso:

Quando você ainda não tem todas as informações no momento da criação do objeto.

Ou quando esses valores serão definidos depois, via métodos, setter ou outros processos.

Útil para relacionar objetos depois, como associar uma Placa e uma Marca a esse Pc.

O agregador que irá utilizar o getter e o setter, ele será o "controlador" das ligações

**Inicializar com tudo já disponível:**
```python
class Pc:
    def __init__(self, versao, placa, marca):
        self._versao = versao
        self._placa = placa
        self._marca = marca
```
Quando usar isso:

Quando você já tem todas as informações necessárias para criar o objeto completo.

Mais direto e simples, sem necessidade de setter para definir atributos depois.

## Herança, generalização e especialização

Cliente é uma especialização de Pessoa  
Cliente herda características de Pessoa(subclasse)

Pessoa é uma generalização de Cliente  
Pessoa é a superclasse que generaliza comportamentos comuns (como nome, CPF, etc)

## Herança simples
```python
class Char:
  def __init__(self, name, power):
    self.name = name
    self.power = power
  def who(self):
    print('oi')
    print(f'Name: {self.name}\n Power: {self.power}\n Class: {self.__class__.__name__}')

class Hero(Char):
  ...

class Villain(Char):
  ...

h1 = Hero('Spider Man', 'Spider sense')
h1.who()
v1 = Villain('Sandman', 'Manipulation')
v1.who()
```

Saída:
```python
oi
Name: Spider Man
 Power: Spider sense
 Class: Hero
oi
Name: Sandman
 Power: Manipulation
 Class: Villain
```
 Para fazer uma classe que possui herança de outra, basta criar com a superclasse dentro dos parênteses como mostrado em:
```python
 class Hero(Char):
#Char é a super classe
#Hero é a classe que herda
```
Todo oque Char tem, Hero irá herdar, inclusive seus métodos, o 'oi' no exemplo acima é impresso, mas poderia ser mudado adicionando o mesmo método nas heranças:

```python
class Hero(Char):
  def who(self):
    print('Executei em hero')
    print(f'Name: {self.name}\n Power: {self.power}\n Class: {self.__class__.__name__}')

class Villain(Char):
  def who(self):
    print('Executei em Villain')
    print(f'Name: {self.name}\n Power: {self.power}\n Class: {self.__class__.__name__}')
```
Saída: 
```python
Executei em hero
Name: Spider Man    
 Power: Spider sense
 Class: Hero        
Executei em Villain 
Name: Sandman       
 Power: Manipulation
 Class: Villain    
```

 As chamadas das classes seguem a ordem de MRO(Method Resolution Order):
 Procure o método na própria classe. Se não tiver, suba para a classe pai (superclasse), e assim por diante.

 
## Super e sobreposição de membros

Quando uma classe herda de outra classe, todos seus métodos são herdados também, caso haja necessidade de adição de regras em um método já herdado, é utilizado o super().

Exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Nome: {self.nome}\nIdade:{self.idade}')
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario
    def apresentar(self):
        super().apresentar()
        print(f'Cargo: {self.cargo}\nSalario:{self.salario}')

p1 = Pessoa('Gui', '23')
p1.apresentar()
p2 = Funcionario('Gio', '21', 'efetivada',2500)
p2.apresentar()

```

p1 acessa a super classe, no qual só printa nome e idade,
p2 acessa a subclasse, que possui nome, idade, cargo e salario

ainda é possivel o uso da p2 no método de apresentação da classe Pessoa:

```
Pessoa.apresentar(p2)
```


## Herança múltipla


Uma classe pode herdar de mais de uma classe, porém é necessário o entendimento da MRO(Method resolution order) pois caso haja dois caminhos para o mesmo método chamado, pode se criar conflitos.
```python

class A:
    ...
    def quem_sou(self):
        print('A')
class B(A):
    ...
class C(A):
    ...
    def quem_sou(self):
        print('C')
class D(B,C):
    ...
d = D()
d.quem_sou()
```
Saída:
```python
C
```
Pelo MRO, como a chamada está em D, a ordem será dos argumentos dados na classe, sendo primeiro B e depois C, após isso de quem herdaram, o A.  
Caso não haja a função em B, ele irá procurar em C

## Mixins

Mixin é uma classe complementar, feita para herdar e adicionar comportamentos extras para poder ser reutilizado.

Classes complementares não são autônomas, apenas possuem funções para serem adicionadas em outras classes.

## Abstração

Abstração em classes é você manter um método assinatura para serem obrigatórios a criação para classes subsequêntes:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
```
Toda classe que herdar de animal precisará ter emitir_som  

Como demonstrado, para criação de classes abstratas é necessário importar e sua classe precisará herdar de ABC
Após isso é necessário usar @abstractmethod em cima do método que será uma assinatura
