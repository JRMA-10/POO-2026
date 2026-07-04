from random import randint
class Bingo:
    def __init__(self, numBolas):
        self.set_numero_de_bolas(numBolas)
        self.bolas = []
        self.lista = []
    def set_numBolas(self, n):
        if n >= 1: self.__numBolas = n
        else: raise ValueError
    def get_numBolas(self):
        return self.__numBolas
    @classmethod
    def sortear(self):
        self.lista = [n for n in range(1, self.get_numBolas())]
        num = randint(0, len(self.lista))
        print(self.lista[num])
        self.bolas.append(self.lista[num])
        self.lista.pop(num)
    @classmethod
    def get_last(self):
        return self.bolas[-1]
    @classmethod
    def sorteados(self, cls):
        return cls.bolas

class BingoUI:
    aqui = object
    def main():
        escolha = 0
        while escolha != 4:
            escolha = BingoUI.menu()
            if escolha == 1: BingoUI.iniciarJogo()
            elif escolha == 2: BingoUI.sortear()
            elif escolha == 3: BingoUI.sorteados()
            else: escolha = 4
    def menu():
        #iniciar jogo, sortear um número, verificar os números sorteados e sair
        print('[1] INICIAR JOGO \n[2] SORTEAR UM NÚMERO \n[3] VERIFICAR OS NÚMEROS SORTEADOS \n[4] SAIR')
        s = input('Sua escolha: \n')
        return s
    @classmethod
    def iniciarJogo(cls):
        numero_de_bolas = int(input('Informe o número de bolas: \n'))
        obj = Bingo(numero_de_bolas)
        cls.aqui = obj
    @classmethod
    def sortear(cls):
        cls.aqui.sortear()
    @classmethod
    def sorteados(cls):
        #mostra os números sorteados até o momento 
        print(cls.aqui.sorteados())

BingoUI.main()