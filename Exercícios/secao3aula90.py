import os
lista = []

while True:
    opcao = str(input('Selecione uma opção\n'
    '[i]nserir [a]pagar [l]istar: '))
    
    if opcao == 'i':
        os.system('cls')
        adicionar = str(input('O que você quer adicionar? '))
        lista.append(adicionar)
    elif opcao == 'a':
        os.system('cls')
        remover = int(input('Digite o índice que quer apagar: '))
        lista.pop(remover)
    elif opcao == 'l':
        os.system('cls')
        for  indice, item in enumerate(lista):
            print(indice, item)
    else:
        continue