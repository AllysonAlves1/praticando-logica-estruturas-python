def imposto():
    # Digite o valor e o ano do carro
    valor=float(input("Digite o valor do carro? "))
    ano=int(input("Digite o ano do carro? "))
    if(ano<1990):
        valor=(valor*0.01)
        print("O valor é: {}".format(valor))
    else:
        valor=valor*0.015
        print("O valor é: {}".format(valor))

imposto() #Inicializando a função