class animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"{self.nome} faz um som generico")

class cachorro (animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="canino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} (o {self.raca}) diz: au au!")


class gato(animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="felino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} (o {self.raca}) diz: miau!")


class vaca(animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="bovino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} (a vaca da raça {self.raca}) diz: muuu!")


dog = cachorro(nome="hot dog", raca="salsicha")
cat = gato(nome="sigma", raca="persa")
cow = vaca(nome="danone", raca="holandesa")

lista_de_animais = [dog, cat, cow]

print("--- DEMONSTRAÇAO DE POLIMORFISMO ---")
for animal in lista_de_animais:
    animal.fazer_som()
