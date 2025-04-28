def entrada():
    print('Digite seus números e use qual quer caractere que não seja um número para finalizar')
    dados = []
    while True:
        try:
            dados.append(int(input('Digite números para sua lista: ')))
        except  ValueError:
            print('Lista encerrada, seu valor repetido na lista é: ')
            break
    
    return dados

def processamento(lista):
    verificador = set()
    for i in lista:
        if i in verificador:
            return i
        verificador.add(i)

def main():
    print(processamento(entrada()))

main()
