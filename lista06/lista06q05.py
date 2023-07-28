# Contabilizando a quantidade de números digitados
quant = 0
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    quant += 1
print(f'Quantidade de números digitados: {quant-1}')