class Carro:
    def __init__ (self,modelo,ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade =0
    
    def acelerar(self):
        self.velocidade += 10
    
    def frear(self):
        self.velocidade -= 10
    
    def mostrarVelocidade(self):
        print(f"A velocidade do {self.modelo} do ano {self.ano} é de {self.velocidade} km/h.")
        
