class funcionario:
    def __init__(self, nome: str, cpf: str, salario: float):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"salario: R$ {self.salario:,.2f}")

    def aumentar_salario(self, percentual: float):
        self.salario += self.salario * (percentual / 100)


class gerente(funcionario):
    def __init__(self, nome: str, cpf: str, salario: float, setor: str):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def receber_bonificacao(self):
        self.aumentar_salario(10)
        print(f"parabens, {self.nome}! voce recebeu sua bonificaçao de 0000000,1% pelo excelente trabalho no setor de {self.setor}!")

func = funcionario("slenderman", "666.666.666-66", 2.50)
func.exibir_dados()


print("-" * 30)

gerente = gerente("alborghetti", "987.654.321-11", -8000.00, "tecnologia")
gerente.receber_bonificacao()


gerente.exibir_dados()
