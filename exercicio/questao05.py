palavra1 = input().lower()
palavra2 = input().lower()

letras_comuns = set(palavra1) & set(palavra2)

print(" ".join(sorted(letras_comuns)))