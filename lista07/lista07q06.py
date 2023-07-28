nums = []
listaPar = []
listaImpar = []

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    nums.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

while True:
    print('[1] Quantidade total de números digitados\n[2] Quantidade de números ímpares\n[3] Quantidade de números pares\n[4] Menor número\n[5] Maior número\n[6] Média\n[7] Sair')
    escolha = int(input())
    match escolha:
        case 1:
            print(f'\n----------------------------\n[1] Quantidade total de números digitados: {len(nums)} \n----------------------------\n')
        case 2:
            print(f'\n----------------------------\n[2] Quantidade de números ímpares: {len(listaImpar)} \n----------------------------\n')
        case 3:
            print(f'\n----------------------------\n[3] Quantidade de números pares: {len(listaPar)} \n----------------------------\n')
        case 4:
            print(f'\n----------------------------\n[4] Menor número: {min(nums)} \n----------------------------\n')
        case 5:
            print(f'\n----------------------------\n[5] Maior número: {max(nums)} \n----------------------------\n')
        case 6:
            print(f'\n----------------------------\n[6] Média: {(sum(nums)/len(nums))} \n----------------------------\n')
        case 7:
            break
