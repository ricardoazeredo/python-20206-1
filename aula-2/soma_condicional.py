#Soma de Números com Condição​
total = 0
contador = 0
while True:    
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    total += numero
    contador += 1
media = total / contador
print(f"Soma total: {total}")
print(f"Média dos números: {media:.2f}")