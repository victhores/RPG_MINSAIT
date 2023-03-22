class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular: str = titular
        self.saldo: float = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo: 
            print('[ERRO] Saldo insuficiente!')
        else:
            self.saldo -= valor

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")
    
Victor = ContaBancaria(titular="Victor", saldo=0.81)