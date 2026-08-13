class ordemdeservico:
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente, descricao):
        ordemdeservico.total_os_criadas += 1
        ordemdeservico.os_abertas += 1
        
        self.id_os = ordemdeservico.total_os_criadas
        self.cliente = cliente
        self.descricao = descricao
        self.status = "aberta"

    def finalizar_os(self):
        self.status = "concluida"
        ordemdeservico.os_abertas -= 1

    def ler_os(self):
        print(f"Id:{self.id_os}|Cliente: {self.cliente}|Descrição: {self.descricao}|Status: {self.status}")

    def verificar_os_abertas(self):
        return ordemdeservico.os_abertas


os1 = ordemdeservico("The Rock", "Troca de tela")
os2 = ordemdeservico("Jair Bolsonaro", "Formatação HD")
os3 = ordemdeservico("Cj", "Instalação do Sistema Operacional")

os2.ler_os()

print("ordens abertas:", os1.verificar_os_abertas())

os2.finalizar_os()

os2.ler_os()

print("ordens abertas:", os1.verificar_os_abertas())