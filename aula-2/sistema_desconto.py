categoria = input("Digite o tipo de cliente (comum, vip, parceiro): ")
valor = float(input("Valor da compra: "))

if categoria == "vip":
    desconto = 0.15
elif categoria == "parceiro":
    desconto = 0.10
else:
    desconto = 0.05

valor_final= valor - (valor * desconto)
print(f"Desconto aplicado: {desconto*100}%")
print(f"Valor final: R${valor_final:.2f}")