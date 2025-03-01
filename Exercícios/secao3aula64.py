nome = 'Guilherme Yamada'
tamanho_nome = 2*len(nome)
escada = ''
contador = 0
while len(escada) != tamanho_nome:
    escada += f'{nome[contador]} '
    contador += 1
    print(escada)