class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = (percentual / 100) * self.salario
            self.salario += aumento
            return f"O salário de {self.nome} foi aumentado em {percentual}% e agora é R${self.salario:.2f}."
        else:
            return "O percentual de aumento deve ser maior que zero."
funcionario = Funcionario("Joao", 5000, "programador")
print(funcionario.aumentar_salario(10))
