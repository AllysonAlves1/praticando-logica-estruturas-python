
# Calculando o IMC do indivíduo 

def calculando_imc(peso,altura):
    imc= peso/(altura**2)
    if(imc < 18.5):
        return 'Seu IMC é: {:.1f} e você está abaixo do peso'.format(imc)
    elif(imc >= 18.5 and imc <= 24.9):
        return 'Seu IMC é: {:.1f} e você está peso normal'.format(imc)
    elif(imc >= 25 and imc <= 29.9):
        return 'Seu IMC é: {:.1f} e você está sobrepeso'.format(imc)
    elif(imc >= 30 and imc <= 34.9):
        return 'Seu IMC é: {:.1f} e você está obesidade I'.format(imc)
    elif(imc >= 35 and imc >= 39.9):
        return 'Seu IMC é: {:.1f} e você está obesidade II'.format(imc)
    else:
        return 'Seu IMC é: {:.1f} e você está obesidade III'.format(imc)

# Informe seu peso em Kg e sua altura em metros

print(calculando_imc(52,1.57)) # Imprimindo o índice de massa corpórea