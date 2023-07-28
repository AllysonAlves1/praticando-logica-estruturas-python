
valor = float(input('Qual foi o valor do produto? '))
parcelas = int(input('Em quantas parcelas você deseja dividir o produto? '))

prestacoes = valor/parcelas

print('O valor das {} prestações irão ser {}'.format(parcelas,prestacoes))

