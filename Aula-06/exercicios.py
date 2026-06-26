# 1. Crie uma classe Pessoa com os atributos nome e idade.
#Crie um método que exiba uma mensagem: “Olá, meu nome é [nome] e tenho [idade] anos.”
from Pessoa import Pessoa

pessoa1 = Pessoa("Ricardo", 45)
pessoa1.falar()


# 2. Crie uma classe Carro que tenha modelo, ano e velocidade.
# Adicione métodos acelerar() e frear().
from Carro import Carro

carro1 = Carro("Ônix",2020)
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.mostrarVelocidade()

# 3. Crie uma classe Conta com saldo e métodos depositar() e sacar().
from Conta import Conta

correntista1 = Conta(0)
correntista1.depositar(1000)
correntista1.sacar(200)

# 4. Crie uma classe Animal com método falar().
from Animal import Animal, Cachorro, Gato

caramelo = Cachorro
tom = Gato
qualquer = Animal
caramelo.falar()
tom.falar()
qualquer.falar()

# 5. Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).
from Produto import Produto

notebook = Produto("MacBook",1000)
notebook.desconto() 
# 6. Crie uma classe Livro com título, autor e método exibir_detalhes().
from Livro import Livro

livreto = Livro("O pequeno principe", "Antonie")
livreto.exibir_detalhes()

# 7. Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).
