# dados_mensal = int(input())
# meses = int(input())
# valor = 0
# valor_final = 0
# sobrou = 0
# for i in range(meses):
#     gasto = int(input())
#     if dados_mensal > gasto:
#         sobrou = dados_mensal - gasto
#         valor = dados_mensal + sobrou
#         valor_final = valor + dados_mensal
#     elif gasto >= dados_mensal:
#         valor = dados_mensal + sobrou
#         valor_final = valor + dados_mensal - gasto

# print(valor_final)

#ChatGPT
# Leitura da entrada
# dados_mensal = int(input())
# meses = int(input())
# megabytes_usados = []

# for _ in range(meses):
#     megabytes_usados.append(int(input()))

# # Cálculo da quota atual
# quota_atual = dados_mensal
# print(quota_atual)

# for i in range(meses):
#     megabytes_usados_mes = megabytes_usados[i]
#     quota_atual += (dados_mensal - megabytes_usados_mes)

# # Impressão do resultado
# print(quota_atual)

#Novo modelo
dados_mensal = int(input())
meses = int(input())
megabytes_usados = []
quota_atual = dados_mensal

for _ in range(meses):
    gasto = int(input())
    megabytes_usados.append(gasto)
    quota_atual += dados_mensal
for i in megabytes_usados:
    quota_atual -= i

print(quota_atual)