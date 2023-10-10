class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
retangulo1 = Retangulo(2, 4)
area1 = retangulo1.calcular_area()
print(f"A área do retângulo é: {area1}")
