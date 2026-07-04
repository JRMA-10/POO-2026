class Circulo:
    def __init__(self):
        self.__raio = 0
    def set_raio(self, r):
        if r >= 0: self.__raio = r
        else: raise ValueError
    def get_raio(self):
        return self.__raio
    def calcular_comprimento(self):
        return (6,28 * self.__raio)
    def calcular_area(self):
        return 3,14 * (self.__raio ** 2)

class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d
        else: raise ValueError
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t
        else: raise ValueError
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo

class Conta_bancaria:
    def __init__(self):
        self.__titular = ' '
        self.__numero_da_conta = 0
        self.__saldo = 0
    def set_titular(self, nome):
        if len(nome) > 0: self.__titular = nome
        else: raise ValueError
    def set_numero_da_conta(self, numero):
        if numero > 0: self.__numero_da_conta = numero
        else: raise ValueError
    def set_saldo(self, saldo):
        self.__saldo = saldo
    def get_titular(self):
        return self.__titular
    def get_numero(self):
        return self.__numero_da_conta
    def get_saldo(self):
        return self.__saldo
    def deposito(self):
        deposito = float('Digite o valor para o deposito: \n')
        if deposito <= 0: raise ValueError
        else: self.__saldo += deposito
    def saque(self):
        saque = float(input('Digite o valor para o saque: \n'))
        if saque <= 0: raise ValueError
        else: 
            self.__saldo -= saque
            return saque

class Cinema():
    def __init__(self):
        self.__dia = 0
        self.__horario = 0
    def set_dia(self, dia):
        if 1 <= dia <= 7: self.__dia = dia
        else: raise ValueError
    def set_horario(self, horario):
        if 0 <= horario <= 24: self.__horario = horario
        else: raise ValueError
    def get_dia(self):
        return self.__dia
    def get_horario(self):
        return self.__horario
    def condicoes(self):
        valor_do_ingresso = 16
        if self.__dia == 6 or self.__dia == 7 or self.__dia == 1:
            valor_do_ingresso = 20
        elif self.__dia == 4:
            valor_do_ingresso /= 2
        if 17 <= self.__horario <= 24:
            valor_do_ingresso += (valor_do_ingresso / 2)
        return valor_do_ingresso

class UI():
    @staticmethod
    def viagem():
        v = Viagem()
        v.set_distancia(float(input('Digite a distância: ')))
        tempo = input('Digite o tempo em horas e minutos: (ex: 17:45)')
        pos = tempo.find(':')
        horas = tempo[:pos]
        minutos = int(int(tempo[pos + 1:]) / 6)
        completo = float(f'{horas}.{minutos}')
        v.set_tempo(completo)
        print(f'A velocidade média foi: {v.get_distancia()}Km / {v.get_tempo()}h = {v.velocidade_media():.2f}Km/h')
    @staticmethod
    def conta_bancaria():
        conta = Conta_bancaria()
        conta.set_titular(input('Digite seu nome: '))
        conta.set_numero_da_conta(int(input('Digite o número da conta: ')))
        conta.set_saldo(float(input('Digite o seu saldo: ')))
        saque = conta.saque()
        print(f'O titular: {conta.get_titular()}, fez um saque de R$ {saque} e seu saldo agora é: R$ {conta.get_saldo()}')
    
    @staticmethod
    def cinema():
        dias = {
            1: 'Domingo', 
            2: 'Segunda', 
            3: 'Terça', 
            4: 'Quarta', 
            5: 'Quinta', 
            6: 'Sexta', 
            7: 'Sábado'
        }
        cinema = Cinema()
        cinema.set_dia(int(input('''
[1] = Domingo
[2] = Segunda 
[3] = Terça
[4] = Quarta
[5] = Quinta
[6] = Sexta
[7] = Sábado
Digite o dia em que você vai ao cinema: 
''')))
        tempo = input('Digite o tempo em horas e minutos: (ex: 09:45)').strip()
        pos = tempo.find(':')
        horas = tempo[:pos]
        minutos = int(int(tempo[pos + 1:]) / 6)
        completo = float(f'{horas}.{minutos}')
        cinema.set_horario(completo)
        print(f'Se você for no(a) {dias[cinema.get_dia()]} às {tempo}h, você pagará R$ {cinema.condicoes():.2f}')
UI.cinema()
