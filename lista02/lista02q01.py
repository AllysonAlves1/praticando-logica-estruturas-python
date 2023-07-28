
# Recebendo os dados do usuário

altura_degrau = float(input('Qual é a altura do degrau em cm? '))
altura_escada = float(input('Qual é a altura da escada? '))

# Calculando a quantidade de degraus para alcançar o topo da escada

topo_da_escada = (altura_escada/(altura_degrau/100))

# Imprimindo a quantidade de degraus que o usuário deverá subir

print("Você terá que subir {:.1f} degraus para chegar ao seu objetivo.".format(topo_da_escada))