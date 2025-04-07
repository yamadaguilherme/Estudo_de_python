
# 📚 Resumo de aulas do curso Python 3 de Otavio Luiz na Udemy.

## Lembrete de atalhos!
**Shift+alt+downarrow** = Copia a linha atual para baixo   
**Selecionar linhas + CTRL /** = Torna todas as linhas selecionadas comentários
## Função print()
**print('texto')** → Imprime  
**,** → Separa os itens dentro do print()  
**sep="x"** → Separa os itens dentro do print() com o caractere usado  
**end='x'**  → Não quebra a linha e adiciona o caractere usado  
**end=''\n"** → Quebra linha  
**print(r"")** → Ignora todas as funções dos caracteres dentro do print.  

## Para Comentarios
**#** → Permite adicionar comentários  
**''' texto '''** → Comentários multilinhas/Docstring  

## Tipos de dados
 Python é uma linguagem dinâmica e forte.  
 **type()** - Permite ver o tipo de dado

 - **Strings - Dados em texto**

  Textos utilizados dentro de ' ou "  
 O caractere \ pode ser usado como Escape(Ignora a função do próximo caractere)  
 r pode ser utilizado antes do "" para ignorar caracteres  
 É possível utilizar " ' ' " para aparição do '  
 As strings são indicados por str
 
  - **Int e Float - Dados em números inteiros e flutuante**
 Int → Número inteiro  
 Float → Número de ponto flutuante (Números que possuem casas decimais)
 
  - **Boolean - Dados em True and False**
True → dado retornado como verdadeiro  
False → dado retornado como falso  
As boolean são indicados por bool

## Conversão de tipos
Concatenar str com +  
Declaração de itens - É possível tranformar um tipo em outro, int('1')  
Multiplicações de str com números são funcionais
## Variáveis 
Variáveis são como um item que pode ser alterado durante o programa.

texto_variável = 1+1

---

**print(f'{variavel}texto')** → Lê todos as variavéis dentro de {}

> **Entrada:**
> ```python
> variavel = 1
> print(f'{variavel}texto')
> ```

> **Saída:**
> ```
> 1 texto
> ```

---

**f'{variavel:.2f}'** → Permite controlar o tanto de casas decimais da variavel   


> **Entrada:**
> ```python
> variavel = 1
> print(f'{variavel:.2f}')
> ```

> **Saída:**
> ```
> 1.00
> ```

---

**'texto{}texto2{}'.format(a,b,c)** → Utiliza em ordem declarada(a,b,c) colocando nos lugares das {}

> **Entrada:**
> ```python
> a = 1
> b = 2
> print('texto {} texto2 {}'.format(a,b,c)')
> ```

> **Saída:**
> ```
> texto 1 texto2 2
> ```

## Operadores
* \+ → Mais (Adição)
* \- → Menos (Subtração)
* \* → Multiplicação
* \/ → Divisão
* \// → Divisão Inteira
* ** → Expoente
* % → Resto da Divisão

## Operadores de comparação

== → Igualdade
Verifica se os dois valores são iguais.

!= → Diferença
Verifica se os dois valores são diferentes.

\> → Maior que
Verifica se o valor da esquerda é maior que o da direita.

< → Menor que
Verifica se o valor da esquerda é menor que o da direita.

\>= → Maior ou igual a
Verifica se o valor da esquerda é maior ou igual ao da direita.

<= → Menor ou igual a
Verifica se o valor da esquerda é menor ou igual ao da direita.

is → Identidade
Verifica se duas variáveis referenciam o mesmo objeto na memória.

is not → Negação da identidade
Verifica se duas variáveis não referenciam o mesmo objeto na memória.

## Operadores lógicos
and → E lógico
Retorna True se ambas as condições forem verdadeiras.

or → OU lógico
Retorna True se pelo menos uma das condições for verdadeira.

not → Negação lógica
Inverte o valor lógico de uma expressão. Retorna True se a condição for falsa, e False se for verdadeira.

![Imagem de lógica](https://siit.co/blog/file_storage/posts/June2021/sRiXCb1tWOHWn4dPBAVu.png)
[imagem retirada do site 'siit.co', em 18/01/2025]

## Input()
É possível coletar dados que venham do usuário, utilizando input()  
Outras possibilidades é de se armazenar em uma variável o input():  
variavel = input()

Também pode se colocar uma pergunta durante o input():  
input('texto de pergunta' )

Os tipos podem serem definidos antes do input() ser lido:
int(input()) → Leitura de input() inteiros

## if, else, elif

Para lógica de programação, são utilizados if, else, elif:


> **Entrada:**
> ```python
> fst_number = int(input('número inteiro: '))
> scnd_number = int(input('número inteiro: '))
> if fst_number > scnd_number:
>   print(f'{fst_number} é maior')
> elif scnd_number > fst_number:
>   print(f'{scnd_number} é maior')
> else: 
>   print('são iguais')
> ```

O programa pede dois números e verifica quais dos dois é maior ou se são iguais.

Atenção: É necessário a identação dentro dos blocos if, else, elif!

## Interpolação básica de strings
s → string
d e i → int
f → float
x e X → hexadecimal (ABCDEF0123456789)

> **Entrada:**
> ```python
> nome = Gui
> altura = 1.70
> print('O %s tem %.2f de altura' % (nome, altura))
> ```

> **Saída:**
> ```
> O Gui tem 1.70 de altura
> ```

## F strings
Formatação para Pads  
:(Caractere)(<^>)(Quantia) → Cria a quantia de caracteres do(s) lado(s) utilizados  
\< → Coloca x caracteres a esquerda do texto  
\^ → Coloca x caracteres com o texto centralizado  
\> → Coloca x caracteres com o texto centralizado  

> **Entrada:**
> ```python
> variavel = 'ABC'
> print(f'{variavel:$>10}')
> ```

> **Saída:**
> ```
> ABC$$$$$$$
> ```

+ → Força a aparecer o sinal do número
- → Força a aparecer o sinal do número CASO seja negativo
= → Força o número antes do caractere a aparecer depois do sinal
, → Força a aparecer , nas casas de milhar

> **Entrada:**
> ```python
> variavel = '1000.482837283'
> print(f'{variavel:0=+10,.1f}')
> ```

> **Saída:**
> ```
> +001,000.5
> ```

---

Conversion Flags
!r → __repr__()
!s → __str__()

## Fatiamento de strings
Correspondente de cada caractere na frase "Olá Mundo":   

 012345678   
 Olá Mundo   
-987654321   

O índice [2] → á   
O índice [-2] → d

Fatiamento [i:f:p]
i → início
f → fim
p → passos(de quantas em quantas casas é "pulado" um caractere)

> **Entrada:**
> ```python
> variavel = 'Olá mundo'
> print(variavel[1:7:2])
> ```

> **Saída:**
> ```
> l u
> ```

## Introdução ao try/except

Para resolver erros que NÃO envolvem sintaxe:   
try → tentar executar o código  
except → pular caso haja um erro no try  
São utilizados os dois juntos  


## Identidade
Toda variável é marcada com uma id para representa-la.  
É possível ver a id usando id(objeto())

## Is, is not
É literal é ou não é, pode ser utilizado em lógicas para rodar certas condições

## Built in types
Série de ações pré definidas para tipos como str, int, float, bool.
Disponível em: https://docs.python.org/3/library/stdtypes.html

## Repetições
while condicao:
Enquanto a condição imposta for verdade, o código dentro do while será repetido até que seja alterado o valor verdade.
break dentro do while quebra a repetição

## Operadores de atribuição

+= → Soma a própria variavel com o valor indicado(pode ser int/float/str)
-= → Subtrai a própria variavel com o valor indicado(pode ser int/float/str)
*= → Multiplica a própria variavel com o valor indicado(pode ser int/float/str)
/= → Divide a própria variavel com o valor indicado(pode ser int/float/str)
//= → Divide arredondando a própria variavel com o valor indicado(pode ser int/float/str?)
**= → Exponencia arredondando a própria variavel com o valor indicado(pode ser int/float/str?)
%= → Resto da divisão a própria variavel com o valor indicado(pode ser int/float/str?)

## Break/Continue no while

O Break para o while e continua a leitura pós o mesmo

Pode ser utilizado continue para voltar ao início do while sem que ele termine de executar todo o while

## While dentro de while

Fazer laços dentro de laços, analogamente a um relógio com mínutos e horas

##  Else com o While

É possível utilizar o else: após um while
Vatagem: se possuir um break dentro do while e um else após o while, e o break for executado, o else é ignorado.

## For / In

Outro tipo de repetição

## Range

Função que mostra a "Range"
Range(start,stop,step)
Começo, quando parar e de quanto em quanto corre o Range

## Itererável, Iterador (Como funciona o For)

iter() Te retorna o Iter do objeto utilizado, onde foi alocado na memória

next() Chama o próximo valor de Iter

> **Entrada:**
> ```python
> texto = 'Gui' #iterável
> iterador = iter(texto) #iterador
>
> while True:
>   try:
>       letra = next(iterador)
>       print(letra)
>   except StopIteration: #StopIteration é o erro ao acabar o next
>       break
> ```

## Continue, break, else

As mesmas funções possíveis dentro do while, podem ser utilizadas no for

## List

[] cria uma lista
Lista são mutáveis, diferente de str
Suportam diferenets valores dentro dela ao mesmo tempo
Ex:

> **Entrada:**
> ```python
> lista = [123, 'ola', True]
> print(lista[0], type(lista[0]))
> ```

> **Saída:**
> ```
> 123 <class 'int'>
> ```

## Create, read, update, delete (CRUD)

Criar lista []
ler list[]
update list[indice] = item atualizado
del list[indice]

Evitar deletar pois em lista grande consome muita memória

lista.append(item) = adiciona o item ao um novo último valor na lista

lista.pop() = remove o último item da lista
lista.pop(indice) = remove o indice indicado
.pop também retorna o item removido
lista.clear() = limpa a lista
lista.insert(indice, item) = adiciona o item no indice desejado, sem excluir ou reescrever nada

lista_a.extend(lista_b) #extende a lista_a, copiando os itens da lista b, e salva na variavel lista_a
lista_c = lista_a + lista_b #concatena a lista_a e lista_b na lista_c

## Dados mutáveis

Funcionam como ponteiros

> **Entrada:**
> ```python
> lista_a = [123, 'ola', True]
> lista_b = lista_a
> lista_a.append('oi')
> print(lista_b)
> ```

> **Saída:**
> ```
> [123, 'ola', True, 'oi']
> ```

lista_b = lista_a.copy()
faz uma copia da lista_a e volta a funcionar como variáveis

Parei na aula 86
