from datetime import datetime

class Paciente: 
    def __init__(self, id, nome, cpf, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_cpf(self, c):
        if len(c) == 11: self.__cpf = c
        else: raise ValueError
    def set_telefone(self, t): 
        if len(t) == 11: self.__telefone = t
        else: raise ValueError
    def set_nascimento(self, n):
        if n > datetime.now(): self.__nascimento = n
        else: raise ValueError("Você não pode ter nascido no futuro!")
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return int(self.__cpf)
    def get_telefone(self): return int(self.__telefone)
    def get_nascimento(self): return self.__nascimento
    def idade(self):
        data_atual = datetime.now()
        x = data_atual - self.get_nascimento()
        anos = x.days // 365 
        meses = x.days % 365 // 30
        return anos, meses
    def __str__(self):
        return f'ID: {self.get_id()} | Nome: {self.get_nome()} | CPF: {self.get_cpf()} | Telefone: {self.get_telefone()} | Data de nascimento: {self.get_nascimento().strftime("%d/%m/%Y")} | Idade atual: {self.idade()[0]} anos e {self.idade()[1]} meses'

class PacienteUI:
    lista = []
    @staticmethod
    def main():
        escolha = 0
        while escolha != 7:
            escolha = PacienteUI.menu()
            match escolha:
                case 1: PacienteUI.inserir()
                case 2: PacienteUI.listar()
                case 3: PacienteUI.atualizar()
                case 4: PacienteUI.excluir()
                case 5: PacienteUI.pesquisar()
                case 6: PacienteUI.aniversariantes()
    @staticmethod
    def menu():
        print('[1] Inserir \n[2] Listar \n[3] Atualizar \n[4] Excluir \n[5] Pesquisar \n[6] Aniversariantes \n[7] Sair')
        return int(input('Informe a opção desejada: '))
    @classmethod
    def inserir(cls):
        id = int(input('Informe o ID do paciente: \n'))
        nome = input('Informe o seu nome: ')
        cpf = input('Informe o seu CPF: \n').strip()
        telefone = input('Informe o seu telefone: \n').strip()
        nascimento = datetime.strptime(input("Informe a data de nascimento: \n"), '%d/%m/%Y')
        x = Paciente(id, nome, cpf, telefone, nascimento)
        cls.lista.append(x)
    @classmethod
    def listar(cls):
        for i in cls.lista: print(i)
    @classmethod
    def atualizar(cls): 
        PacienteUI.listar()
        id = int(input('Informe o ID do paciente para alteração: '))
        for i in cls.lista: 
            if i.get_id() == id:
                i.set_nome(input('Informe o seu novo nome: \n').strip())
                i.set_telefone(input('Informe o seu telefone: \n').strip())
                i.set_cpf(input('Informe o seu CPF: \n').strip())
                i.set_nascimento(datetime.strptime(input("Informe a data de nascimento: \n"), '%d/%m/%Y'))
    @classmethod
    def excluir(cls): 
        PacienteUI.listar()
        id = int(input('Informe o id para a exclusão do paciente: '))
        for i in cls.lista: 
            if i.get_id() == id: 
                cls.lista.remove(i)
    @classmethod
    def pesquisar(cls):
        nome = input('Informe as primeiras letras do nome do paciente: \n')
        for i in cls.lista: 
            if i.get_nome().startswith(nome): 
                print(i)
    @classmethod
    def aniversariantes(cls): 
        mes_informado = int(input('Informe o mês para ver os aniversariantes: \n'))
        for i in cls.lista:
            if i.get_nascimento().month == mes_informado:
                print(i)
PacienteUI.main()