livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livros.append([titulo, autor])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")

        excluido = False
 
        for contador in livros:
            if contador[0].lower()== pesquisa.lower():
                livros.remove(contador)
                print("Livro excluído!")
                excluido = True

            if not excluido:
                print("nenhum digito foi excluido")


    elif opcao == "5":

        print("Programa encerrado.")
        break

    elif opçao =="2":
        print("quantidade de livro cadastrado", len (livros))

    else:

        print("Opção inválida!")

    