class cofredigital:
    def __init__(self, titular: str, senha: str):
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0.0

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            print(f"deposito de R$ {valor:.2f} deu certo!")
        else:
            print("o valor do deposito tem que ser positivo(voce e burro?)")

    def sacar(self, valor: float, senha_informada: str):
        if senha_informada != self.__senha:
            print("senha errada! voce nao pode entrar aqui")
            return

        if valor <= 0:
            print("o valor do saque tem que positivo(voce e burro?)")
            return

        if valor > self.__saldo:
            print("voce nao tem dinheiro para sacar kkkk")
            return

        self.__saldo -= valor
        print(f"saque de R$ {valor:.2f} deu certo! agora some daqui")

uou1 = cofredigital("nugget", "frango")

valor = float(input("Valor: "))
uou1.depositar(valor)
valor = float(input("Valor: "))
senha = input("Senha: ")
uou1.sacar(valor,senha)