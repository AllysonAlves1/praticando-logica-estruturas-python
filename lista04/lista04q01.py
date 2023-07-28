def notas(nota1,nota2,nota3,nota4):
    media = (nota1+nota2+nota3+nota4)/4
    if(media>10 or media < 0):
        print("Nota inválida!")
    elif(media>=9):
        print("A")
    elif(media >= 7.5 and media < 9):
        print("B")
    elif(media>=6 and media < 7.5):
        print("C")
    elif(media >=4 and media < 6):
        print("D")
    elif(media >= 0 and media < 4 ):
        print("E")
    
notas(-1,-1,-1,-1) #Coloque suas notas para calcular a média