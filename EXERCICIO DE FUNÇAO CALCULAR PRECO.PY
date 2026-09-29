def calcular_total(preco, quantidade):
    total = preco * quantidade
    return total


preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

total = calcular_total(preco, quantidade)

print(f"Total da compra: R$ {total:.2f}")