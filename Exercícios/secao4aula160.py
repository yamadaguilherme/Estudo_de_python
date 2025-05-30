import copy

def print_lista(lista, nome):
    print(f'Lista dos {nome}')
    for l in range(len(lista)):
        print(lista[l])

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print_lista(produtos, 'produtos')

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

print_lista(novos_produtos, 'novos produtos')

produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda p: p['nome'], reverse=True)

print_lista(produtos_ordenados_por_nome, 'produtos ordenados por nome')

produtos_ordandos_por_preco = sorted(novos_produtos,key= lambda p: p['preco'], reverse=False)
print_lista(produtos_ordandos_por_preco, 'produtos ordandos por preco')

