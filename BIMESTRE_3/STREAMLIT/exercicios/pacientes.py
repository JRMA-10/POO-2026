from datetime import datetime

class Paciente: 
    def __init__(self, nome, cpf, telefone, nascimento): 
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_nome(self, nome): 
        if len(nome) == 0: raise ValueError
        self.__nome = nome
    def set_cpf(self, cpf): 
        if len(cpf) < 5: raise ValueError
        self.__cpf = cpf
    def set_telefone(self, telefone): 
        if len(telefone) < 9: raise ValueError
        self.__telefone = telefone
    def set_nascimento(self, nascimento):
        n = datetime.strptime(nascimento, "%d/%m/%Y")
        if n > datetime.now(): raise ValueError
        self.__nascimento = n
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento
    def idade(self): 
        idade = datetime.now() - self.__nascimento
        idade = idade.days
        anos = idade // 365 
        meses = idade % 365 // 30
        return f'{anos} anos e {meses} meses'
    def __str__(self): 
        return f'Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone} | Nascimento: {self.get_nascimento().strftime("%d/%m/%Y")} | Idade: {self.idade()}'
    