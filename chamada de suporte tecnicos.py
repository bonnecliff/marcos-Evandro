nome = input (" digite o nome do usuario: ")
print()
print('===== QUAL TIPO DE PROBLEMA =====')
print()
print("1- Indisponibilidade total do sistema")
print("2- Sistema funcionando, mas com lentidão ou erros ")
print("3- Problema que não impede o trabalho")
print("4- Outros problemas")
problema = int(input ("digite o tipo de problema: "))
tempo =  int(input(" Há quanto tempo o problema ta ocorrendo (em dias)? "))

if problema == (1):
    prioridade = "critica"
    tipo = "Indisponibilidade total do sistema"

elif problema == (2):
    prioridade = "alta"
    tipo = "Sistema funcionando, mas com lentidão ou erros"

elif problema ==(3):
    prioridade = "média"
    tipo = "Problema que não impede o trabalho"

else:
    prioridade = "baixa"
    tipo = "Outros problemas"
    
print(f"cliente:{nome}")
print (f"problema: {tipo}")
print (f"tempo do problema em dias: {tempo}")
print (f"prioridade: {prioridade}")

