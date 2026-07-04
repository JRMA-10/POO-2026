class Times:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_estado(self, e):
        if len(e) > 0: self.__estado = e
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def __str__(self):
        return f'ID: {self.get_id()} | NOME: {self.get_nome()} | ESTADO: {self.get_estado()}'

class Jogadores:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_idTime(self, it):
        if it >= 0: self.__it = it
        else: raise ValueError
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_camisa(self, c):
        if c >= 0: self.__camisa = c
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_it(self):
        return self.__it
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def __str__(self): 
        return f'ID : {self.get_id()} | IdTime : {self.get_it()} | Nome : {self.get_nome()} | Camisa : {self.get_camisa()}'
    
class UI():
    lista_de_times = []
    lista_de_jogadores = []
    def main():
        escolha = 0
        while escolha != 11:
            escolha = UI.menu()
            match escolha:
                case 1: UI.inserir_time()
                case 2: UI.listar_time()
                case 3: UI.atualizar_time()
                case 4: UI.excluir_time()
                case 5: UI.inserir_jogador()
                case 6: UI.listar_jogador()
                case 7: UI.atualizar_jogador()
                case 8: UI.excluir_jogador()
                case 9: UI.listar_jogadores_do_time()
                case 10: UI.transferir_jogador()
    def menu():
        print('[1] INSERIR TIMES\n[2] LISTAR TIMES \n[3] ATUALIZAR TIMES \n[4] EXCLUIR TIMES \n[5] INSERIR JOGADOR \n[6] LISTAR JOGADORES \n[7] ATUALIZAR JOGADORES \n[8] EXCLUIR JOGADOR \n[9] LISTAR JOGADORES DE UM TIME \n[10] TRANFERIR JOGADOR \n[11] SAIR')
        u = int(input('Informe a sua escolha: \n'))
        return u
    @classmethod
    def inserir_time(cls):
        id = int(input('Informe o ID do time: '))
        nome = input('Informe o nome do Time: ').strip()
        estado = input('Informe o nome do Estado do time: ')
        time = Times(id, nome, estado)
        for i in cls.lista_de_times:
            if i.get_id() == id or i.get_nome() == nome: print('Não foi possível adicionar o TIME!')
            return
        cls.lista_de_times.append(time)
    @classmethod
    def listar_time(cls):
        for i in cls.lista_de_times: print(i)
    @classmethod
    def atualizar_time(cls):
        UI.listar_time()
        id = int(input('Informe o ID do time que você deseja fazer a alteração: '))
        for i in cls.lista_de_times: 
            if i.get_id() == id: 
                i.set_nome(input('Informe o novo nome: '))
                i.set_estado(input('Informe o novo nome do Estado: '))
    @classmethod
    def excluir_time(cls):
        UI.listar_time()
        id = int(input('Informe o ID do time que você deseja excluir: '))
        for i in cls.lista_de_times:
            if i.get_id() == id: cls.lista_de_times.remove(i)
    @classmethod
    def inserir_jogador(cls): 
        id = int(input('Informe o ID do Jogador: '))
        it = int(input('Informe o ID do seu time: '))
        nome = input('Informe o nome do jogador: ').strip()
        camisa = int(input('Informe o número da camisa do seu jogador: '))
        jogadores = Jogadores(id, it, nome, camisa)
        for i in cls.lista_de_jogadores:
            if i.get_id() == id or i.get_nome() == nome: print('Não foi possível adicionar o Jogador!')
            return
        cls.lista_de_jogadores.append(jogadores)
    @classmethod
    def listar_jogador(cls):
        for jogador in cls.lista_de_jogadores: print(jogador)
    @classmethod
    def atualizar_jogador(cls):
        UI.listar_jogador()
        id = int(input('Informe o ID do JOGADOR que você deseja fazer a alteração: '))
        for i in cls.lista_de_jogadores: 
            if i.get_id() == id: 
                i.set_nome(input('Informe o novo nome: '))
                i.set_camisa(int(input('Informe o seu nove número: ')))
    @classmethod
    def excluir_jogador(cls):
        UI.listar_jogador()
        nome = input('Informe as primeiras letras do nome do seu jogador: ')
        for i in cls.lista_de_jogadores:
            if i.get_nome().startswith(nome):
                cls.lista_de_jogadores.remove(i)
    @classmethod
    def listar_jogadores_do_time(cls):
        id_do_time = int(input('Informe o ID do Time que você deseja ver os jogadores: '))
        for i in cls.lista_de_jogadores:
            if i.get_it() == id_do_time:
                print(i)
    @classmethod
    def transferir_jogador(cls):
        UI.listar_jogador()
        jogador = int(input('Informe o ID do jogador que você deseja alterar o time: '))
        UI.listar_time()
        novo_time = int(input('Informe o ID do time que você vai transferi-lo: '))
        for i in cls.lista_de_jogadores: 
            if i.get_id() == jogador:
                i.set_idTime(novo_time)
UI.main()