valor = float(input("Digite o valor da compra: "))
if valor >= 200:
    print("Desconto de 10% aplicado!")
    valor *= 0.9
else:
    print("Sem desconto.")
print(f"Total a pagar: R${valor:.2f}")