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
    @staticmethod
    def menu(): 
        print(' [1] INSERIR \n [2] LISTAR \n [3] ATUALIZAR \n [4] EXCLUIR \n [9] FIM')
        return int(input('Informe uma opção: '))
    @staticmethod
    def cliente_inserir(): 
        id = int(input('Informe o ID: \n'))
        nome = input('Informe o nome: \n')
        email = input('Informe o email: \n')
        fone = input('Informe o telefone: \n')
        Service().cliente_inserir(id, nome, email, fone)
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
        Service().cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def cliente_excluir():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input('Informe o id do cliente a ser excluido: \n'))
        Service().cliente_excluir(id)

UI.main()