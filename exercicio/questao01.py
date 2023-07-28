hortifruti = ("banana", 15, "maça", 16, "pêra", 10, "uva", 6, "melancia", 30, "cebola", 45, "alho", 12, "tomate", 13, "cenoura", 18, "pimentão", 4)

entrada = input()

if(hortifruti.count(entrada) != 0):
    print(f"{hortifruti[hortifruti.index(entrada) + 1]}kg")
else:
    print("falta")
