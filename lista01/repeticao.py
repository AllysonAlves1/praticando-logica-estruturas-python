# import random

# inicio = int(input("Diga o valor meu patrao: "))
# for num in range(inicio, 21,2):
#     print(num)

# Jogo da adivinhação
# num = (random.randrange(0,10))
# # print(num)
# valor = 0
# while valor != num:
#     valor = int(input("Digite o valor: "))
#     if(num == valor):
#         print("Você acertou!")
#         break
#     else:
#         print("Você errou!")
#         continue

# tabuada
# num_tabuada = int(input("Digite o valor: "))
# for num in range(1,11):
#     print(f"{num_tabuada} x {num} = {num_tabuada*num}")

# Descobrindo o maior valor usando função
# valores = []
# for _ in range(8):
#     num = int(input('digite um numero:'))
#     valores.append(num)
# print(f'O maior valor foi: {max(valores)}')

#Descobrindo o maior valor sem o uso de uma função
# numero_anterior = 0
# for num in range(8):
#     num = int(input('Digite um número: '))
#     if num > numero_anterior:
#         numero_anterior = num
# print(f'O maior valor foi: {numero_anterior}')

#Descobrindo o menor valor sem o uso de uma função
# numero_anterior = 9999
# for num in range(8):
#     num = int(input('Digite um número: '))
#     if num < numero_anterior:
#         numero_anterior = num
# print(f'O menor valor foi: {numero_anterior}')