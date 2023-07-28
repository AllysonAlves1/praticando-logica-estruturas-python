# A média de 6 números digitados pelo usuário
num = 0
for _ in range(6):
    numero = int(input("Digite um número: "))
    num += numero
    media = num/6
# Em caso de número negativo a função se encerra
    if numero < 0:
        break
print(media)