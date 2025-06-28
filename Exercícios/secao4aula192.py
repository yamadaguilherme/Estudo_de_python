tarefas = list()
descarte = list()

def verifica(task):
    if task == 'listar':
        listar()
    elif task == 'desfazer':
        desfazer()
    elif task == 'refazer':
        refazer()
    elif task == 'sair':
        print('Fechando programa')
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

while True:
    print('Comandos: listar, desfazer, refazer ou sair')
    comando = str(input('Digite uma tarefa ou comando:' ))
    verifica(comando.lower())
    print('')