class itembiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            print(f"o item '{self.titulo}' ja esta emprestado")

    def devolver(self):
        self.disponivel = True


class Livro(itembiblioteca):
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas


class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item: itembiblioteca):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"'{item.titulo}' foi emprestado para {self.nome}.")
        else:
            print(f"desculpe, '{item.titulo}' nao tem no momento.")

    def devolver_item(self, item: itembiblioteca):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"'{item.titulo}' foi devolvido por {self.nome}.")
        else:
            print(f"O usuario {self.nome} no momento nao possui o livro '{item.titulo}'.")

    def ver_historico(self):
        print(f"\nusuario: {self.nome}")
        if not self.itens_emprestados:
            print("nenhum item em posse no momento.")
        else:
            print("itens atualmente em posse:")
            for item in self.itens_emprestados:
                print(f"- {item.titulo}")


meu_livro = Livro("michael de santa e sua familha", 101, "simeon", 444)
usuario = Usuario("gameseduuu")

usuario.ver_historico()

usuario.pegar_item(meu_livro)

usuario.ver_historico()

usuario.pegar_item(meu_livro)

usuario.devolver_item(meu_livro)
