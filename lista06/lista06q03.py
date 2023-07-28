# Contabilizando quantos números foram digitados e a soma desses números até receber o número 0
quant = 0
soma = 0
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    quant += 1
    soma += num
print('[1] Quantidade de números digitados \n[2] Soma\n[3] Sair')
numero_escolhido = int(input())
if numero_escolhido == 1:
    print(f'Quantidade de números digitados: {quant-1}')
elif numero_escolhido == 2:
    print(f'Soma: {soma}')
elif numero_escolhido == 3:
    print('Saindo...')