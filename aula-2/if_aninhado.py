nota = float(input("Nota: "))

if nota >= 7:
    participacao = input("Participou de todas as aulas? (s/n) ")
    if participacao == "s":
        print("Aluno aprovado com excelência.")
    else:
        print("Aprovado, mas com ressalvas de frequência.")
else:
    print("Aluno reprovado.")
        