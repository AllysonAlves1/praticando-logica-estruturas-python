entrada = input().strip().split()
nova_entrada = ''.join(entrada).lower()

eh_palindromo = True
for i in range(len(nova_entrada)):
    if nova_entrada[i] != nova_entrada[-i-1]:
        eh_palindromo = False
        break

if eh_palindromo:
    print("VERDADEIRO")
else:
    print("FALSO")
