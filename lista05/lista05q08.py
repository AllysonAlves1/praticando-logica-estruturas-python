# Quantos números entre 100 e 200 foram digitados
num = 0
for _ in range(5):
    numero = int(input("Digite um número: "))
    if numero >= 100 and numero <= 200:
        num = num + 1
print(num)