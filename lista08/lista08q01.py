nums = []
pares = []
impares = []
primos = []

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    nums.append(num)

    # Números Pares
    if num % 2 == 0:
        pares.append(num)

    # Números Ímpares
    elif num % 2 == 1:
        impares.append(num)

# Números primos
for n in nums:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    if n >= 2 and primo:
        primos.append(n)
while True:
    print('[1] Quantidade total de números digitados.\n[2] A lista de números ímpares.\n[3] A lista de números pares.\n[4] A lista de números primos.\n[5] Os dois primeiros números digitados.\n[6] Os dois últimos números digitados.\n[7] Sair')
    escolha = int(input())
    match escolha:
        case 1:
            print(f'\n----------------------------\n Quantidade total de números digitados: {len(nums)} \n----------------------------\n')
        case 2:
            print(f'\n----------------------------\n A lista de números ímpares: {impares} \n----------------------------\n')
        case 3:
            print(f'\n----------------------------\n A lista de números pares: {pares} \n----------------------------\n')
        case 4:
            print(f'\n----------------------------\n A lista de números primos: {primos} \n----------------------------\n')
        case 5:
            print(f'\n----------------------------\n Os dois primeiros números digitados: {nums[:2]} \n----------------------------\n')
        case 6:
            print(f'\n----------------------------\n Os dois últimos números digitados: {nums [-2:]} \n----------------------------\n')
        case 7:
            break
        case _ :
            print('O número é inválido!\nDigite um que esteja na lista.')


