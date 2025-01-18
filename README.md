
# 📚 Resumo de aulas do curso Python 3 de Otavio Luiz na Udemy.

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
