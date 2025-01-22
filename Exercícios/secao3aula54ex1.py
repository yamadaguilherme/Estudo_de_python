try:
    numb = int(input('digite um número inteiro '))
    if type(numb) is int:
        inteiro = numb%2
        if inteiro == 0:
            print('O número é par ')
        else:
            print('O número é ímpar ')
except: 
    print('O valor digitado não é um número')
