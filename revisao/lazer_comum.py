lazer_em_comum = []
pessoa1 = input().strip().split(", ")
pessoa2 = input().strip().split(", ")

for lazer1 in pessoa1:
    for lazer2 in pessoa2:
        if lazer1 == lazer2:
            lazer_em_comum.append(lazer1)

lazer_em_comum.sort()
if lazer_em_comum:
    print(", ".join(lazer_em_comum))
else:
    print("NADA")