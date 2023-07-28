# Fatorial de um número inteiro
i = 1
valor = 1
num = int(input("Número do fatorial: "))
fatorial = num
while i < num:
    valor *= num
    num-=1
print(f'{fatorial}! = {valor}')
    