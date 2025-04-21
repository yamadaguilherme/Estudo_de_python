def entrada():
    lista_de_num = []
    print('Digite um número! \nCaso não seja um número o programa irá finalizar')
    while True:
        num = input('Número: ')
        try:
            lista_de_num.append(int(num)) 
        except ValueError:
            return lista_de_num

def multiplica(lista_numb):
    multiplicado = 1
    for i in lista_numb:
        multiplicado *= i
    return multiplicado

def paridade(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'

def main():
    resultado = multiplica(entrada())
    print(f'Seus números multiplicados dão: {resultado} e é {paridade(resultado)}')
    
main()