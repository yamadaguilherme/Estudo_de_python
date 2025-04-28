def questoes():
    perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
    return perguntas

def main():
    exercicios = questoes()
    letras = ['a', 'b', 'c', 'd']
    for i in range(3):
        print(exercicios[i]['Pergunta'])
        for k in range(4):
            print(f"{letras[k]}) {exercicios[i]['Opções'][k]}")
        resposta = input('Digite a letra da opção: ').lower()

        if resposta in letras:
            indice = letras.index(resposta)
            if exercicios[i]['Opções'][indice] == exercicios[i]['Resposta']:
                print('Resposta correta!')
            else:
                print('Resposta errada')
        else:
            print('Você digitou uma opção inválida')
        
main()
