from Monstro import Monstro

class Lobo(Monstro):
    def __init__(self, name, healt_points, attack_points, power_points):
        super().__init__(name, healt_points, attack_points)
        self.name = name
        self.power_points = power_points
        self.monsters.append({"Classe": "Lobo",
                             "Nome": self.name, 
                             "HP": self.health_points, 
                             "AP": self.attack_points,
                             "PP": power_points})
        print(f'{name} foi adicionado ao jogo como "LOBO".\n')