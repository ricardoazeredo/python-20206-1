class Produto:
    def __init__ (self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self):
        self.preco *= .9
        print(f"O preço atual do produto {self.nome} é de R$ {self.preco}")