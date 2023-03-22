from Gerente import Gerente

class GerenteEstoque(Gerente):
    def atribuir_tarefa(self):
        print("Atribuir tarefa para estoque")
        self.numero_de_funcionarios_disponiveis -= 5

gerente_de_estoque = GerenteEstoque()
print(gerente_de_estoque.numero_de_funcionarios_disponiveis)
gerente_de_estoque.atribuir_tarefa(10)
print(gerente_de_estoque.numero_de_funcionarios_disponiveis)
