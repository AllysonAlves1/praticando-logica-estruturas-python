# Quantos números são divisíveis por 3 e a 4 ao mesmo tempo
num = 0
for _ in range(4):
    numero = int(input("Digite um número: "))
    if (numero%3==0) and (numero%4==0):
        num = num + 1
print(num)