# MATCH - IDADE
idade = int(input("Digite a idade: "))

match idade:    
    case _ if idade < 12:
        print("Criança")
    case _ if idade < 18:
        print("Adolescente")
    case _ if idade < 60:
        print("Adulto")
    case _ if idade >= 60:
        print("Idoso")
    case _:
        print("Idade inválida!")