# O menor valor dos números digitados até receber -1 como saída do programa
valor = 9999
saida = 0
while saida != -1:
    num = int(input("Digite um número: "))
    if num < valor and num != -1:
        valor = num
    if num == -1:
        saida = num
print(f"O menor valor digitado foi: {valor}")