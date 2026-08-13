class livro:
    def __init__(self, titulo:str, autor:str, paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"livro: '{self.titulo}' feito por {self.autor} ({self.paginas} pgs)"

    def comparar_tamanho(self, outro_livro):
        if self.paginas > outro_livro.paginas:
            print(f"'{self.titulo}' tem mais paginas que '{outro_livro.titulo}'")
        elif self.paginas < outro_livro.paginas:
            print(f"'{outro_livro.titulo}' tem mais paginas que '{self.titulo}'")
        else:
            print(f"os livros dois tem a mesma quantidade de paginas ({self.paginas} pgs)")

livro1 = livro("pou e suas aventuras", "pou", 999)
livro2 = livro("a doçe vida de trevor philips", "lester", 123)

print(livro1)
print(livro2)
        
livro1.comparar_tamanho(livro2)
