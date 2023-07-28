# A média dos valores digitados, até um valor negativo for digitado
soma = 0
quant = 0
num = 0
while num >= 0:
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
print(f'A média é: {(soma-num)/(quant-1)}')