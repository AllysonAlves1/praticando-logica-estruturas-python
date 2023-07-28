
# Transformando em graus Fahrenheit

def converterParaFahrenheit(celsius):
    f = (9*celsius+160)/5
    return 'A temperatura em graus Fahrenheit é: {}'.format(f)

# Qual é a temperatura em Celsius?
#                              |
#                             \ / 
print(converterParaFahrenheit(30)) # Imprimindo o valor da conversão