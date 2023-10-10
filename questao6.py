class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto = Produto("Tenis", 300.0, 2)
total = produto.calcular_total()
print(f"O total para o {produto.nome} é R${total}")
