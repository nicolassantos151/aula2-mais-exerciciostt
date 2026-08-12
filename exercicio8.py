# ==============================================================================
# EXERCÍCIO - CLASSE PET VIRTUAL (TAMAGOTCHI)
# ==============================================================================
# Crie uma estrutura do zero para controlar as necessidades de um bichinho virtual:
#
# 1. Classe PetVirtual:
#    - Atributos (__init__): nome (str), fome (int, iniciando em 5) e felicidade (int, iniciando em 5).
#    - Método alimentar(self):
#      * Se a fome for maior que 0, diminui a fome em 2 e exibe:
#        "[nome] foi alimentado! Fome atual: X"
#      * Se a fome já for 0, exibe: "[nome] já está de barriga cheia!"
#    - Método brincar(self):
#      * Aumenta a felicidade em 2 e aumenta a fome em 1.
#      * Exibe: "Você brincou com [nome]! Felicidade: X | Fome: Y"
#    - Método status(self):
#      * Exibe o nome do pet, a fome atual e a felicidade.
#      * Se a fome for maior ou igual a 8, exibe um alerta: "Atenção: [nome] precisa comer!"
#
# 2. Teste no Código:
#    - Instancie um pet virtual: meu_pet = PetVirtual("Pou")
#    - Chame o método status().
#    - Chame o método brincar() 2 vezes.
#    - Chame o método alimentar() 3 vezes.
#    - Chame o método status() novamente para conferir o resultado final.
# ==============================================================================

import random


class PetVirtual:
    def __init__(self, nome, fome=5, felicidade=10):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade

    def diminuir_felicidade_aleatoria(self):
        perda = random.randint(0, 2)
        self.felicidade -= perda
        self.felicidade = max(self.felicidade, 0)

    def alimentar(self):
        self.diminuir_felicidade_aleatoria()
        if self.fome > 0:
            self.fome -= 2
            self.fome = max(self.fome, 0)
            print(f"[{self.nome}] fome: {self.fome}")
        else:
            print("ele vai explodir de tanto comer")
            print(f"[{self.nome}] fome: {self.fome}")

    def brincar(self):
        self.diminuir_felicidade_aleatoria()
        self.felicidade += 2
        self.fome += 1
        print(f"[{self.nome}] felicidade: {self.felicidade} | fome: {self.fome}")

    def status(self):
        self.diminuir_felicidade_aleatoria()
        print(f"status - [{self.nome}] felicidade: {self.felicidade} | fome: {self.fome}")

pet = PetVirtual("rizoto")

pet.status()

pet.brincar()
pet.brincar()

pet.alimentar()
pet.alimentar()
pet.alimentar()

pet.status()