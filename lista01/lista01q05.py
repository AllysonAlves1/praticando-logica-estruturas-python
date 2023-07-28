import datetime
ano_de_nascimento = int(input('Em que ano você nasceu? '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano_atual = int(date.strftime("%Y"))

idade = ano_atual - ano_de_nascimento
idade_em_2028 = 2028 - ano_de_nascimento
print('Sua idade é:', idade)
print('Em 2028 sua idade será:', idade_em_2028)
