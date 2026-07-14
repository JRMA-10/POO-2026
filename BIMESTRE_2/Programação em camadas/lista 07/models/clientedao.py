# DAO = DATA ACCESS OBJECT
from models.cliente import Cliente
from pathlib import Path
import json

class ClienteDAO: 
    def __init__(self): 
        self.__arquivo = Path(__file__).resolve().parent / "clientes.json"
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj):
        id = 0
        for objeto in self.__objetos: 
            if objeto.get_id() > id: id = objeto.get_id()
            objeto.set_id(id + 1)
        self.__objetos.append(obj)
        self.__salvar()
    def listar(self): return self.__objetos
    def listar_id(self, id): 
        for obj in self.__objetos: 
            if obj.get_id() == id: return obj
        return None
    def atualizar(self, obj): 
        aux = self.listar_id(self.get_id())
        if aux != None: 
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()
    def excluir(self, id): 
        aux = self.listar_id(id)
        if aux != None: 
            self.__objetos.remove(aux)
            self.__salvar()
    def listar_nome(self, iniciais):
        for i in self.__objetos: 
            if i.get_nome().lower().startswith(iniciais.lower()): return i; return None
    def __abrir(self): 
        try: 
            arquivo = open(self.__arquivo, mode = 'r')
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = [] # Reseta a lista
            for dic in list_dic: 
                obj = Cliente.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError: 
            pass
    def __salvar(self): 
        arquivo = open(self.__arquivo, mode = 'w')
        json.dump(self.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()
