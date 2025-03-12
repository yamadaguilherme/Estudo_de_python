while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operator = input('Digite um operador(+-/*): ')

    
    num_valid = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float =float(num_1)
        num_2_float =float(num_2)
        num_valid = True
    
    except:
        num_valid = None
    
    if num_valid is None:
        print('Erro de digitação.')
        continue

    operator_allowed = '+-/*'
    
    if operator not in operator_allowed:
        print('Erro de digitação')
        continue

    if len(operator)>1:
        print('Digite apenas um operador')
        continue

    print('Realizando conta: ')
    result = 0
    if operator == '+':
        result = num_1_float + num_2_float

    elif operator == '-':
        result = num_1_float - num_2_float

    elif operator == '/':
        result = num_1_float / num_2_float

    elif operator == '*':
        result = num_1_float * num_2_float

    print(f'Seu resultado é {result}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break