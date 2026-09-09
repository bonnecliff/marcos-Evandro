nome= input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))

if quantidade == 0:
    estoque = "Produto esgotado!"
elif quantidade <= 5:
    estoque = "Estoque crítico!"
elif quantidade <=20: 
    estoque = "Estoque baixo!"
else:
    quantidade >=21
    estoque = "Estoque normal"

print(f"nome: {nome}")  
print(f"quantidade: {quantidade}")
print(f"situaçaõ do estoque: {estoque}")
