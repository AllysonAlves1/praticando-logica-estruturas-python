paises = []
while True:
    pais = input('Digite o nome do país: ').upper()
    if pais == '':
        break
    paises.append(pais)
for pais in paises:
    if pais[0] == 'B':
        print(pais)