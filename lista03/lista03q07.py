def aumento_salario(cargo,salarioInicial):
    if(cargo == "gerente"):
        salario=(salarioInicial*0.1)+salarioInicial
    elif(cargo=="engenheiro"):
        salario=(salarioInicial*0.2) +salarioInicial
    elif(cargo=="tecnico"):
        salario=(salarioInicial*0.3) +salarioInicial
    else:
        salario = (salarioInicial*0.5) +salarioInicial

    print("O seu antigo sálario era: {}, seu novo salário: {} e a diferença é {}.".format(salarioInicial,salario,salario-salarioInicial))

aumento_salario("tecnico",10000) # Digite seu cargo e seu salário atual