#No Python não tem switch case. A partir do Python 3.10, temos o match case, que é uma estrutura de controle de fluxo que permite comparar um valor com vários padrões e executar um bloco de código correspondente ao primeiro padrão que corresponder.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "+":       
        print("Resultado: ", num1 + num2)
    case "-":
        print("Resultado: ", num1 - num2)
    case "*":
        print("Resultado: ", num1 * num2)
    case "/":
        print("Resultado: ", num1 / num2)
    case _:
        print("Operação inválida!")