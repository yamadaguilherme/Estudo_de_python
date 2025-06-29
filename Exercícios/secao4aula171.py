def menor(l1,l2):
    menor_lista = min(len(l1),len(l2))
    return menor_lista

lista_a = [1,2,3,4,5,6,7,8]
lista_b = [1,2,3,4,5,6]

lista_juntas = list(zip(lista_a,lista_b))

lista_final = []

for i in range(len(lista_juntas)):
    lista_somada = lista_a[i] + lista_b[i]
    lista_final.append(lista_somada)
    
print(lista_final)