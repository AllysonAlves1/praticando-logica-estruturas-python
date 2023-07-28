# Carrinho de compras
saida = ''
produtos = {}
sum = 0
quant = 0
while saida != 'Stop':
    produto = input('Nome do produto: ')
    valor = float(input('Qual é o valor do produto: '))
    produtos[produto] = valor
    num = int(input('Digite 1 para continuar e 0 para parar: '))
    if num == 0:
        saida = 'Stop'

for i in produtos.values():
    sum = sum + i
    if i > 200:
        quant +=1
maior = 0
menor = 9999999
for key, value in produtos.items():
    if value > maior:
        maior = value
        produto_caro = key
for key, value in produtos.items():
    if value < menor:
        menor = value
        produto_barato = key


print(f'\nO total de gastos da compra: {sum}\nO produto mais caro é: {produto_caro}\nO produto mais barato é: {produto_barato}\nProdutos que custam mais de R$200,00: {quant}')