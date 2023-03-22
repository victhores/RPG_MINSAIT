from ContaBancaria import ContaBancaria

class ContaEspecial(ContaBancaria):
    def bajular_cliente(self):
        print("O senhor gostaria de um cafezinho?")


cliente_indra = ContaEspecial(titular="Indra Company", saldo=12000.83)
cliente_indra.depositar(30000)
cliente_indra.sacar(12000.83)
cliente_indra.consultar_saldo()

