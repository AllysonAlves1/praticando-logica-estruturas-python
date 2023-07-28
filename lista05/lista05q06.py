# O menor valor de 8 números digitados pelo usuário
num = 9999
for _ in range(8):
    numero = int(input("Digite um número: "))
    if numero < num:
        num = numero
print(num)