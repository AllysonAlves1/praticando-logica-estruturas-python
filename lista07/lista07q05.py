nums = []

while True:
    num  = int(input("Digite um número: "))
    if num == 0:
        break
    nums.append(num)

while True:
    print(f'[1] Quantidade de números digitados: {len(nums)}\n[2] Soma: {sum(nums)}\n[3] Sair')
    escolha = int(input())
    if escolha == 3:
        break