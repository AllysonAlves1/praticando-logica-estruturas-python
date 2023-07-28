cidades = []

while True:
    cidade = input("Digite o nome de uma cidade: ").lower()
    if cidade == '':
        break
    cidades.append(cidade)
for i in cidades:
    vogais = []
    for vogal in i:
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
            vogais.append(vogal)
    print(i, vogais)