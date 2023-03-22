from Personagem import Personagem
from Monstro import Monstro

class SerVivo:
    def __init__(self, name, healt_points, attack_points):
        self.name = name
        self.health_points = healt_points
        self.attack_points = attack_points

    def mostrar_todos(self, nome_do_solicitante):
        print(f'\n{nome_do_solicitante} solicitou: \nPersonagens ---> {Personagem.characters}')
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