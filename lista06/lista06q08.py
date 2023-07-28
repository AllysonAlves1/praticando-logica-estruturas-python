# O maior valor dos números digitados até receber -1 como saída do programa
num = 0
valor = 0
while num != -1:
    num = int(input("Digite um número: "))
    if num > valor:
        valor = num
print(f"O mairo valor digitado foi: {valor}")