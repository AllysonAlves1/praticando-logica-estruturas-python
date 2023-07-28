# Lista dos números
nums = [1, 33, 70, 16, 21 , 2]
listaPar = []
listaImpar = []
# Condicional que pecorre a lista e caso o número seja par ele imprime a mensagem
for num in nums:
    if num%2 == 0:
        listaPar.append(num)
    if num%2 == 1:
        listaImpar.append(num)
print(f'A lista com os números pares {listaPar}\nA lista com os números ímpares {listaImpar}')