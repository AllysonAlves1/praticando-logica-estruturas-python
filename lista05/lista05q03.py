# Somando 5 números digitados pelo usuário
num = 0
for _ in range(5):
    numero = int(input("Digite um número: "))
    num += numero
# Em caso de número negativo a função se encerra
    if numero < 0:
        break
print(num)