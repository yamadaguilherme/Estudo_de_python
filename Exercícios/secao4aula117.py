def entrada():
    valor = input('Qual seu valor que quer utilizar? ')
    if valor.isnumeric() == True:
        funcao = input('Qual função você quer utilizar?\nOpções: [d]uplicar [t]riplicar [q]uadruplicar')
        formatado_func = funcao.lower()
        return int(valor), formatado_func
    else:
        print('Erro! Você não digitou um número')
        return None

def duplica(num):
    double = num * 2
    return double

def triplica(num):
    triple = num * 3
    return triple

def quadriplica(num):
    quadra = num * 4
    return quadra

def main():
    valor, funcao = entrada()
    condicao_d = funcao[0] == 'd'
    condicao_t = funcao[0] == 't'
    condicao_q = funcao[0] == 'q'
    if valor == None:
        print('Programa encerrado')
    elif condicao_d:
        print(f'Seu número duplicado é {duplica(valor)}')
    elif condicao_t:
        print(f'Seu número triplicado é {triplica(valor)}')
    elif condicao_q:
        print(f'Seu número quadriplicado é {quadriplica(valor)}')
    else:
        print('Erro na função digitada')
        
main()