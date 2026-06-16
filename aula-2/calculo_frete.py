valor = float(input("Digite o valor da compra: "))
if valor >= 300:
    print("Frete grátis aplicado!")
    print(f"Valor final: R${valor}")
else:
    print("Frete de R$30,00 adicionado.")
    total = valor + 30.00
    print(f"Valor final: R${total}")