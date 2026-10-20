from datetime import datetime

class AtendimentoItens:
    def __init__(self, id, id_atendimento, id_servico, qtd):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.set_qtd(qtd)
        self.__valor = 0
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_id_atendimento(self, id_atendimento): 
        if id_atendimento < 0: raise ValueError("Id deve ser positivo")
        self.__id_atendimento = id_atendimento
    def set_id_servico(self, id_servico): 
        if id_servico < 0: raise ValueError("Id deve ser positivo")
        self.__id_servico = id_servico
    def set_qtd(self, qtd): 
        if qtd <= 0: raise ValueError('Deve haver pelo menos 1 serviço')
        self.__qtd = qtd

    def get_id(self) : return self.__id
    def get_atendimento(self) : return self.__id_atendimento
    def get_servico(self) : return self.__id_servico
    def get_qtd(self) : return self.__qtd
    
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime("%d/%m/%Y %H:%M")} - {self.__atendimento} - {self.__servico} - {self.__qtd}"
    
    def to_json(self):
        return { "id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"), "id_atendimento":self.__atendimento, "id_servico":self.__id_servico, "qtd":self.__qtd, "valor":self.__valor }
    
    @staticmethod
    def from_json(dic):
        atendimento = AtendimentoItens(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"), dic["id_atendimento"], dic["id_servico"], dic["qtd"], dic["valor"])
        return atendimento