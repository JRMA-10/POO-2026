class Funcionario(object): # Herda dessa classe padrão
    def __init__(self, nome, salario_base): 
        self.__nome = nome
        self._salario_base = salario_base
    def get_nome(self): return self.__nome
    def get_salario(self): return self._salario_base
    def __str__(self): 
        return f'{self.__nome} - {self.get_salario()}'

class Gerente(Funcionario): 
    def __init__(self, nome, salario_base, gratificacao): 
        super().__init__(nome, salario_base)
        self.__gratificacao = gratificacao
    def get_salario(self):
        return super().get_salario() + self.__gratificacao
    # def __str__(self): 
    #     return f'{super().get_nome()} - {self.get_salario()}'

x = Funcionario("José Maria", 5000)
print(x)
print(x.get_nome())
print(x.get_salario())
y = Gerente("João", 5000, 3000)
print(y)
print(y.get_nome())
print(y.get_salario())

from abc import ABC, abstractmethod

class ClasseAbstrata(ABC): 
    def __init__(self, valor): 
        super().__init__()
        self.valor = valor
    