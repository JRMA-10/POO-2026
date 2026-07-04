from datetime import datetime
import json
from pathlib import Path

class Contato: 
    def __init__(self, id, nome, email, fone, nasc): 
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nasc(nasc)
    def set_id(self, id): 
        if id < 0: raise ValueError
        self.__id = id
    def set_nome(self, n): 
        if len(n) < 1: raise ValueError
        self.__nome = n
    def set_email(self, e): 
        if not '@' in e and len(e) < 10: raise ValueError
        self.__email = e
    def set_fone(self, f): 
        if len(f) < 7: raise ValueError
        self.__fone = f
    def set_nasc(self, nasc): 
        if nasc > datetime.now(): raise ValueError
        self.__nasc = nasc
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email (self): return self.__email 
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc
    def __str__(self): 
        return f'ID: {self.__id} | NOME: {self.__nome} | EMAIL: {self.__email} | TELEFONE: {self.__fone} | NASCIMENTO: {self.get_nasc().strftime("%d/%m/%Y")}'
    def to_json(self): 
        return {'id' : self.__id, 'nome' : self.__nome, 'email' : self.__email, 'fone' : self.__fone, 'nasc' : self.__nasc}
    @staticmethod
    def from_json(dic):
        return Contato(dic['id'], dic['nome'], dic['email'], dic['fone'], dic['nasc']) 

class ContatoUI: 
    __contato = []
    __contatos_json = Path(__file__).resolve().parent / "contatos.json"
    def main():
        escolha = 0
        while escolha != 8: 
            escolha = ContatoUI.menu()
            match escolha: 
                case 1: ContatoUI.inserir()
                case 2: ContatoUI.listar()
                case 3: ContatoUI.listar_id()
                case 4: ContatoUI.atualizar()
                case 5: ContatoUI.excluir()
                case 6: ContatoUI.pesquisar()
                case 7: ContatoUI.aniversariantes()
        pass
    def menu():
        print(' [1] INSERIR \n [2] LISTAR \n [3] LISTAR_ID \n [4] ATUALIZAR \n [5] EXCLUIR \n [6] PESQUISAR \n [7] ANIVERSARIANTES \n [8] SAIR')
        return int(input('Informe a sua escolha: '))
    @classmethod
    def inserir(cls):
        id = int(input('Informe o ID: \n')) 
        nome = input('Informe o nome: \n')
        email = input('Informe o email: \n')
        fone = input('Informe o telefone: \n')
        nasc = datetime.strptime(input("Informe a data de nascimento: \n"), '%d/%m/%Y')
        x = Contato(id, nome, email, fone, nasc)
        cls.__contato.append(x)
        ContatoUI.salvar()
    @classmethod
    def listar(cls): 
        for x in cls.__contato: print(x)
    @classmethod
    def listar_id(cls):
        id = int(input('Informe o ID: \n'))
        for i in cls.__contato: 
            if i.get_id == id: print(i)
    @classmethod
    def atualizar(cls):
        id = int(input('Informe o ID: \n'))
        for i in cls.__contato: 
            if i.get_id == id: 
                i.set_nome(input('Informe o nome: \n'))
                i.set_email(input('Informe o email: \n'))
                i.set_fone(input('Informe o telefone: \n'))
                i.set_nasc(datetime.strptime(input("Informe a data de nascimento: \n"), '%d/%m/%Y'))
    @classmethod
    def excluir(cls):
        ContatoUI.listar()
        id = int(input('Informe o ID: \n'))
        for i in cls.__contato: 
            if i.get_id == id: cls.__contato.remove(i)
    @classmethod
    def pesquisar(cls):
        nome = input('Informe o início do nome desejado: \n')
        for i in cls.__contato: 
            if i.get_nome().startswith(nome): print(i)
    @classmethod
    def aniversariantes(cls):
        atual = datetime.now()
        for i in cls.__contato: 
            if i.get_nasc().month == atual.month: print(i)
    @classmethod
    def abrir(cls):
        try: 
            arquivo = open(cls.__contatos_json, mode = 'r')
            lista_dicionario = json.load(arquivo)
            arquivo.close()
            for dicionario in lista_dicionario: 
                x = Contato.from_json(dicionario)
                cls.__contatos.append(x)
        except FileNotFoundError: 
            pass
    @classmethod
    def salvar(cls): 
        arquivo = open(cls.__contatos_json, mode = 'w')
        json.dump(cls.__contato, arquivo, default = Contato.to_json, indent = 2)
        arquivo.close()

ContatoUI.main()