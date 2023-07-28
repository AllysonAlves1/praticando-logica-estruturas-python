# Selection sort
# def selection_sort(lista):
#     for i in range(len(lista)):
#         # Encontra o elemento mínimo da lista restante
#         min_index = i
#         for j in range(i+1, len(lista)):
#             if lista[j] < lista[min_index]:
#                 min_index = j
#         # Coloca o elemento mínimo encontrado na posição correta
#         lista[i], lista[min_index] = lista[min_index], lista[i]

# # Testa o algoritmo
# lista = [3, 2, 5, 1, 4]
# selection_sort(lista)
# print(lista)

# Mais simplificado
def selection_sort(lista):
    for i in range(len(lista)):
        # Encontra o elemento mínimo da lista restante usando a função min()
        min_index = lista.index(min(lista[i:]))
        # Coloca o elemento mínimo encontrado na posição correta
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Testa o algoritmo
lista = [3, 2, 5, 1, 4, 209, 28, 92, 62]
selection_sort(lista)
print(lista)

# Bubble Sort 

# def bubble_sort(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(n-1):
#             if lista[j] > lista[j+1]:
#                 # Troca os elementos de lugar
#                 lista[j], lista[j+1] = lista[j+1], lista[j]

# # Testa o algoritmo
# lista = [3, 2, 5, 1, 4]
# bubble_sort(lista)
# print(lista)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                # Troca os elementos de lugar
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            # A lista está ordenada, então para o loop
            break

# Testa o algoritmo
lista = [3, 2, 5, 1, 4, 10, 12, 7]
bubble_sort(lista)
print(lista)



