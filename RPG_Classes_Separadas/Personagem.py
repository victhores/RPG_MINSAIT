from SerVivo import SerVivo

class Personagem(SerVivo):
    characters : list[dict[str, object]] = []

    def __init__(self, name, health_points, attack_points):
        super().__init__(name, health_points, attack_points)
        self.characters.append({"Classe": "Personagem",
                                "Nome": name, 
                                "HP": self.health_points, 
                                "AP": self.attack_points})
        print(f'{name} foi adicionado ao jogo como "PERSONAGEM".\n')
    
    def mostrar_personagens(self):
        print(f'\n{self.name} solicitou: \nPersonagens ---> {Personagem.characters}\n')
    
    def excluir_personagem(self, name):
        for personagem in Personagem.characters:
            if personagem["Nome"] == name:
                Personagem.characters.remove(personagem)
                print(f'\n{name} foi excluído do jogo.')
                return
        print(f'\n{name} não foi encontrado no jogo.')
