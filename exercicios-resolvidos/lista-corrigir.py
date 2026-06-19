# Exercício 1
# Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve: - Pegar o usuário qual produto vai ser cadastrado por meio de um input - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente" 
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem Produto X cadastrado com sucesso e em seguida printar a lista completa produtos = ["celular", "camera", "fone de ouvido", "monitor"] 

produtos = []
cadastrar = int(input("Quantos produtos vc quer cadastrar? "))
print("Quantidade de produtos para cadastrar: ", cadastrar)

for i in range(cadastrar + 1):
    print(f"registro: {i}")
    novo_produto = input("Cadastre um produto: ").lower()
    
    if novo_produto not in produtos:
        produtos.append(novo_produto)
        print(f"Produto {novo_produto} foi inserido com sucesso")
        
    else:
        print("Produto já cadastrado")
    print("produtos: ",produtos)

print("================")
print("Saiu do programa")
print("================")




