produtos = []

for i  in range(0,4):
    novo_produto = input("cadastre um novo produto: ")
    novo_produto = novo_produto.lower()

    if novo_produto in produtos:
        print("produto já cadastrado")
    else:
        produtos.append(novo_produto)
        print(f"Produto {novo_produto} cadastrado com sucesso")
    print(produtos)
print("====================")    
print("Saiu do programa!")
print("====================")    