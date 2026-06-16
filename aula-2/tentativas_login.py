tentativas = 3
senha_correta = "admin"

while tentativas > 0:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Login Autorizado")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Acesso bloqueado por tentativas excessivas.")