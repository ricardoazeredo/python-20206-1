#1
n = int(input('Número: '))
if n % 2 == 0:
    print('Par')
else:
    print('Ímpar')

#2
idade = int(input('Idade: '))
if idade >= 18:
    print('Adulto')
elif idade >= 12:
    print('Adolescente')
else:
    print('Criança')

#3
nota1 = 6
nota2 = 8
media = (nota1 + nota2)/2
if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')
