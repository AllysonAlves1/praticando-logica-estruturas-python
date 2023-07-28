# Um algoritmo que faça a contagem dos números que são divisíveis por 3
quant = 0
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    if num % 3 == 0:
        quant +=1
print(f"A quantidade de números divisíveis por 3 é: {quant-1}")

