contador = 1

while contador<=1:
    print(contador)
    contador = contador + 1

senha =""
while senha!= "1234":
    senha = input(" Digite a senha: ")
    print ("Acesso permitido!")
    quantidade= int(input("Quantos alunos? " ))

contador= 1
while contador <= quantidade:
    nome = input("Digite o nome do aluno:")
    print("Aluno cadastrado:" , nome)
    contador = contador + 1

opcao = 0
while opcao != 1:
    print("1 - Cadastrar aluno")
    print("2 - listar alunos")
    print("3 - Sair") 

    opcao = int(input("Escolha uma opção: " ))

    if opcao == 1:
            print("cadastro de aluno")
    elif opcao == 2:
            print("Lista de alunos")
    elif opcao == 3:
            print("saindo...")
    else:
            print("opçao invalida!")
    quantidade = int(input("Quantos livros deseja cadastrar? "))
    print()
contador = 1 
while contador <=1:
     idade = int(input("Digite a idade:"))
     if idade >= 18:
       print("Maior de idade")
     else:
         print("Menor de idade")
     contador = contador + 1

nota = float(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota >10:
    print ("nota invalida!")
    nota = float(input("Digite uma nota de 0 a 10: "))
    print("Nota registrada:" , nota)













