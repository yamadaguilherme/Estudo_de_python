import copy

from secao4aula160v2_entry import produtos, imprime

imprime(produtos, 'produtos')

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

imprime(novos_produtos, 'novos_produtos')

produtos_ordenados_por_nome = sorted(novos_produtos, key = lambda p: p['nome'], reverse = True)

imprime(produtos_ordenados_por_nome, 'produtos_ordenados_por_nome')

produtos_ordandos_por_preco = sorted(novos_produtos,key= lambda p: p['preco'], reverse=False)

imprime(produtos_ordandos_por_preco, 'produtos_ordandos_por_preco')