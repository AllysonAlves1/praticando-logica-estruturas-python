# Tabuada dos números digitados, caso não queira mais digite o número 0
saida = ""
while saida != "Para tudo!":
    num = int(input("Digite um número: "))
    if num == 0:
        saida = "Para tudo!"
    i=1
    while i <= 10:
        print(f'{num} x {i} = {num*i}')   
        i+=1
