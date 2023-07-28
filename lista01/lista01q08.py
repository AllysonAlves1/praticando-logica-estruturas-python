
valor = float(input('Qual foi o valor do produto? '))
desconto = int(input('O produto tem um desconto de: '))
novo_valor = valor - (valor*(desconto/100))
print('O valor do produto R${} com desconto de {}% é: {}'.format(valor, desconto, novo_valor))