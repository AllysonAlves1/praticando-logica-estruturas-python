# Biblioteca para utilizar a criação de números aleatórios
import random

# Utilizamos o sample para não ter repetição de números
numeros = tuple(random.sample(range(1, 101), 5))

# Retorna os números gerados na tupla
print(numeros)

# Retorna o menor valor da tupla
print(min(numeros))

# Retorna o maior valor da tupla
print(max(numeros))
