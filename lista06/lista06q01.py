# Contando os usuários do sexo masculino e feminino
contagemM = 0
contagemF = 0
i = 0
while i < 6:
    i += 1
    sexo = input("Qual é o seu sexo?")
    while sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
        print('Digite a letra m ou M para masculino e a letra f ou F para feminino')
        sexo = input("Qual é o seu sexo?")
    if sexo == 'm' or sexo == 'M':
        contagemM += 1

    if sexo == 'f' or sexo == 'F':
            contagemF += 1
    
    if sexo == '':
        break

print(f'Dos clientes {contagemM} são do sexo masculino e {contagemF} são do sexo feminino')
