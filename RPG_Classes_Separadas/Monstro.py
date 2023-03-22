from SerVivo import SerVivo
from Personagem import Personagem

class Monstro(SerVivo):
    monsters : list[dict[str, object]] = []

    def __init__(self, name, healt_points, attack_points):
        super().__init__(name, healt_points, attack_points)

    def mostrar_monstros(self):
        print(f'\n{self.name} solicitou: \nMonstros ---> {Monstro.monsters}\n')

    def attack(self, target):
        self.target = target
        self.damage = self.attack_points
        for i, personagem in enumerate(Personagem.characters[:]):
            if personagem["Nome"] == self.target:
                personagem["HP"] -= self.damage
                print(f'{self.name} atacou {target}. \n{target} agora tem {personagem["HP"]} ponto(s) de saúde.')
                if personagem["HP"] <= 0:
                    Personagem.characters.remove(personagem)
                    print(f'{target} morreu.\n')
                break
        else:
            print(f'\n[ERRO] Não existe nenhum personagem com o nome "{self.target}". Tente novamente.\n')
