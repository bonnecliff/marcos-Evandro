print("=====sistema para biblioteca =====")
print("1 - cadastrar livro")
print("2 - cadastrar aluno")
print("3 - Realizar emprestimo")
print("4 - Sair")
opção= input("Digite a opção desejada")
if opção== "1" :
   Quantidade_livros= int (input("Quantos livros deseja cadastrar?"))
   For: in range (quantidade_livros)
   nome_livro= input(f"Digite o nome do livro{i+1}:")
   codigo_livro= input(f"Digite o codigo do livro{i+1}:")
   print (f"livro" {nome_livro})("codigo{codigo_livro})cadastrado:")
   print("cadastro de livro concluido!\n")
elif opção== "2" :
    print("=====cadastrar alunos =====")
    quantidade= int(input("Quantos alunos deseja cadastrar?: "))
    for in range (quantidade)
    Nome_aluno= input(f"Digite o nome do livro{i+1}:")
    matricula_aluno = input(f"Digite a matricula do aluno{i+1}:")
    print= (f "aluno" {nome_aluno})("Matricula{matricula_do aluno})cadastrado:")
    print("cadastro de aluno concluido!\n")
elif opção =="3":
 codigo_livro= input(f"Digite o codigo do livro :")
 matricula_aluno = input("Digite a matricula do aluno:")
if codigo_livro =""and matricula_aluno!="":
    print("emprestimo registrado com sucesso!\n")
    "print"("erro dados invalidos ou livro indisponivel:\n")
elif opção=="4":
    print("encerrando o sistema. ate logo!")
