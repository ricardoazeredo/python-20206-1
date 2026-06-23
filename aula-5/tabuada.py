# ===============================
# TABUADA COM FUNÇÕES - VERSÃO SIMPLES
# ===============================

def ler_numero():
    """Pede um número inteiro ao usuário."""
    while True:
        try:
            numero = int(input("Digite um número para ver sua tabuada: "))
            return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def gerar_tabuada(numero):
    """Gera a tabuada de 1 a 10 para o número informado."""
    tabuada = []
    for i in range(1, 11):
        resultado = numero * i
        tabuada.append((i, resultado))  # armazena par (multiplicador, resultado)
    return tabuada


def mostrar_tabuada(numero, tabuada):
    """Exibe a tabuada formatada na tela."""
    print(f"\nTabuada do {numero}")
    print("-" * 20)
    for i, resultado in tabuada:
        print(f"{numero} x {i} = {resultado}")
    print("-" * 20)



"""Função principal que coordena o programa."""
print("=== GERADOR DE TABUADA ===")
numero = ler_numero()
tabuada = gerar_tabuada(numero)
mostrar_tabuada(numero, tabuada)


