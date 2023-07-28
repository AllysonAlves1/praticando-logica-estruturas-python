# Algoritmo que devolve a quantidade de números digitados, soma, média e produto
quant = 0
soma = 0
produto = 1
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    quant += 1
    soma += num
    if num != 0:
        produto*=num

print('[1] Quantidade de números digitados \n[2] Soma\n[3] Média\n[4] Produto\n[5] Sair')
numero_escolhido = int(input())
if numero_escolhido == 1:
    print(f'Quantidade de números digitados: {quant-1}')
elif numero_escolhido == 2:
    print(f'Soma: {soma}')
elif numero_escolhido == 3:
    print(f'Média: {(soma-num)/(quant-1)}')
elif numero_escolhido == 4:
    print(f'Produto: {produto}')
elif numero_escolhido == 5:
    print(f'Saindo...')