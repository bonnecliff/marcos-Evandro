biblioteca = []

def mostrar_menu(): 
    print("\n === BIBLIOTECA===")
    print(" 1- cadastrar livro")
    print(" 2- listrar livro")
    print(" 3- buscaar livro")
    print(" 4- remover livro")
    print(" 0 - sair")


while True:
    mostrar_menu()
    opcao = input("Escolhe uma opção ")

    if opcao =="1":
        titulo = input ("titulo:")
        autor= input ("autor:")
        cadastrar_livro (titulo, autor)

    elif opcao =="2" :
         listrar_livro()

    elif opcao =="3" : 
         titulo = input("Titulo que deseja buscar:")
         buscar_livro (Titulo)

       
    elif opcao =="4" :
         titulo = input ("Titulo que deseja remover:")
         remover_livro (titulo)

    elif opcao =="0" :
        print("Encerado o sistema. Até logo! ")
    break
else:
        print("opçaoo invalida, tente de novo:")
       