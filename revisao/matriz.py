n = int(input())
matriz = []
for i in range(n):
    print(i)
    linha = list(map(int, input().split()))
    matriz.append(linha[i])
        
soma = 0
for k in matriz:
    soma += k

print(f"SOMA = {soma}")
