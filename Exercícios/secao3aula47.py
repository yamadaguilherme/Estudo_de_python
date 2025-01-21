nome = input('qual seu nome? ')
idd = int(input('qual sua idd? '))
n = True
print(type(nome))
print(type(idd))
if nome and idd:
    print(f'Seu nome é {nome}')
    print(f'Seu nome de tras pra frente é {nome[::-1]}')
    if  " " in nome:
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')
    print(f'Seu nome tem {len(nome)} caracteres')
    print(f'A última letra do seu nome é {nome[(len(nome))-1:]}')
else:
    print('Desculpa, nada foi digitado')
