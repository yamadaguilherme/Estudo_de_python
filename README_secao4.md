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


parei na aula 118
