nums = []

while True:
    num  = int(input("Digite um número: "))
    if num == 0:
        break
    nums.append(num)
print(f'A lista dos números:{nums} e sua quantidade é de {len(nums)}')