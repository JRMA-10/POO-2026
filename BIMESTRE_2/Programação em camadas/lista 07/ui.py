from service import Service

class UI: 
    @staticmethod
    def main(): 
        op = 0
        while op != 9: 
            op = UI.menu()
            match op: 
                case 1: UI.cliente_inserir()
                case 2: UI.cliente_listar()
                case 3: UI.cliente_atualizar()
                case 4: UI.cliente_excluir()
                case 5: UI.servico_inserir()
                case 6: UI.servico_listar()
                case 7: UI.servico_atualizar()
                case 8: UI.servico_excluir()
    @staticmethod
    def menu(): 
        print(' [1] INSERIR CLIENTE \n [2] LISTAR CLIENTE \n [3] ATUALIZAR CLIENTE  \n [4] EXCLUIR CLIENTE \n [5] INSERIR SERVIÇO \n [6] LISTAR SERVIÇOS \n [7] ATUALIZAR SERVIÇOS \n [8] EXCLUIR SERVIÇOS \n [9] FIM')
        return int(input('Informe uma opção: '))
    @staticmethod
    def cliente_inserir(): 
        id = int(input('Informe o ID: \n'))
        nome = input('Informe o nome: \n')
        email = input('Informe o email: \n')
        fone = input('Informe o telefone: \n')
        Service.cliente_inserir(id, nome, email, fone)
    @staticmethod
    def cliente_listar(): 
        for obj in Service().cliente_listar(): print(obj)
    @staticmethod
    def cliente_atualizar(): 
        for obj in Service().cliente_listar(): print(obj)
        id = int(input('Informe o ID a ser atualizado: \n'))
        nome = input('Informe o novo nome: \n')
        email = input('Informe o novo email: \n')
        fone = input('Informe o novo telefone: \n')
        Service.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def cliente_excluir():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input('Informe o id do cliente a ser excluido: \n'))
        Service().cliente_excluir(id)
    
    @staticmethod
    def servico_inserir(): 
        id = int(input('Informe o ID do serviço: \n'))
        servico = input('Informe a descricao do servico: \n')
        valor = float(input('Informe o valor do serviço: \n'))
        Service.servico_inserir(id, servico, valor)
    @staticmethod
    def servico_listar(): 
        for obj in Service.servico_listar: print(obj)
    @staticmethod
    def servico_atualizar(): 
        for obj in Service().servico_listar(): print(obj)
        id = int(input('Informe o ID a ser atualizado: \n'))
        descricao = input('Informe a nova descrição: \n')
        valor = float(input('Informe o novo valor: \n'))
        Service.servico_atualizar(id, descricao, valor)
    @staticmethod
    def servico_excluir(): 
        for obj in Service.servico_listar(): print(obj)
        id = int(input('Informe o id do serviço a ser excluido: \n'))
        Service.servico_excluir(id)
UI.main()