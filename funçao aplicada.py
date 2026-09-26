biblioteca  =[]

def cadastro_livro():
    titulo = input("Titulo: ")
    autor = input("Autor")
    livro = [titulo, autor]
    biblioteca.append(livro)

    def listar_livros():
        for contador in biblioteca:
            print("Titulo: ", contador[0])
            print("Autor:", contador[1])

            cadastar_livros(
    
    )