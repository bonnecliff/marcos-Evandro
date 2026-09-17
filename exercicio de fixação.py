contador = 1

while contador<=5:
    print(contador)
    contador = contador + 1
    print()

    senha =""
    while senha!= "1234":
        senha = input(" Digite a senha: ")
        print ("Acesso permitido!")
        print()
        quantidade= int(input("Quantos alunos? " ))

        contador= 1
        while contador <= quantidade:
            nome = input("Digite o nome do aluno:")
            print("Aluno cadastrado:" , nome)
            contador = contador + 1

            opão = 0
            print()
            while opcao != 3:
                print("1 - Cadastrar aluno")
                print("2 - listar alunos")
                print("3 - Sair")

                opcao = 




