def entrar_numero():
    while True:
        try:
            numero = int(input("Digite um número: "))
            return numero
        except ValueError:
            print("digite um número inteiro")

def gerar_tabuada(numero):
    tabuada = []
    for i in range(1,11):
        resultado = numero * i
        tabuada.append((i,resultado))
    return tabuada

def mostrar_tabuada(numero, tabuada):
    print("-"*30)
    print(f"\nTabuada do número {numero}")
    for i, resultado in tabuada:
        print(f"{numero} x {i} = {resultado}")
    print("-"*30)

def receber_numeros():
    try:
        numero1 = float(input("Digite o primeiro numero"))
        numero2 = float(input("Digite o segundo numero"))        
    except ValueError:
        print("digite um valor float")

def somar(num1, num2):
    return num1 + num2

def subtrair(num1,num2):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2
def dividir(num1, num2):
    if num2 == 0:
        return "O denominador não pode ser Zero"
    return num1 / num2
def operador():
    operador = input("Digite o operador multiplicação(*)),divisão(/),soma(+),subtração(-): ")
