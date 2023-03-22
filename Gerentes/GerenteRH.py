from Gerente import Gerente

class GerenteRH(Gerente):
    def demitir_funcionario(self):
        self.numero_de_funcionarios_disponiveis -= 1
    


gerente_de_rh = GerenteRH(10)
print(gerente_de_rh.numero_de_funcionarios_disponiveis)
gerente_de_rh.atribuir_tarefa()
print(gerente_de_rh.numero_de_funcionarios_disponiveis)
