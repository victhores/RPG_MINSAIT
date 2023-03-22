class Bicho:
    def __init__(self, peso):
        self.peso = peso

class Animal(Bicho):
    def __init__(self, peso, nome):
        super().__init__(peso)
        self.nome = nome

    def fazer_barulho(self):
        print("Fez barulho genérico")

class Cachorro(Animal):
    def fazer_barulho(self):
        print("Au au!")

class Gato(Animal):
    def fazer_barulho(self):
        print("Miau!")

class Ave(Animal):
    def __init__(self, tem_asa):
        super().__init__()

    def fazer_barulho(self):
        super().fazer_barulho()


animal_generico = Animal(nome="Cavalo")
animal_generico.fazer_barulho()

cachorro_bob = Cachorro(nome='Bob', peso=15)
cachorro_bob.fazer_barulho()

gato_mike = Gato(nome="Mike", peso=15)
gato_mike.fazer_barulho()

ave_piu = Ave(Animal)