from itertools import zip_longest
def decorador_externo(param):
    def decorador(func):
        def wrapper(*args,**kwargs):
            lista_final = []
            for i in range(param):
                resultado = func(*args, **kwargs)
                lista_final.append(resultado)
                print(resultado)
            print(lista_final)
        return wrapper
    return decorador


def comparador(l1,l2):
    return min(len(l1), len(l2))
        
siglas = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']

tamanho = comparador(siglas, cidades)

@decorador_externo(tamanho)
def junta_listas(l1,l2):
    i = junta_listas.contador
    sigla_cidade = [l1[i],l2[i]]
    junta_listas.contador += 1 
    return sigla_cidade

junta_listas.contador = 0

lista_final = junta_listas(siglas, cidades)