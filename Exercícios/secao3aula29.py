nome = input('Qual seu nome?')
peso = float(input('Qual seu peso?'))
altura_metros = float(input('Qual a sua altura?'))
imc =  peso/(altura_metros**2)

print(f'{nome}, tem {peso} kg e {altura_metros} metros.\nSeu imc é {imc:.2f}')