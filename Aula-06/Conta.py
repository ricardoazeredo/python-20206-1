class Conta:
    def __init__ (self,saldo):
        self.saldo = saldo

    def depositar(self, saldo):
        self.saldo += saldo
    
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Valor sacado foi de R${valor}. Saldo atual é de R${self.saldo}.")
        else:
            print("Saldo insuficiente")

    