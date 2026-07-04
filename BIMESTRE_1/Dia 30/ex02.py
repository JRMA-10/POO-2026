class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)  #atriburos de instancia
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError
        else: self.__id = id 
    def set_nome(self, nome): 
        if len(nome) > 0: self.__nome = nome 
        else: raise ValueError
    def set_email(self, email):
        self.__email = email 
    def set_fone(self, fone):
        self.__fone = fone 
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f'{self.get_id()} - {self.get_nome()} - {self.get_email()} - {self.get_fone()}'

class ContatoUI:
    contatos = [] #atributo de classe 
    @staticmethod #Esse método serve para reiniar os valores sempre que a função for chamada
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            elif op == 2: ContatoUI.listar()
            elif op == 3: ContatoUI.atualizar()
            elif op == 4: ContatoUI.excluir()
            elif op == 5: ContatoUI.pesquisar()
            else: op = 6
    def menu():
        print('[1] - INSERIR \n[2] - LISTAR \n[3] - ATUALIZAR \n[4] - EXCLUIR \n[5] - PESQUISAR \n[6] - FIM')
        return int(input('Sua escolha: '))
    @classmethod
    def inserir(cls): #estático que acessa um elemento da classe 
        id = int(input('Informe o id do contato: '))
        nome = input('Infome o nome: ')
        email = input('Informe o email: ')
        fone = input('Informe o telefone: ')
        x = Contato(id, nome, email, fone)
        cls.contatos.append(x)
    @classmethod #permite usar valores que estão armazenados na classe, mas fora da função
    def listar(cls): #para usar esse valores, é necessário colocar como parâmetro CLS
        if len(cls.contatos) == 0: print('Nenhum contato na agenda!')
        else: 
            for x in cls.contatos: print(x)
    @classmethod
    def atualizar(cls):
        for i in cls.contatos: print(i)
        n = int(input('Informe o ID do usuário que você quer alterar: '))
        for ob in cls.contatos:
            if ob.get_id() == n: 
                nome = input('Infome o novo nome: ')
                email = input('Informe o novo email: ')
                fone = input('Informe o novo telefone: ')
                ob.set_email(email)
                ob.set_fone(fone)
                ob.set_nome(nome)
    @classmethod
    def excluir(cls):
        for i in cls.contatos: print(i)
        n = int(input('Informe o id do contato que você deseja deletar: '))
        for ob in cls.contatos:
            if ob.get_id() == n:
                cls.contatos.remove(ob)
    @classmethod
    def pesquisar(cls): 
        iniciais = input('Infome o nome do contato: \n').strip()
        for obj in cls.contatos:
            if obj.get_nome().startswith(iniciais):
                print(obj)
ContatoUI.main()