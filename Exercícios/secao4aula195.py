import json

def ler():
    try:
        with open('tarefas.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        with open('tarefas.json', 'w') as f:
            json.dump([], f, indent= 4)
        return []
def salvar():
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f, indent= 4)

def verifica(task):
    if task == 'listar':
        listar()
    elif task == 'desfazer':
        desfazer()
    elif task == 'refazer':
        refazer()
    elif task == 'sair':
        print('Fechando programa')
        salvar()
        exit()
    else:
        tarefas.append(task)

def imprime():
    for tarefa in tarefas:
        print(f'{tarefa}')

def listar():
    if len(tarefas) == 0:
        print('Não há tarefas')
        return
    imprime()

def desfazer():
    if len(tarefas) == 0:
        print('Não há tarefas para desfazer')
        return
    descarte.append(tarefas.pop())
    imprime()

def refazer():
    if len(descarte) == 0:
        print('Não há tarefas para resfazer')
        return
    tarefas.append(descarte.pop())
    imprime()

tarefas = ler()
descarte = list()

while True:
    print('Comandos: listar, desfazer, refazer ou sair')
    comando = str(input('Digite uma tarefa ou comando:' ))
    verifica(comando.lower())
    print('')