import funcoes

numeros = []

while True:
    num = int(input('Digite um número: '))
    if num == -1:
        break
    else:
        numeros.append(num)

while True:
    print('[1] O fatorial do menor número digitado\n[2] A lista de números positivos\n[3] A lista de números negativos\n[4] A lista de números primos\n[5] A lista dos números pares\n[6] Os dois últimos números digitados\n[7] O fatorial do maior número digitado\n[8] Sair')
    menu = int(input('Digite um número: '))
    match menu:
        case 1:
            funcoes.fatorial_lista(*numeros)
        case 2:
            funcoes.lista_positivos(*numeros)
        case 3:
            funcoes.lista_negativos(*numeros)
        case 4:
            funcoes.lista_primos(*numeros)
        case 5:
            funcoes.lista_pares(*numeros)
        case 6:
            funcoes.ultimos_dois(*numeros)
        case 7:
            funcoes.fatorial_lista(*numeros, tipo= "maior")
        case 8:
            print('Saindo...')
            break
        case _ :
            print('Operação inválida, escolha algum número da lista\n')