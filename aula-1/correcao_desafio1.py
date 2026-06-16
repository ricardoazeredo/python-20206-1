#1
nome='Ana'; idade=28; cidade='Rio'
print(f'Olá {nome}, {idade} anos, mora em {cidade}.')

#2
num = float(input('Número: '))
if num > 0:
    print('Positivo')
elif num < 0:
    print('Negativo')
else:
    print('Zero')

#3
peso = 70; altura = 1.75
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Normal')
elif imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')
