Livros = []

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))

    livro = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade}

    livros.append(livro)

    print("Livro cadastrado com sucesso!")

