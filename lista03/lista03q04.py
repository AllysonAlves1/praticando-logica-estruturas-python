# Digite três números
def imprimindo_resultado():
    num1=int(input("Digite um número: "))
    num2=int(input("Digite um número: "))
    num3=int(input("Digite um número: "))
    nums = [num1,num2,num3]
    # Média
    media = (num1+num2+num3)/3

    # Soma
    soma = num1+num2+num3

    # Produto
    produto = num1*num2*num3

    print("A média é: {}, a soma: {}, o produto é: {}, o menor valor é: {} e o maior valor é: {}".format(media,soma,produto,min(nums),max(nums)))

imprimindo_resultado()