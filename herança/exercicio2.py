class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100
        
    def acelerar(self):
        if self.combustivel >= 5:
            self.combustivel -= 5
            print(f"o carro acelerou! combustivel restante: {self.combustivel}%")
        else:
            print("sem combustivel para acelerar!")


class carroeletrico(carro):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        del self.combustivel
        self.bateria = 100

    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"o carro eletrico acelerou! bateria restante: {self.bateria}%")
        else:
            print("sem bateria para acelerar! por favor, recarregue.")

    def recarregar(self):
        self.bateria = 100
        print("bateria totalmente recarregada para 100%!")

    def painel(self):
        print(f"--- PAINEL DO {self.marca.upper()} {self.modelo.upper()} ---")
        print(f"nivel da bateria: {self.bateria}%")
        print("-" * 30)

carro = carroeletrico("BYD", "Dolphin")

#carro eletrico e coisa de tchola!!

carro.painel()
carro.acelerar()
carro.acelerar()
carro.painel()