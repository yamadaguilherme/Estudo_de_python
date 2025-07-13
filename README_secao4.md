# 📚 Resumo de aulas da seção 4 do curso

## Parâmetro/Argumentos

def função(a,b,c):

Você pode pedir um argumento em funções para que ela aplique o objetivo dela
a,b,c são os parâmetros

Caso seja inputado os valores 1,2,3 para os parâmetros a,b,c eles serão chamados de
argumentos

função(1,c=3,b=2)

Pode se chamar os argumentos mostrando o parâmetro referente a eles

## NoneType

def função(a,b,c=None):

É possível atribuir valores None, onde caso seja inputado um valor de C, o C será considerado o valor inputado, e em condições que não seja inputado nada, ele se comportará como None

## Global

Os valores de variáveis dentro de uma função apenas servem para dentro dela
Para quebrar isso, pode-se definir valores fora da função OU utilizar o global

def func():
    global x
    x = 10

o x será possivel utilizar mesmo fora da função

## *args 

def função(*args):

Empacotamento:
Para o tanto de argumentos que você queira guardar e não modificar em uma tupla
Caso queira modificar, pode retransformar a tupla em uma lista

para desempacotar pode utilizar o *noma_da_variavel

##  dict

dict é um type
é um dicionário contendo vários valores com suas nomenclaturas

animais = {
    'nome': 'levi',
    'peso': '5kg',
    'idade': '6 anos',

}

## Chaves

animais = {}

chave = 'nome' 

animais[chave] = 'levi'
animais['peso'] = '5kg'

CRUD funciona para chaves 

modelo de if e else utilizando dict

if animais.get('idade') is None:
    print('não existe')
else:
    print(animais['idade'])

   
## Métodos em dict

len(dicionario) - retorna quantas chaves há no dicionário

dicionario.keys() - retorna os nomes das chaves 
é possível fazer com for também
for chaves in dicionario:

dicionario.values() - retorna os valores das chaves

dicionario.items() - retorna tanto as chaves como os valores

dicionario.setdefault('chave', 'valor') - seta um valor para uma chave se não existir

dicionario = {
    'chave1' = valor1,
    'chave2' = valor2,
}

dicio = dicionario.copy() - copia RASA do dicionario (shallowcopy)

caso queira fazer uma deepcopy:

import copy
dicionario2 = copy.deepcopy(dicionario1)

dicionario.get('chave1', 'mensagem caso não exista')

get pede a chave do dicionário mas não acontece erro caso não exista
parecido com o try mas para dicionários 

dicionario.pop('chave1') - retorna a chave1 mas apaga ela do dicionário

dicionario.popitem() - retorna o último item do dicionário mas apaga ele

dicionario.update({
    'chave1' : 'item1'
    'chave2' : 'item2'

})

ou

dicionario.update(chave1 = 'item1', chave2 = 'item2')

update atualiza alguma chave e pode adicionar novas chaves

dicionario.update(lista)
ou
dicionario.update(tupla)

são funcionais

## Set 

s1 = set()  - cria um set vazio

s1 = set{1,2,3} - set com Dados

set discarta todos os valores repetidos
é possível a transformação de lista ou tupla em sets e a volta deles também
método efetivo para tirar valores iguais

porém os sets NÃO GARANTEM ordem 
Não aceitam valores mútaveis
Não tem índices
Funcionam analogamente como sacolas

MÉTODOS ÚTEIS

s1.add('valor') - adiciona o valor no set

s1.update() - pode adicionar vários valores de uma vez

s1.clear() - limpa o set

s1.discard('valor') - descarta o valor dentro do set

OPERADORES ÚTEIS

| - união

& - intersecção

*-*  - 'a - b' = resulta nos itens únicos do grupo da esquerda

^ - diferença simétrica(itens que não estão em ambos)


## Função lambda

UTF-8 é a ordem de caracteres usada pelo python

Exemplo:

Lista com nomes e sobrenomes

> ```python
> def ordena(item):
>   return item['nome']
> 
>lista.sort(key=ordena)
>
> for item in lista:
>    print(item)
> ```

De maneira mais simples:

> ```python
> lista.sort(key=lambda item: item['nome'])
>
> for item in lista:
>    print(item)
> ```

lambda não precisa ser definida antes

lambda x, y: x+y
estaria definindo uma função de soma

lambda é usado para coisas simples para encurtar

## Empacotamento e Desempacotamento

Empacotamento(packing)

*args = argumentos posicionais extras (recebidos como uma tupla).

**kwargs = argumentos nomeados extras (recebidos como um dicionário).

> ```python
> def exemplo(*args, **kwargs):
>    print(args)    # tupla
>    print(kwargs)  # dicionário
>
>
> exemplo(1, 2, 3, nome="João", idade=25)
> # args = (1, 2, 3)
> # kwargs = {"nome": "João", "idade": 25}
> ```

Desempacotamento(unpacking)

É quando usamos * ou ** para espalhar os valores de uma tupla ou dicionário ao chamar a função.

> ```python
> valores = (10, 20)
> dados = {"nome": "Ana", "idade": 22}
>
> def mostrar(a, b, nome, idade):
>    print(a, b, nome, idade)
>
> mostrar(*valores, **dados)
> ```

## List Comprehension

lista = []
for num in range(10):
    lista.append(numero)
print(lista)

mas para um jeito mais fácil utilizando list Comprehension:

lista = [num for num in range(10)]
print(list)

## Mapeamento

Para o mapeamento é possível utilizar a função .map()
Porém para organização e leitura é melhor ser utilizado manualmente

> ```python
> produtos = [
>    {'nome': 'p1', 'preco': 20},
>    {'nome': 'p2', 'preco': 10},
>    {'nome': 'p3', 'preco': 30},
> ]
>
> novos_produtos = [
>    {**produto, 'preco': produto['preco'] * 1.05}
>    if produto['preco'] > 20 else {**produto}
>    for produto in produtos
> ]
>
> for produto in novos_produtos:
>    print(produto)
> ```

O código acima mapeia os produtos e faz o preço aumentar em 5% caso o preco seja maior que 20

Mapeamento é você criar uma "base" onde pode mudar os valores seguindo a sequência
Vem antes do for 


## Filtro de dados em list comprehension

Vem depois do for 
Decide quais valores serão incluidos da lista original

> ```python
> produtos = [
>    {'nome': 'p1', 'preco': 20},
>    {'nome': 'p2', 'preco': 10},
>    {'nome': 'p3', 'preco': 30},
> ]
>
> novos_produtos = [
>    produto for produto in produtos if produto['preco'] >= 20
> ]
>
> for produto in novos_produtos:
>    print(produto)
> ```

## List comprehension com dois for

É possível fazer com dois for

> ```python
> lista = [
>    (x,y)
>    for x in range(3)
>    for y in range(3)
> ]
>
> ```

Ou também com um for na parte ternária


> ```python
> lista = [
>    [x for y in range(3)]
>    for y in range(3)
> ]
>
> ```

OBS: os dois geram resultados DIFERENTES

## Dictionary comprehension e set comprehension

Dictionary: 

> ```python
> produto = {
>     'nome': 'Caneta Azul',
>     'preco': 2.5,
>     'categoria': 'Escritório',
> }
> 
> dc = {
>     chave: valor.upper()
>     if isinstance(valor, str) else valor
>     for chave, valor
>     in produto.items()
> }
> 
> print(dc)
> ```

Todo compreendimento de list comprehension pode serem usadas para dict e set

## isinstance()

Verifica se seu item é de tal classe
if isinstance(item, classe):

faz uma ação caso seu item seja da classe desejada

## isinstance()

Verifica se seu item é de tal classe
if isinstance(item, classe):

faz uma ação caso seu item seja da classe desejada


## Truthy and falsy

Valores podem assumir Truth ou false, mas também podem serem Truthy ou falsy
Exemplos de falsy:

false
0
''
[]
None
{}
()
0.0

Também existem funções para verificar se é falsy ou Truthy
falsy(item)
truthy(item)

Seriam como grupos de valores que assumem falsy

## dir, hasattr e getattr

São verificadores de atributos.
Conseguem ver se alguma função é permitida no objeto dado

dir(objeto) - verifica quais são todas funções permitidas

hasattr(objeto, função) - verifica se no objeto é permitida a função desejada

getattr(objeto, função()) - executa a função mesmo se ela estiver salva em outra variável



## Generator expression, iterables and iterators

Iterable: você pode acessar índices

Iterators: você só pode acesar sequencias

Generator expression é uma função gera uma sequencia um de cada vez, ocupando menos memória

> ```python
> generator(n for n in range(10000))
> for i in generator:
>   print(i)
> ```
> ```
> A saída será print sequencial de 0 até 9999
> ```

Todo generator é um iterator, i.e. pode se chamar as funções aplicaveis em iterators.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*iBgdO1ukASeyaLtSv3Jpnw.png" alt="Imagem de lógica">
</p>

<p align="center">
  <em>[imagem retirada do site 'miro.medium', em 10/05/2025]</em>
</p>


## Generator function

Generator function são funções que podem serem pausadas

Exemplo:

> ```python
>  def fibonacci_sequence():
>        a, b = 0, 1
>        while True:
>            yield a
>            a, b = b, a + b
> fib_gen = fibonacci_sequence()
>    for _ in range(10):
>        print(next(fib_gen)) 
> ```


yield faz a pausa da função e retorna o valor, quando chamado novamente, a função continua de onde pausou

## Yield from

É possível conectar duas funções geradoras diferentes unindo elas com yield from

    def generator_1():
        yield 1
        yield 2
        yield 3

    def generator_2():
        yield from generator_1()
        yield 4
        yield 5

    for value in generator_2():
        print(value)

    Saída:
    1
    2
    3
    4
    5
    
## Try, else, except and finally

Try e except já foram mencionadas

o except por consequência da The zen of python
deve sempre ser especificado o erro:

except TypeError:

except Except: maior classe de erro possível, quando cair em qual quer erro não definido, cairá nesse except

é possível utilizar vários except's

Try com finally
O finally é executado independente de o try ter conseguido completar todas as ações

Else pode ser utilizado mas acaba por ser redundante nas maioria das vezes

## Raise 

raise erro 
força que um erro aconteça

É útil para tratamento de erros esperados

## Módulos, import, from, as e *

O site: https://docs.python.org/3/py-modindex.html
possuí todos os módulos incluidos no python

Maneiras de importar módulos

import módulo:
importa todo o módulo

name space:
é o módulo.ação

vantagens de importar modulo inteiro:
o name space é bem definido no programa

desvantagens:
nomes grandes

from módulo import ação1, ação2:
importa apenas ações do módulo

pode se utilizar o as para mudar o nome do módulo ou ação
exemplo:
from sys import exit as sair

## Modularização

É possivel acessar pelo seu código outra pasta com outro código
Chamado de módulo

import sys
import modulo_outra_pasta

o programa vai importar a outra pasta chamada modulo_outra_pasta e executar

Caso o modulo esteja em outro caminho/diretório
é possivel usar 
sys.path.append('Nome/do/caminho')


## Recarregamento de módulo, importlib e singleton

o import módulo é um singleton, i.e. só pode ter uma instância por execução do programa

consequência: o módulo sempre que for chamado será a mesma instância, caso esteja dentro de um for ou while, só será feita uma execução, pois sua instância não mudará

para contornar isso, podemos utilizar a importlib

import importlib 

e dentro do for utilizar:
importlib.reload(módulo)

oque vai fazer a reutilização do módulo

## Packages

é possível colocar módulos dentro de pastas(packages)

exemplo de package:
package/modulo

import package.modulo

porém quando você for utilizar alguma função dentro do módulo
pode acabar por ser muito longa

exemplo:
print(package.modulo.soma_do_módulo)

para contornar isso, pode se usar:

from package import módulo

print(modulo.soma_do_módulo)



As execuções importam pois definem o pov, caso executar um arquivo que não esteja no mesmo diretório haverá necessidade de importação.
Analogamente ao file explorer, só podendo acessar as pastas contidas dentro do repositório, sem a possibilidade de retorno para diretório anteriores.

## Variáveis livres + nonlocal

Variáveis livres são variáveis que são referenciadas em uma função (ou bloco de código), mas não são definidas dentro desse escopo. Em vez disso, elas vêm de um escopo mais externo.

Pode se utilizar nonlocal x para acessar e poder alterar valores de outros escopos

*lembrete: funções closure:

```python
def contador(x):
    valor = x  # variável definida no escopo externo
    def soma(y):
        nonlocal valor
        valor += y
        return valor
    return soma

c = contador(1)
print(c(5))
print(c(1))
print(c(-2))
```

## Funções decoradoras em geral(decorators)

Funções que adicionam funcionalidades a outras funções ou métodos sem modificá-las diretamente. Elas "embrulham" a função original, permitindo executar código antes ou depois dela, e retornam uma nova função com o comportamento modificado.

utilizam um formato de closure + a modificação desejada

```python
def criar_funcao(funcao):
    def interna():
        modificacao
        return resultado
    return interna
```

ele utiliza a funcao e altera uma nova modificacao

## Syntax Sugar 

Syntactic sugar (ou açúcar sintático) em Python é uma forma mais simples, elegante e legível de escrever código

property

Uma das formas é nas funções
caso você for utilizar uma função que cria outra função, pode chamar ela simplesmente usando @

O decorador @property permite que você acesse o resultado de um método como se fosse um atributo, sem precisar colocar parênteses ().

## Função decoradora com parâmetro

Um decorador com parâmetros é um decorador que recebe argumentos além da função a ser decorada.

A função externa: recebe os parâmetros do decorador.

A função do decorador em si: recebe a função a ser decorada.

A função wrapper: modifica o comportamento da função original.



## Ordem de aplicação dos decoradores

A ordem vem de baixo para cima


@decorador(3)
@decorador(2)
@decorador(1)

decorador(1) será executado antes

## Função zip e zip_longest

zip
a função junta duas listas com os indicadores iguais, usando o tamanho como o MENOR comprimento entre as duas listas

```python
siglas = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']

print(list(zip(siglas,cidades)))
```

```python
saida:
[['BA', 'Salvador'], ['SP', 'Ubatuba'], ['MG', 'Belo Horizonte']]
```

zip_longest
a função junta duas listas com os indicadores iguais, usando o tamanho como o MAIOR comprimento entre as duas listas

é necessário importar

```python
from itertools import zip_longest

siglas = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']

print(list(zip_longest(siglas,cidades)))
```
```python
saida:
[['BA', 'Salvador'], ['SP', 'Ubatuba'], ['MG', 'Belo Horizonte'], ['RJ', None]]
```
é possivel completar os valores que vão estar como None passando um terceiro parâmetro:

```python
print(list(zip_longest(siglas,cidades,fillvalue = 'x')))

saida:
[('BA', 'Salvador'), ('SP', 'Ubatuba'), ('MG', 'Belo Horizonte'), ('RJ', 'x')]
```
## count

from itertools import count

count() é uma função de contagem infinita
parâmetros: 
count(start, step)

## Combinations, permutations e product

Organizam em inter as possivei combinações

combinations nao repete as combinações, a ordem não importa
exemplo: 
caso apareça x e y, então, y e x não aparecerão

```python
from intertools import combinations, permutations, product

print(*list(combinations(lista, numcombinado)))
```

permutations repete as combinações, a ordem importa
exemplo: 
caso apareça x e y, então, y e x  aparecerão

print(*list(permutations(lista, numcombinado)))

product

faz o produto entre as possiveis combinações
exemplo:

```python
camisa = [
    ['azul', 'branca', 'preta' , 'beje']
    ['feminino', 'masculino']
]


print(product(*camisa))
```

irá fazer todas combinações possiveis entre as cores e o gênero

## Group by

from intertools import groupby

groupby cria grupos quando indicado a lista e a chave

é necessário que a chave esteja ordenada, caso não esteja, a função não irá funcionar corretamente
```python
grupos = groupby(lista, key= chave)

for chave, grupo in grupos:
    print(chave)
    for item in grupo:
    print(item)
```
## Map

Útil para alterar vários itens em um interador
Lembrete: map retorna um interator
É a função já feita como se fosse rodar o for para substituir cada elemento

exemplo:
```python
nomes = ['ana', 'joão', 'maria']
nomes_maiusculos = list(map(str.upper, nomes))
print(nomes_maiusculos)  # ['ANA', 'JOÃO', 'MARIA']
```
como foi alterado para lista, o 'interador' foi consumido, mas a lista pode ser reutilizada

## partial


partial faz uma copia de uma funcao com alguma das variaveis substituida por um valor fixo
vantagens: ela é só uma cópia, então você ainda pode usar sua função original
```python
from functools import partial

def multiplicar(a, b):
    return a * b

dobro = partial(multiplicar, 2)

print(dobro(10))  # 20
print(dobro(5))   # 10
```
## generatortype
```python
from types import GeneratorType

isinstance(objeto, GeneratorType)
```
retorna true ou false verificando se é um generator

## filter

a função pede
filter(função, lista, acumulador)

exemplo:
```python
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 20.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    p for p in produtos
    if p['preco'] > 10
 ]

novo_produtos = filter(
    lambda p: p['preco'] > 10,
    produtos,
    0
)
```
note que novos_produtos e novo_produto fazem a mesma coisa

o retorno do filter sempre será igual ou menor a lista dada

## funções recursivas

são funções que generalizam etapas e utilizam de si mesmo para resolver um problema

```python
def fibonacci(n, x= 0, y= 1):
    if n == 0:
        return x
    x = x+y
    n -= 1
    return fibonacci(n, y, x)

print(fibonacci(5))
```

## Limite de recursão

Existem limites de execução, a pilha do python é definida por padrão
caso execute um programa que passe desse limite, ele irá dar um erro
para contornar erros de recursão por excesso é possível fazer o seguinte:
```python
import sys

sys.setrecursionlimit(valordesejado)
```
## Ambientes virtuais(venv)

Ambientes virtuais são utilizados para facilitar manutenção e organização de programas
Salva-se todas versões das extensões e ferramentas utilizadas, para possível utilização futura.

## Criando um venv

para executar no powershell

```powershell
python -m venv venv
```

## Ativando e desativando o venv
```powershell
.\venv\Scripts\activate
```
selecionar a pasta venv, scrits e depois ativar
para desativar só é necessário digitar
```powershell
deactivate
```
as pastas podem ser diferentes de acordo com o nome dado ao ambiente virtual

## pip

Instalando pacotes e bibliotecas que não estão originalmente com o python

```powershell
pip install pacote
```

para desinstalar:
```powershell
pip unistall pacote
```

para ver quais estão instalados no ambiente:

```powershell
pip freeze
```

para ver versões dos pacotes:

```powershell
pip index versions pacote
```
para atualizar:

```powershell
pip install pacote --upgrade
```

para instalar versões específicas:

```powershell
pip pacote==versão
```
## Requirements.txt

Ao invez de colocar todo o arquivo das instalações, o mais comum é utilizar o requirements.txt, um arquivo contendo as versões necessárias 
Para gerar requirements.txt:

```powershell
pip freeze > requirements.txt
```

Para instalar arquivos do requirements.txt:

```powershell
pip install -r ./requirements.txt
```

## Criando arquivos com python

Pode criar-se arquivos atráves do python, para isso é necessário indicar qual tipo de arquivo vai ser criado:

| Modo     | Nome                   | O que faz                                                       |
|----------|------------------------|-----------------------------------------------------------------|
| `[r]`    | **read**               | Abre para **leitura** (erro se o arquivo não existir)           |
| `[w]`    | **write**              | Abre para **escrita** (cria ou **sobrescreve** o arquivo)       |
| `[x]`    | **exclusive creation** | Tenta **criar** o arquivo — erro se **já existir**              |
| `[a]`    | **append**             | Abre para **adicionar conteúdo ao final** (cria se não existir) |
| `[b]`    | **binary**             | Abre em modo **binário** (ex: imagens, áudio, PDF)              |
| `[t]`    | **text**               | Abre em modo **texto** (padrão)                                 |
| `[+]`    | **update**             | Abre para **leitura e escrita** no mesmo arquivo                |

```powershell
arquivo = open('arquivo.txt', 'modo')

arquivo.close()
```
**Lembrete:** SEMPRE FECHAR UM ARQUIVO APÓS ABRIR

Um método mais fácil de abrir e fechar arquivo:

```powershell
with open('arquivo.txt', 'modo', enconding='utf8') as arquivo:
```

Para mover o "cursor" para o ínicio:
```powershell
arquivo.seek(0,0)
```

Para escrever mais de uma linha ou com iterável:
```powershell
arquivo.writelines()
```

**Lembrete:** O cursor importa no read!

Para ler um arquivo:
```powershell
print(arquivo.read())
```

Para ler linha(funciona como next):
```powershell
print(arquivo.readline())
```

Para ler várias linhas():
```powershell
for linha in arquivo.readlines():
    print(linha.strip())
```

Para deletar um arquivo():
```powershell
os.remove(caminho_arquivo)
```

Para renomear ou mover um arquivo():
```powershell
os.rename(caminho_arquivo,'nome_arquivo')
```
## Criando um arquivo json
```python
import json

dados = {
    "nome": "Ana",
    "idade": 25,
    "cursos": ["Python", "SQL"]
}

with open('dados.json', 'w') as f:
    json.dump(dados, f, indent=4)
```

O arquivo é convertido para json, acontece algumas alterações durante a conversão

## Guard Clause

Para maior legibilidade do código, é possível utilizar o return dentro do primeiro if, caso não seja uma condicional extensa

```python
def listar():
    if len(tarefas) == 0:
        print('Não há tarefas')
        return
    imprime()
```

Em casos como o acima é útil para legibilidade
Para execuções mais limpas lembrar que é possível usar o if not

## Positional only parameters /

Tudo que vier antes da barra nos parametros, deverá ser posicional
```python
def function(a,b, /, c, d):
    ...
function(1,2,d=4,c=3)
```
A chamada a cima será possível pois o c e o d estão após a barra

## Keyword only arguments *

Tudo que vier após a barra nos parametros, deverá ser apenas argumentos nomeados
```python
def function(a,b, *, c, d):
    ...
function(1,2,d=4,c=3)
```
É possível a junção de ambas:

```python
def function(a,b, /,*, c, d):
    ...
function(1,2,d=4,c=3)
```
onde todos argumentos antes da barra são posicionais e todos após * são nomeados.

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
