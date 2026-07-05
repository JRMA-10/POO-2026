from enum import Enum 
from datetime import datetime
import json
from pathlib import Path

class Grupo(Enum): A, B, C, D, E, F, G, H, I, J, K, L = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
class Fase(Enum): GRUPOS, DEZESSEISAVOS, OITAVAS, QUARTAS, SEMIS, FINAL = 1, 2, 3, 4, 5, 6

class Pais: 
    def __init__(self, id, nome, sigla, grupo): 
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)
    def set_id(self, id): 
        if id < 0: raise ValueError
        self.__id = id
    def set_nome(self, n): 
        if len(n) < 1: raise ValueError
        self.__nome = n
    def set_sigla(self, s): 
        if len(s) > 3: raise ValueError
        self.__sigla = s
    def set_fone(self, f): 
        if len(f) < 7: raise ValueError
        self.__fone = f
    def set_grupo(self, g):
        self.__grupo = g
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_sigla(self): return self.__sigla
    def get_grupo(self): return self.__grupo
    def to_json(self): return {"id" : self.__id, "nome" : self.__nome, "sigla" : self.__sigla, "grupo" : self.get_grupo().name}
    
    @staticmethod
    def from_json(dic): return Pais(dic["id"], dic["nome"], dic["sigla"], dic["grupo"])

    def __str__(self): return f'ID: {self.__id} | NOME: {self.__nome} | SIGLA: {self.__sigla} | GRUPO: {self.get_grupo().name}'

class Jogos:
    def __init__(self, id, id_1, id_2, gols_1, gols_2, fase, hora):
        self.set_id(id)
        self.set_id_1(id_1)
        self.set_id_2(id_2)
        self.set_gols_1(gols_1)
        self.set_gols_2(gols_2)
        self.set_fase(fase)
        self.set_hora(hora)
    def set_id(self, id):
        if id < 0: raise ValueError
        self.__id = id
    def set_id_1(self, i):
        if i < 0: raise ValueError
        self.__id_1 = i
    def set_id_2(self, i):
        if i < 0: raise ValueError
        self.__id_2 = i
    def set_gols_1(self, g):
        if g < 0: raise ValueError
        self.__gols_1 = g
    def set_gols_2(self, g):
        if g < 0: raise ValueError
        self.__gols_2 = g
    def set_fase(self, f):
        self.__fase = f
    def set_hora(self, h):
        self.__hora = h
    def get_id(self): return self.__id
    def get_id_1(self): return self.__id_1
    def get_id_2(self): return self.__id_2
    def get_gols_1(self): return self.__gols_1
    def get_gols_2(self): return self.__gols_2
    def get_fase(self): return self.__fase
    def get_hora(self): return self.__hora

    def to_json(self): return {'id' : self.__id, 'time1' : self.__id_1, 'time2' : self.__id_2, 'gols1' : self.__gols_1, 'gols2' : self.__gols_2, 'fase' : self.get_fase().name, 'hora' : self.get_hora().strftime("%d/%m/%Y")}
    
    @staticmethod
    def from_json(dic): return Jogos(dic['id'], dic['time1'], dic['time2'], dic['gols1'], dic['gols2'], dic['fase'], dic['hora'])
    
    def __str__(self): return f'ID: {self.__id} | TIME 1: {self.__id_1} | TIME 2: {self.__id_2} | GOLS 1: {self.__gols_1} | GOLS 2: {self.__gols_2} | FASE: {self.get_fase().name} | HORA: {self.get_hora().strftime("%d/%m/%Y")}'

class UI: 
    __lista_de_paises = []
    __lista_de_jogos = []
    __paises_json = Path(__file__).resolve().parent / "paises.json"
    __jogos_json = Path(__file__).resolve().parent / "jogos.json"
    def main(): 
        escolha = 0 
        while escolha != 11: 
            escolha = UI.menu()
            match escolha: 
                case 1: UI.inserir_pais()
                case 2: UI.inserir_jogos()
                case 3: UI.listar_paises()
                case 4: UI.listar_jogos()
                case 5: UI.atualizar_pais()
                case 6: UI.atualizar_jogos()
                case 7: UI.excluir_pais()
                case 8: UI.excluir_jogos()
                case 9: UI.pesquisar_pais()
                case 10: UI.pesquisar_jogos
    def menu():
        print(' [1] INSERIR PAIS \n [2] INSERIR JOGO \n [3] LISTAR PAÍSES \n [4] LISTAR JOGOS \n [5] ATUALIZAR PAÍS \n [6] ATUALIZAR JOGO \n [7] EXCLUIR PAÍS \n [8] EXCLUIR JOGO \n [9] PESQUISAR POR TIME \n [10] PESQUISAR POR JOGO \n [11] SAIR')
        return int(input('Informe a sua escolha: '))
    @classmethod
    def inserir_pais(cls):
        id = int(input('Informe o id do País: \n'))
        nome = input('Informe o nome do País: \n')
        sigla = input('Informe a sigla do País: \n')
        grupo = Grupo(int(input('Informe o grupo: \n')))
        P = Pais(id, nome, sigla, grupo)
        cls.__lista_de_paises.append(P)
        UI.salvar_paises()
    @classmethod
    def inserir_jogos(cls): 
        id = int(input('Informe o ID do jogo: \n'))
        id1 = int(input('Informe o ID do primeiro time: \n'))
        id2 = int(input('Informe o ID do segundo time: \n'))
        gols1 = int(input('Informe a quantidade de gols do primeiro Time: \n'))
        gols2 = int(input('Informe a quantidade de gols do segundo time: \n'))
        fase = Fase(int(input('Informe a fase do jogo: \n')))
        hora = datetime.strptime(input('Informe a data do jogo: '), "%d/%m/%Y")
        J = Jogos(id, id1, id2, gols1, gols2, fase, hora)
        cls.__lista_de_jogos.append(J)
        UI.salvar_jogos()
    @classmethod
    def listar_paises(cls):
        if len(cls.__lista_de_paises) == 0: UI.abrir_paises()
        for i in cls.__lista_de_paises: print(i)
    @classmethod
    def listar_jogos(cls): 
        if len(cls.__lista_de_jogos) == 0: UI.abrir_jogos()
        for i in cls.__lista_de_jogos: print(i)
    def atualizar_pais(): 
        pass
    def atualizar_jogos():
        pass
    def excluir_pais(): 
        pass
    def excluir_jogos(): 
        pass
    def pesquisar_pais():
        pass
    def pesquisar_jogos(): # Por fases 
        pass

    @classmethod
    def abrir_paises(cls): 
        try: 
            arquivo = open(cls.__paises_json, mode = 'r')
            lista_dicionario = json.load(arquivo)
            arquivo.close()
            for dicionario in lista_dicionario: 
                x = Pais.from_json(dicionario)
                cls.__lista_de_paises.append(x)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar_paises(cls):
        arquivo = open(cls.__paises_json, mode = 'w')
        json.dump(cls.__lista_de_paises, arquivo, default = Pais.to_json, indent = 2)
        arquivo.close()

    @classmethod
    def abrir_jogos(cls): 
        try: 
            arquivo = open(cls.__jogos_json, mode = 'r')
            lista_dicionario = json.load(arquivo)
            arquivo.close()
            for dicionario in lista_dicionario: 
                x = Jogos.from_json(dicionario)
                cls.__lista_de_jogos.append(x)
        except FileNotFoundError: 
            pass

    @classmethod
    def salvar_jogos(cls):
        arquivo = open(cls.__jogos_json, mode = 'w')
        json.dump(cls.__lista_de_jogos, arquivo, default = Jogos.to_json, indent = 2)
        arquivo.close()

UI.main()