from models.servico import Servico
from pathlib import Path
import json

class ServicoDAO: 
    def __init__(self): 
        self.__arquivo = Path(__file__).resolve().parent / "servico.json"
        self.__objetos = []
        self.__abrir()
    def inserir(self, obj): #recebe um objeto para adicionar na lista
        self.__objetos.append(obj)
        self.__salvar()
    def listar(self): return self.__objetos # retorna a lista inteira
    def listar_id(self, id): # Retorna o objeto que tem o mesmo id do informado
        for obj in self.__objetos: 
            if obj.get_id() == id: return obj
        return None 
    def atualizar(self, obj): 
        aux = self.listar_id(self.get_id) #encontra esse id
        if aux != None: 
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()
    def excluir(self, id): 
        aux = self.listar_id(id)
        if aux != None: 
            self.__objetos.remove(aux)
            self.__salvar()
    def id(self): return len(self.__objetos)
    def listar_nome(self, iniciais): return [filter(lambda x: x.starswith(iniciais), self.__objetos)]
    def __abrir(self): 
        try: 
            arquivo = open(self.__arquivo, mode = 'r')
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic: 
                obj = Servico.from_json(dic)
                self.__objetos.append(obj)
        except FileExistsError: 
            pass
    def __salvar(self): 
        arquivo = open(self.__arquivo, mode = 'w')
        json.dump(self.__objetos, arquivo, default = Servico.to_json, indent = 2)
        arquivo.close()
