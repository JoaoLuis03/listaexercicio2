class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Frankenstein", "Mary Shelley")

print(livro1.detalhes())
print(livro2.detalhes())