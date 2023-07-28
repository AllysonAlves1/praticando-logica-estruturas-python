# Imprimindo os números pares no intervalo determinado
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
if(num1>num2):
    print('Digite o segundo número maior do que o primeiro')
for num in range(num1+1,num2):
    if(num%2==0):
        print(num)