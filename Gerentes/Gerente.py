class Gerente:
    def __init__(self, numero_de_funcionarios_disponiveis):
        self.numero_de_funcionarios_disponiveis = numero_de_funcionarios_disponiveis
    
    def atribuir_tarefa(self):
        pass



gerente_normal = Gerente(10)
print(gerente_normal.numero_de_funcionarios_disponiveis)

gerente_normal.atribuir_tarefa()
print(gerente_normal.numero_de_funcionarios_disponiveis)
