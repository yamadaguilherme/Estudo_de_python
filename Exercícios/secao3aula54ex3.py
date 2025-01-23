name = input('Qual seu nome? ')
size_name = len(name)
if size_name >= 7:
    print('Seu nome é muito grande')
elif size_name >= 5:
    print('Seu nome é normal')
else:
    print('Seu nome é curto')