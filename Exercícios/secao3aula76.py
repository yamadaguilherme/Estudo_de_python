print('digite uma palavra: ')
palavra = input()

palavra_oculta = '_'*len(palavra)
print(palavra_oculta)

contador = 0

while palavra_oculta != palavra:

    print('digite uma letra: ')
    letra = input()
    
    if len(letra) > 1:
        print('digite apenas uma letra')
        continue

    contador += 1    

    nova_palavra_oculta = ''

    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra_oculta += letra
        else:
            nova_palavra_oculta += palavra_oculta[i]
    
    palavra_oculta = nova_palavra_oculta

    print(palavra_oculta)
print(f'''Parabéns!A palavra era {palavra_oculta}
      'foram utilizadas {contador} tentativas''')