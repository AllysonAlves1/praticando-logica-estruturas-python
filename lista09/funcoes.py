def fatorial_lista(*numeros, tipo="menor"):
    def menor_valor(numeros):
        menor = numeros[0]
        for n in numeros:
            if n < menor:
                menor = n
        return menor

    def maior_valor(numeros):
        maior = numeros[0]
        for n in numeros:
            if n > maior:
                maior = n
        return maior

    if tipo == "menor":
        menor = menor_valor(numeros)
        fatorial = 1
        for i in range(1, menor+1):
            fatorial *= i
        print('\n',fatorial, '\n') 

    elif tipo == "maior":
        maior = maior_valor(numeros)
        fatorial = 1
        for i in range(1, maior+1):
            fatorial *= i
        print('\n',fatorial,'\n')
    else:
        return "Tipo inválido"
    

def lista_positivos(*numeros):
    positivos = [n for n in numeros if n > 0]
    print('\n',positivos,'\n')


def lista_negativos(*numeros):
    negativos = [n for n in numeros if n < 0]
    print('\n',negativos, '\n') 

def lista_primos(*numeros):
    primos = []
    for n in numeros:
        if n > 1:
            eh_primo = True
            for i in range(2, n):
                if n % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(n)
    print('\n',primos,'\n')

def lista_pares(*numeros):
    pares = [n for n in numeros if n % 2 == 0]
    print('\n',pares,'\n')

def ultimos_dois(*numeros):
    print('\n',numeros[-2:],'\n')
