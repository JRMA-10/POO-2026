class Retangulo:
    def __init__(self): 
        self.__base = 0
        self.__altura = 0
    def set_base(self, valor):
        if valor < 0: raise ValueError('Valor deve ser maior que 0!') #pra dar um erro e aparecer essa mensagem
        self.__base = valor
    def set_altura(self, valor):
        if valor < 0: raise ValueError('Valor deve ser maior que 0!')
        self.__altura = valor
    def get_base(self): 
        return self.__base
    def get_altura(self):
        return self.__altura
    def diagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** (0.5)


class UI:
    def main():
        x = Retangulo()
        x.set_base(float(input('Digite algo: ')))
        x.set_altura(float(input('Digite outro valor: ')))
        print(f'O retangulo de base {x.get_base():.2f} e altura {x.get_altura():.2f} tem o valor da diagonal sendo: {x.diagonal():.2f}')

UI.main() #chama a funcao main 