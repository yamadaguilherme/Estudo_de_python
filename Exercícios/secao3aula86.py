lista = []
while True:
    novo_item = input('''Digite algo: 
    Para parar não digite nada. ''')
    if novo_item == '':
        print('Programa encerrado')
        break
    lista.append(novo_item)
    print(lista)
for i in range(len(lista)):
    print(i, lista[i])