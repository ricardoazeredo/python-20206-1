numero = int(input("Gerar tabuada de: "))
inicio = int(input("início: "))
fim = int(input("fim: "))

for i in range(inicio, fim + 1):
    #print(f"índice i: {i}")
    print(f"{numero} x {i} = {numero * i}")