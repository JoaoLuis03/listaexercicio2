class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Oi, meu nome é {self.nome}.")
pessoa = Pessoa("Joao", 19)
pessoa.falar()