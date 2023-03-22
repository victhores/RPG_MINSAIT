class SerVivo:
    def __init__(self, name, healt_points, attack_points):
        self.name = name
        self.health_points = healt_points
        self.attack_points = attack_points

    def mostrar_seres_vivos(self):
        print(f'\n{self.name} solicitou: \nPersonagens ---> {Personagem.characters}')
        print(f'\nMonstros ---> {Monstro.monsters}\n')

    def mostrar_atributos(self):
        for personagem in range(len(Personagem.characters)):
            print(f'Procurando por atributos de {self.name}...')
            if Personagem.characters[personagem]["Nome"] == self.name:
                self.health_points = Personagem.characters[personagem]["HP"]
                print(f'{self.name} tem {self.health_points} ponto(s) de saúde e {self.attack_points} ponto(s) de ataque.\n')
                break
            else: 
                print(f'{self.name} não foi encontrado no jogo.')
                break                



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
    
    def excluir_personagem(self, deleted):
        for personagem in Personagem.characters:
            if personagem["Nome"] == deleted:
                Personagem.characters.remove(personagem)
                print(f'\n{deleted} foi excluído do jogo.')
                return
        print(f'\n{deleted} não foi encontrado como "PERSONAGEM" no jogo.')



class Monstro(SerVivo):
    monsters : list[dict[str, object]] = []

    def __init__(self, name, healt_points, attack_points):
        super().__init__(name, healt_points, attack_points)

    def mostrar_monstros(self):
        print(f'\n{self.name} solicitou: \nMonstros ---> {Monstro.monsters}\n')

    def excluir_monstro(self, name):
        for monstro in Monstro.monsters:
            if monstro["Nome"] == name:
                Monstro.monsters.remove(monstro)
                print(f'\n{name} foi excluído do jogo.')
                return
        print(f'\n{name} não foi encontrado como "MONSTRO" no jogo.')

    def atacar(self, target):
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
            print(f'\n[ERRO] Não existe nenhum "PERSONAGEM" com o nome "{self.target}". Tente novamente.\n')
                    

class Lobo(Monstro):
    def __init__(self, name, healt_points, attack_points, power_points):
        super().__init__(name, healt_points, attack_points)
        self.name = name
        self.power_points = power_points
        self.monsters.append({"Classe": "Monstro",
                              "Espécie": "Lobo",
                              "Nome": self.name, 
                              "HP": self.health_points, 
                              "AP": self.attack_points,
                              "PP": power_points})
        print(f'{name} foi adicionado ao jogo como "LOBO".\n')


class Goblin(Monstro):
    def __init__(self, name, healt_points, attack_points, intelligence_points):
        super().__init__(name, healt_points, attack_points)
        self.name = name
        self.intelligence_points = intelligence_points
        self.monsters.append({"Classe": "Goblin",
                              "Espécie": "Lobo",
                              "Nome": self.name, 
                              "HP": self.health_points, 
                              "AP": self.attack_points,
                              "IP": intelligence_points})
        print(f'{name} foi adicionado ao jogo como "GOBLIN".\n')

