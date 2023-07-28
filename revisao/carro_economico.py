n = int(input())
carros = []

for _ in range(n):
    carro, km = input().split()
    km = int(km)
    carros.append((carro, km))

carro_mais_economico = carros[0]
carro_menos_economico = carros[0]

for carro in carros[1:]:
    if carro[1] > carro_mais_economico[1]:
        carro_mais_economico = carro
    elif carro[1] < carro_menos_economico[1]:
        carro_menos_economico = carro


print(f'MAIS ECONÔMICO: {carro_mais_economico[0]}\nMENOS ECONÔMICO: {carro_menos_economico[0]}\n\nPARA 1000KM:\n{carro_mais_economico[0]} gasta {1000/carro_mais_economico[1]:.1f}\n{carro_menos_economico[0]} gasta {1000/carro_menos_economico[1]:.1f}')