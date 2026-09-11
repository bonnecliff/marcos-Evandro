nome = input ("Digite o nome do aluno: ")
idade = int (input("Digite a idade do aluno: "))
cadastro = input("Possui cadastro ativo(sim ou não): "). strip(). lower()

if cadastro == "não" or cadastro == "não":
    situação = "acesso negado!"

elif idade < 14:
    situação = "Acesso permitido somente com acompanhamento "

elif idade >= 14 and idade < 18:
    situação =" Acesso permitido" 

else:
    "Acesso permitido"

print("\n=====Resultado=====")
print(f"aluno:{nome}")
print(f"situação:{situação}")