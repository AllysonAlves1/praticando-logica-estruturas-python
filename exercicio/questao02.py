livros = []

N = int(input())

for _ in range(N):
    N = input()
    livro = N.split(", ")
    livros.append(livro)
    
for livro in livros:
    print(f"Livro {livro[0]} de {livro[1]} foi publicado em {livro[2]}.")