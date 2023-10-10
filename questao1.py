import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2
raio_circulo = 3
circulo = Circulo(raio_circulo)
area = circulo.calcular_area()
print(f"A área do círculo é: {area}")