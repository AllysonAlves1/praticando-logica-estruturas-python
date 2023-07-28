nums = []
decrescente = []
crescente = []

for _ in range(3):
    num = int(input('Digite um número: '))
    nums.append(num)
    for chave,valor in enumerate(crescente): # Com enumerate transformamos a lista em um tupla(chave , valor)
        if num < valor:
            crescente.insert(chave,num) # Insere um novo item com o num no vetor antes da posição chave.
            break
    else:
        crescente.append(num)
    for chave,valor in enumerate(decrescente):
        if num > valor:
            decrescente.insert(chave,num)
            break
    else:
        decrescente.append(num)

while True:
    print('[1] Exibir os números na ordem digitada\n[2] Exibir em ordem Decrescente\n[3] Exibir em ordem Crescente\n[4] Sair')
    escolha = int(input())
    match escolha:
        case 1:
            print(f'\n----------------------------\n {nums} \n----------------------------\n')
        case 2:
            print(f'\n----------------------------\n  {decrescente} \n----------------------------\n')
        case 3:
            print(f'\n----------------------------\n  {crescente} \n----------------------------\n')
        case 4:
            break
        case _ :
            print('O número é inválido!\nDigite um que esteja na lista.')


