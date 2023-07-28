# Classificação do campeonato brasileiro do ano de 2019
classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
                 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

# Os 5 primeiros colocados
print(classificacao[:5])

# Os 4 últimos colocados
print(classificacao[-4:])

# Ordem alfabética
print(sorted(classificacao))

# Em que indice se encontra o time chapecoense
print(classificacao.index("Chapecoense")+1)
