class Retangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.__area = 0
        self.__diagonal = 0
    def area(self): 
        self.__area = self.base * self.altura
        return self.__area
    def diagonal(self): 
        #h² = base² + altura²
        self.__diagonal = (self.base ** 2 + self.altura ** 2) ** (1/2)
        return self.__diagonal
    def __str__(self): 
        return f'Base: {self.base} \nAltura: {self.altura} \nÁrea: {self.area():.2f} \nDiagonal: {self.diagonal():.2f}'