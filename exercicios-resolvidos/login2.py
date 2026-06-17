import random  # Importamos o módulo random no início do arquivo
#=============================================================================
#Resolução do exercício 1 e 2: Sistema de login e direcionamento M2F
#=============================================================================

#1. Base de dados simulada(Dados cadastrados no sistema)
banco_cpf = "12345678900"
banco_email_principal = "diretoria@senac.br"
banco_email_secundario = "suporte@senac.br"
banco_m2f_enabled = True

print("--TELA DE AUTENTICAÇÃO--")

#2. Entrada de dados do usuário
input_cpf = input("Informe o CPF cadastrado: ")
input_email =  input("Informe o e-mail cadastrado: ")

#3. Processamento das regras de validação (lógica solicitada na especificação)
print(f"CPF é válido? {input_cpf == banco_cpf}")
cpf_valido = input_cpf == banco_cpf

#O e-mail informado deve corresponder ao principal ou ao secundário
email_valido = (input_email == banco_email_principal) or (input_email == banco_email_secundario)
print(f"Email logado: {email_valido}")

# O login exige obrigatoriamente CPF E E-mail corretos simultaneamente 
pode_logar = cpf_valido and email_valido
print("Pode logar: "+ str(pode_logar))

# 4. Saída de Dados e Validação de Fluxo de Segurança 
if pode_logar:
    print("\n Credenciais básicas validadas com sucesso!")
    # Verificação do status de M2F (Caso de Uso de Fluxo Opcional) 
    if banco_m2f_enabled:
        # Saída esperada se o M2F estiver ativo para este usuário específico 
        print("[M2F Ativo] - Segunda etapa de autenticação é obrigatória.")
        print("Resultado retornado: {'autenticado': False, 'm2f_requirido': True}")

        # --- 4 NÚMEROS ALEATÓRIOS INDIVIDUAIS ---
        # Gera uma lista contendo 4 números aleatórios entre 0 e 9
        numeros_aleatorios = [random.randint(0,9) for _ in range(4)]
        print(f"Números gerados para o token: {numeros_aleatorios}") 

        # Junta as 4 unidades de números para formar o código final em formato de texto (string)
        codigo_gerado = "".join(map(str, numeros_aleatorios))
        
        # Pede para o usuário digitar o código recebido
        input_codigo = input("Digite o código correspondente aos números gerados: ")
        
        # Compara o código digitado com o gerado
        if input_codigo == codigo_gerado:
            print("\n Código M2F correto!")
            print("Resultado retornado: {'autenticado': True, 'm2f_requirido': True}")
        else:
            print("\n Falha na autenticação: Código M2F incorreto.")
            print("Resultado retornado: {'autenticado': False, 'm2f_requirido': True}")
     
    else:
        # Saída esperada se o M2F estiver desativado
        print("[M2F INATIVO] - Acesso direto liberado para o painel")
        print("Resultado retornado: {'autenticado': True, 'm2f_requirido': False}")
else:
    print("\n Falha na autenticação: CPF ou E-mail incorretos.")        