from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.profissionais import Profissionais
from models.profissionaisdao import ProfissionaisDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(obj)
    @staticmethod
    def cliente_listar(): return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id): return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha): 
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id): ClienteDAO().excluir(id)
    @staticmethod
    def cliente_listar_nomes(iniciais): return ClienteDAO().listar_nome(iniciais)
    
    @staticmethod
    def servico_inserir(descricao, valor): 
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar(): return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id): return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor): 
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)
    @staticmethod
    def servico_listar_nomes(iniciais): return ServicoDAO().listar_nome(iniciais)
    @staticmethod
    def servico_listar_descricao(desc): return ServicoDAO().listar_descricao(desc)

    @staticmethod
    def profissionais_inserir(nome, email, senha, especialidade):
        obj = Profissionais(0, nome, email, senha, especialidade)
        ProfissionaisDAO.inserir(obj)
    @staticmethod
    def profissionais_listar(): return ProfissionaisDAO().listar()
    @staticmethod
    def profissionais_listar_id(id): return ProfissionaisDAO().listar_id(id)
    @staticmethod
    def profissionais_atualizar(id, nome, email, senha, especialidade): 
        obj = Profissionais(id, nome, email, senha, especialidade)
        ProfissionaisDAO().atualizar(obj)
    @staticmethod
    def profissionais_excluir(id): ProfissionaisDAO().excluir(id)
    @staticmethod
    def profissionais_listar_nomes(iniciais): return ProfissionaisDAO().listar_nome(iniciais)