class Viagem: 
    def __init__(self, destino, distancia, litros): 
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)
    def set_destino(self, d):
        if len(d) > 0: self.__destino = d
        else: raise ValueError
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d 
        else: raise ValueError
    def set_litros(self, l):
        if l >= 0: self.__litros = l 
        else: raise ValueError
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros
    def __str__(self):
        return f'O consumo foi: {self.get_distancia():.2f} / {self.get_litros():.2f} = {self.consumo():.2f}'
class Pais: 
    def __init__(self, nome, populacao,area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_populacao(self, p):
        if p > 0: self.__populacao = p
        else: raise ValueError
    def set_area(self, a):
        if a > 0: self.__area = a
        else: raise ValueError
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao / self.__area
    def __str__(self):
        return f'{self.get_populacao():.2f}hab / {self.get_area()}Km = {self.densidade():.2f}'
    
class UI:
    @staticmethod
    def main():
        while True:
            op = UI.menu()
            if op == 1: UI.calculo()
            elif op == 2: UI.pais()
            else: break
    @staticmethod
    def menu():
        escolha = int(input('Digite sua escolha: \n[1] Calcular a Viagem \n[2] Calcular densidade demográfica \n[3] Fim \n'))
        return escolha
    @staticmethod
    def calculo():
        destino = input('Digite o destino da sua viagem: ').strip()
        distancia = float(input('Digite a distancia da sua viagem: '))
        litro = float(input('Digite a quantidade de litros: '))
        v = Viagem(destino, distancia, litro)
        print(v)
    @staticmethod
    def pais():
        nome = input('Digite o nome do País: \n')
        populacao = int(input('Digite a quantidade de habitantes: \n'))
        area = float(input('Digite a área em Km²: \n'))
        p = Pais(nome, populacao, area)
        print(p)
UI.main()