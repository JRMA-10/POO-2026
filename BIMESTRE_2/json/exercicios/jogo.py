from enum import Enum 
from datetime import datetime
import json

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
    def set_nasc(self, nasc): 
        if nasc > datetime.now(): raise ValueError
        self.__nasc = nasc