# Diga a cor do CD que você quer

cor = input("Digite a cor do CD: ")

match cor:
    case "verde":
        print("R$ 10")
    case "azul":
        print("R$ 20")
    case "amarelo":
        print("R$ 30")
    case "vermelho":
        print("R$ 40")
    case _:
        print("Digite uma das cores verde, azul, amarelo ou vermelho")