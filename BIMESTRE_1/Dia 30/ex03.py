class Pais:
    def __init__(self, id, nome, populacao, area): 
        self.set_id(id)
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)
    def set_id(self, i):
        if i >= 0: self.__id = i
        else: raise ValueError
    def set_nome(self, n):
        if len(n) == 0: raise ValueError
        else: self.__nome = n
    def set_populacao(self, p):
        if p >= 0: self.__populacao = p
        else: raise ValueError
    def set_area(self, a):
        if a > 0: self.__area = a
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.get_populacao() / self.get_area()
    def __str__(self):
        return f'Id: {self.get_id()} | Nome: {self.get_nome()} | População: {self.get_populacao()} | Área: {self.get_area():.2f} | Densidade demográfica: {self.densidade():.2f}'

class PaisUI:
    paises = []
    @staticmethod
    def main():
        escolha = 0
        while escolha != 7:
            escolha = PaisUI.menu()
            if escolha == 1: PaisUI.inserir()
            elif escolha == 2: PaisUI.listar()
            elif escolha == 3: PaisUI.atualizar()
            elif escolha == 4: PaisUI.excluir()
            elif escolha == 5: PaisUI.mais_populoso()
            elif escolha == 6: PaisUI.mais_povoado()
            else: escolha = 7
    def menu():
        print('[1] INSERIR \n[2] LISTAR \n[3] ATUALIZAR \n[4] EXCLUIR \n[5] MAIS POPULOSO \n[6] MAIS POVOADO \n[7] SAIR')
        escolha = int(input('Insira a sua escolha: '))
        return escolha
    @classmethod
    def inserir(cls):
        id = int(input('Digite o ID do País: \n'))
        nome = input('Digite o nome do País: \n')
        populacao = int(input('Digite a população do País: \n'))
        area = float(input('Digite a área: '))
        o = Pais(id, nome, populacao, area)
        cls.paises.append(o)
    @classmethod
    def listar(cls):
        for n in cls.paises:
            print(n)
    @classmethod
    def atualizar(cls):
        PaisUI.listar()
        id = int(input('Informe o ID para alteração: '))
        for obj in cls.paises:
            if obj.get_id() == id:
                nome = input('Digite o nome do País: \n')
                populacao = int(input('Digite a população do País: \n'))
                area = float(input('Digite a área: '))
                obj.set_nome(nome)
                obj.set_populacao(populacao)
                obj.set_area(area)
    @classmethod
    def excluir(cls):
        id = int(input('Informe o ID para alteração: '))
        for obj in cls.paises:
            if obj.get_id() == id:
                cls.paises.remove(obj)
    @classmethod
    def mais_populoso(cls):
        populacao = {}
        valores = []
        for c in cls.paises:
            populacao[c.get_populacao()] = c.get_nome()
            valores.append(c.get_populacao())
        maior = max(valores)
        print(populacao[maior])
    @classmethod
    def mais_povoado(cls):
        povoamento = {}
        valores = []
        for c in cls.paises:
            povoamento[c.densidade()] = c.get_nome()
            valores.append(c.densidade())
        maior = max(valores)
        print(povoamento[maior])
PaisUI.main()