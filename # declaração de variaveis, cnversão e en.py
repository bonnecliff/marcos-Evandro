# declaração de variaveis, cnversão e entrada de dados
#pelo usuario
nome= input("informe seu nome:")
idade = int(input("informe sua idade:"))
altura = float(input("informe altura: "))

# implementação 01
print ("o nome informado foi:", nome)
print ("A altura informada foi:", altura)
print (" A idade informada foi:", idade)

if idade >= 18:
    print("pra essa idade o voto e obrigatoio.")
else: 
    print("Émenor de idade.")