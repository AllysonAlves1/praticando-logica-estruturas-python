def notas(nota1,nota2,nota3,nota4):
    media = (nota1+nota2+nota3+nota4)/4
    if(media>=9):
        print("A")
    elif(media >= 7.5 and media < 9):
        print("B")
    elif(media>=6 and media < 7.5):
        print("C")
    elif(media >=4 and media < 6):
        print("D")
    else:
        print("E")

notas(10,5,5,5) #Coloque suas notas para calcular a média