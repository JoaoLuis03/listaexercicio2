class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

# Exemplo de uso da classe:
aluno = Aluno("João", [7.5, 8.0])

media = aluno.calcular_media()
print(f"A média das notas de {aluno.nome} é {media}")

