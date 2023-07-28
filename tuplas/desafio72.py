# Os números de 0 a 20 em extensão
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input("Digite um número entre 0 e 20: "))

# Caso o número seja menor que 0 ou maior que 20, retorna que o número é inválido, caso seja um número válido segue a função.
if numero < 0 or numero > 20:
    print("Número inválido! Tente novamente.")

else:
    extenso = tupla[numero]
    print(f"O número {numero} por extenso é: {extenso}")
