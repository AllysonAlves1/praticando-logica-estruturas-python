# Digite três números

""" num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: ")) """

# Ordenando os valores

""" list = [num1, num2,num3]
list.sort()
print(list)
 """

# Imprimindo os valores

#print(sorted(list))

notas = []
for _ in range(3):
    num = int(input('digite um numero:'))
    notas.append(num)
notas.sort(reverse = True)
print(notas)
