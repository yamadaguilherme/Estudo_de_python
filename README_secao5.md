
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
