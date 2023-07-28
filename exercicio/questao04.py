entrada = map(int, input().split())
pares = []
impares = []
for i in entrada:
    if(i % 2 == 0):
        pares.append(i)
    else:
        impares.append(i)
pares.sort()
impares.sort()
inteiros = [pares, impares]
print(inteiros)