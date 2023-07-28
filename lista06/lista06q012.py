# Algoritmo que ler dois números e retorna todos os números pares entre eles

num1 = int(input("Limite inferior: "))
num2 = int(input("Limite Superior: "))

if num1 >= num2:
    print("Digite o segundo valor maior do que o primeiro")
    
while num1<num2-2:
    if num1%2==0:
        num1+=2
        print(num1)
    elif num1%2==1:
        num1-=1