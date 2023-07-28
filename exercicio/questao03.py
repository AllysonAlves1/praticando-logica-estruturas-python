nomes = input().split(", ")
numeros = input().split()
x, y = map(int, numeros)

print(", ".join(nomes[x:y]))