# Imprimindo os resultados dos números digitados pelo usuário
soma_num = 0
produto_num = 1
maior_num = 0
menor_num = 9999
for num in range(6):
    numero = int(input("Digite um número: "))
    soma_num += numero
    media = soma_num/6
    produto_num *= numero
    if numero < menor_num:
        menor_num = numero
    if numero > maior_num:
        maior_num = numero

print(f'Foram digitados <{num+1}> números e o resultado foi: \nSoma: {soma_num}\nMédia: {media}\nProduto: {produto_num}\nMenor: {menor_num}\nMaior: {maior_num}') 