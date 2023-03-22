from Monstro import Monstro

class Goblin(Monstro):
    def __init__(self, name, healt_points, attack_points, intelligence_points):
        super().__init__(name, healt_points, attack_points)
        self.name = name
        self.intelligence_points = intelligence_points
        self.monsters.append({"Classe": "Goblin",
                             "Nome": self.name, 
                             "HP": self.health_points, 
                             "AP": self.attack_points,
                             "IP": intelligence_points})
        print(f'{name} foi adicionado ao jogo como "GOBLIN".\n')
