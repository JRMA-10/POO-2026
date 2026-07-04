#Métodos mágicos; 
from multiprocessing.sharedctypes import Value

class Retangulo: 
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, b):
        if b >= 0: self.__b = b
        else: raise ValueError
    def set_altura(self, h):
        if h >= 0: self.__h = h
        else: raise ValueError
    def get_base(self):
        return self.__b
    def get_altura(self): 
        return self.__h
    def calcArea(self):
        return self.__b * self.__h
    def calcDiagonal(self):
        #h² = b² + c²
        return (self.__b ** 2 + self.__h ** 2) * (1/2)
    def __str__(self):
        return f'Eu sou um retangulo e minha área é {self.calcArea()} e minha diagonal é {self.calcDiagonal}'

class Frete:
    def __init__(self, d, p):
        self.set_distancia(d)
        self.set_peso(p)
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError
    def set_peso(self, p):
        if p >= 0: self.__peso = p
        else: raise ValueError
    def get_distancia(self):
        return self.__distancia
    def get_peso(self):
        return self.__peso
    def calcFrete(self):
        return (self.__peso * self.__distancia) / 100
    def __str__(self):
        return f'O valor a ser pago será: {self.get_peso()} / {self.get_distancia()} / 100 = R$ {self.calcFrete()}'

class Equacao:
    def __init__(self, a, b, c):
        self.set_a(a) #a precisa ser diferente de 0
        self.__b = b
        self.__c = c
    def set_a(self, a):
        if a != 0: self.__a = a
        else: raise ValueError
    def get_a(self):
        return self.__a
    def delta(self):
        #b² - 4 * a * c
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    def tem_raizes_reais(self):
        if self.delta() >= 0: return True
        else: return False
    def raiz1(self):
        return ((- self.__b) + (self.delta() ** 0.5)) / (2 * self.__a)
    def raiz2(self):
        return ((- self.__b) - (self.delta() ** 0.5)) / (2 * self.__a)
    def __str__(self):
        if self.tem_raizes_reais():
            if self.delta() == 0: 
                return f'A raiz da equação {self.__a}x² + {self.__b}x + {self.__c} é: {self.raiz1()}'
            else:
                return f'As raízes da equação {self.__a}x² + {self.__b}x + {self.__c} são: {self.raiz1()} e {self.raiz2()}'
        else: return 'A equação não tem raízes reais'
class UI:
    @staticmethod
    def main():
        print('[1] Retângulo \n[2] Frete \n[3] Equação')
        n = int(input('Sua escolha: '))
    @staticmethod
    def retangulo():
        b = float(input('Digite a Base do Retangulo: \n'))
        h = float(input('Digite a altura do Retangulo: \n'))
        x = Retangulo(b, h)
        x.calcArea()
        print(x.calcArea())
        print(x.calcDiagonal())
        print(x)
    @staticmethod
    def Frete():
        d = float(input('Digite a distância: \n'))
        p = float(input('Digite o peso: \n'))
        x = Frete(d, p)
        print(x.calcFrete())
        print(x)
    @staticmethod
    def equacao():
        a = float(input('Digite o valor de a: \n'))
        b = float(input('Digite o valor de b: \n'))
        c = float(input('Digite o valor de c: \n'))
        x = Equacao(a, b, c)
        print(x)
UI.equacao()