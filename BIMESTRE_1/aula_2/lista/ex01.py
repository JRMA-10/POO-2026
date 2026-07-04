class Circulo:
    def __init__(self, raio):
        self.raio = raio
    def operacao(self):
        return 3.14 * (self.raio ** 2)

c1 = Circulo(3)
print(c1.operacao())