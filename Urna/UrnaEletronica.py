class UrnaEletronica:
    def __init__(self):
        self.candidato = [  {"nome_candidato": "André", "partido": "A"},
                            {"nome_candidato":"Bruno", "partido": "B"},
                            {"nome_candidato":"Carlos", "partido": "C"} ]

    def exibe_candidatos(self):
        for candidato in self.candidato:
            print("\nNome do candidato:", candidato.get("nome_candidato"))
            print("Partido do candidato:", candidato.get("partido"))
    
    def adiciona_candidato(self, nome_candidato, partido):
        self.candidato.append({"nome_candidato": nome_candidato, "partido": partido})

    def remove_candidato(self):
        self.candidato.pop()

    def atualiza_candidato(self, indice, chave, novo_dado):
        try:
            self.candidato[indice][chave] = novo_dado
        except Exception as e:
            print(e)
            pass


urna = UrnaEletronica()

urna.adiciona_candidato(nome_candidato="Daniel", partido="D")
urna.adiciona_candidato(nome_candidato="Eder", partido="E")

urna.remove_candidato()

urna.atualiza_candidato(indice=0, chave="nome_candidato", novo_dado="ele")

urna.exibe_candidatos()