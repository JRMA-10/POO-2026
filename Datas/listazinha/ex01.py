from datetime import datetime, timedelta #módulo

class Treino: 
    def __init__(self, id, data_do_treino, distancia_percorrida, tempo_da_corrida): 
        self.set_id(id)
        self.set_data_do_treino(data_do_treino)
        self.set_distancia_percorrida(distancia_percorrida)
        self.set_tempo_da_corrida(tempo_da_corrida)
    def set_id(self, id): 
        if id >= 0: self.__id = id
        else: raise ValueError('ID inválido!')
    def set_data_do_treino(self, dt): 
        if dt < datetime.now(): self.__dataTreino = dt
        else: raise ValueError('Data inválida!')
    def set_distancia_percorrida(self, dp):
        if dp > 0: self.__distancia_percorrida = dp
        else: raise ValueError('Distancia inválida')
    def set_tempo_da_corrida(self, tc):
        self.__tempo_da_corrida = tc
    def get_id(self): return self.__id
    def get_data_do_treino(self): return self.__dataTreino
    def get_distancia_percorrida(self): return self.__distancia_percorrida
    def get_tempo_da_corrida(self): return self.__tempo_da_corrida
    def pace(self):
        segundos = (self.get_tempo_da_corrida().total_seconds()) / 60
        return segundos / self.get_distancia_percorrida()
    def __str__(self):
        return f'ID: {self.get_id()} | DATA DO TREINO: {datetime.strftime(self.get_data_do_treino(), '%d/%m/%Y')} | DISTÂNCIA PERCORRIDA: {self.get_distancia_percorrida()} | TEMPO DA CORRIDA: {self.get_tempo_da_corrida()} | Pace: {self.pace():.2f}'
    
class TreinoUI: 
    treinos = []
    def main():
        escolha = 0
        while escolha != 7: 
            escolha = TreinoUI.menu()
            match escolha: 
                case 1: TreinoUI.inserir()
                case 2: TreinoUI.listar()
                case 3: TreinoUI.listar_id()
                case 4: TreinoUI.atualizar()
                case 5: TreinoUI.excluir()
                case 6: TreinoUI.mais_rapido()
    def menu(): 
        print('[1] INSERIR \n[2] LISTAR \n[3] LISTAR_ID \n[4] ATUALIZAR \n[5] EXCLUIR \n[6] MAIS_RÁPIDO \n[7] SAIR')
        return int(input('Faça a sua escolha: '))
    @classmethod
    def inserir(cls):
        id = int(input('Informe o ID: \n'))
        data_do_evento = datetime.strptime(input("Informe a data do evento: \n"), '%d/%m/%Y')
        distancia_percorrida = float(input('Informe a distancia percorrida: \n'))
        tempo_da_corrida = timedelta(hours = int(input('Informe as horas: \n')), minutes = int(input('Informe os minutos: \n')), seconds = int(input('Informe os segundos: \n')))
        t = Treino(id, data_do_evento, distancia_percorrida, tempo_da_corrida)
        cls.treinos.append(t)
    @classmethod
    def listar(cls): 
        for i in cls.treinos: print(i)
    @classmethod
    def listar_id(cls): 
        id = int(input('Informe o id do treino que você deseja: '))
        for i in cls.treinos: 
            if i.get_id() == id: print(i)
    @classmethod
    def atualizar(cls):
        TreinoUI.listar()
        id = int(input('Informe o ID do treino para alteração: '))
        for i in cls.treinos: 
            if i.get_id() == id: 
                i.set_data_do_evento(datetime.strptime(input("'Informe a data do evento: \n"), '%d/%m/%Y'))
                i.set_distancia_percorrida(float(input('Informe a distancia percorrida: \n')))
                i.set_tempo_de_corrida(timedelta(hours = int(input('Informe as horas: \n')), minutes = int(input('Informe os minutos: \n')), seconds = int(input('Informe os segundos: \n'))))
    @classmethod
    def excluir(cls):
        TreinoUI.listar()
        id = int(input('Informe o ID para a exclusão: '))
        for i in cls.treinos: 
            if i.get_id() == id: 
                cls.treinos.remove(i)
    @classmethod
    def mais_rapido(cls):
        lista_paces = sorted(filter(lambda x: x.pace(), cls.treinos), key = lambda x: x.pace())
        print(f'Seu melhor treino foi: {lista_paces[0]}')
TreinoUI.main()