nome = input("Digite o nome do cliente: ")
velocidade = int(input("Digite a velocidade em Mbps: "))

if velocidade <=50:
    plano = " Plano basico: "
elif velocidade <=199:
    plano = " Plano intermediário: "
elif velocidade <= 499:
    plano = " Plano avançado: "
else:
    velocidade>= 500
    plano = " Plano ultra: "

print (f"nome: {nome}")
print (f"plano: {plano}")
print (f"velocidade: {velocidade} Mbps")
