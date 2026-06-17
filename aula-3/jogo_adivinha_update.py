import os
import random  # Nova biblioteca para manipular a lista

# 1. Declaração de Vetores (Listas) e Variáveis
banco_palavras = ['python', 'backend', 'programacao', 'fullstack', 'codigo']
palavra_secreta = random.choice(banco_palavras) # Seleção dinâmica

letras_acertadas = ''
letras_tentadas = [] # Vetor para armazenar o histórico de chutes
tentativas_restantes = 6 # Controle estrito do loop por tentativas

# 2. Desenvolvimento do Pequeno Programa com Loops (while)
while tentativas_restantes > 0:
    print(f"\nTentativas restantes: {tentativas_restantes}")
    print(f"Letras já testadas: {', '.join(letras_tentadas)}")
    
    letra_digitada = input('Digite uma letra: ').lower()
    
    if len(letra_digitada) > 1 or not letra_digitada.isalpha():
        print('Por favor, digite apenas uma única letra.')
        continue
        
    if letra_digitada in letras_tentadas:
        print('Você já tentou essa letra! Tente outra.')
        continue
        
    letras_tentadas.append(letra_digitada) # Alimentando o vetor
    
    # 3. Verificação usando Loop (for) e Condicionais
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        print("Boa! Você acertou uma letra.")
    else:
        tentativas_restantes -= 1 # Decremento no contador do while
        print("Essa letra não está na palavra.")
        
    # Construção da palavra mascarada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print('Palavra formada:', palavra_formada)
    
    # Condições de Fim de Jogo
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('--- VOCÊ GANHOU!! PARABÉNS! ---')
        print(f'A palavra era: {palavra_secreta}')
        break
else:
    print('\n--- FIM DE JOGO! Suas tentativas acabaram. ---')
    print(f'A palavra correta era: {palavra_secreta}')