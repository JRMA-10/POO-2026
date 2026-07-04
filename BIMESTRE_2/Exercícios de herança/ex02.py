class Playlist: 
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
    def set_id(self, i):
        if i >= 1: self.__id = i
        else: raise ValueError
    def set_nome(self, n):
        if len(n) > 0: self.__nome = n
        else: raise ValueError
    def set_descricao(self, d):
        if len(d) >= 0: self.__descricao = d
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def __str__(self):
        return f'ID da Playslist: {self.get_id()} | Nome: {self.get_nome()} | Descrição: {self.get_descricao()}'

class Musicas: 
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    def set_id(self, i):
        if i >= 1: self.__id = i
        else: raise ValueError
    def set_titulo(self, t):
        if len(t) > 0: self.__titulo = t
        else: raise ValueError
    def set_artista(self, a):
        if len(a) >= 0: self.__artista = a
        else: raise ValueError
    def set_album(self, a):
        if len(a) >= 0: self.__album = a
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    def __str__(self):
        return f'ID da música: {self.get_id()} | Título: {self.get_titulo()} | Artista: {self.get_artista()} | Álbum: {self.get_album()}'
    
class PlayListitem:
    def __init__(self, id, idpl, idmusic, sequencia):
        self.set_id(id)
        self.set_idpl(idpl)
        self.set_idmusic(idmusic)
        self.set_sequencia(sequencia)
    def set_id(self, i):
        if i >= 1: self.__id = i
        else: raise ValueError
    def set_idpl(self, i):
        if i >= 1: self.__idpl = i
        else: raise ValueError
    def set_idmusic(self, i):
        if i >= 1: self.__idmusic = i
        else: raise ValueError
    def set_sequencia(self, s):
        if s >= 1: self.__sequencia = s
        else: raise ValueError
    def get_id(self):
        return self.__id
    def get_idpl(self):
        return self.__idpl
    def get_idmusic(self):
        return self.__idmusic
    def get_sequencia(self):
        return self.__sequencia
    def __str__(self):
        return f'ID: {self.get_id()} | ID da Playslist: {self.get_idpl()} | ID da música: {self.get_idmusic()} | Sequência: {self.get_sequencia()}'

class UI:
    lista_de_playlists = []
    lista_de_musicas = []
    lista_de_itens = []
    id_geral = 1
    def main():
        escolha = 0
        while escolha != 12:
            escolha = UI.menu()
            match escolha:
                case 1: UI.inserir_playlist()
                case 2: UI.listar_playlist()
                case 3: UI.atualizar_playlist()
                case 4: UI.excluir_playlist()
                case 5: UI.inserir_musica()
                case 6: UI.listar_musicas()
                case 7: UI.atualizar_musica()
                case 8: UI.excluir_musica()
                case 9: UI.adicionando_musica_playlist()
                case 10: UI.remover_musica_playlist()
                case 11: UI.ver_musicas_playlist()
    def menu():
        print('[1] INSERIR PLAYLIST\n[2] LISTAR PLAYLISTS \n[3] ATUALIZAR PLAYLIST \n[4] EXCLUIR PLAYLIST \n[5] INSERIR MÚSICA \n[6] LISTAR MÚSICAS \n[7] ATUALIZAR MÚSICAS \n[8] EXCLUIR MÚSICA \n[9] ADICIONAR UMA MÚSICA A UMA PLAYLIST \n[10] REMOVER UMA MÚSICAS DE UMA PLAYLIST \n[11] VER MÚSICAS DE UMA PLAYLIST \n[12] SAIR')
        c = int(input('Informe a sua escolha: \n'))
        return c
    @classmethod
    def inserir_playlist(cls):
        id = int(input('Informe o ID da playlist: \n'))
        nome = input('Informe o nome da playlist: \n').strip()
        descricao = input('Informe uma descrição para a playlist: ').strip()
        P = Playlist(id, nome, descricao)
        for i in cls.lista_de_playlists:
            if i.get_id() == id or i.get_nome() == nome: print('Não foi possível adicionar a playslist, pois ela já existe!')
            return
        cls.lista_de_playlists.append(P)
    @classmethod
    def listar_playlist(cls):
        for i in cls.lista_de_playlists: print(i)
    @classmethod
    def atualizar_playlist(cls):
        UI.listar_playlist()
        id = int(input('Informe o ID da playlist: '))
        for i in cls.lista_de_playlists:
            if i.get_id() == id: 
                i.set_nome(input('Informe o novo nome: '))
                i.set_descricao(input('Informe a nova descrição: '))
    @classmethod
    def excluir_playlist(cls):
        UI.listar_playlist()
        id = int(input('Informe o ID da playlist que você deseja excluir: '))
        for i in cls.lista_de_playlists:
            if i.get_id() == id: cls.lista_de_playlists.remove(i)
    @classmethod
    def inserir_musica(cls):
        id = int(input('Informe o ID da música: \n'))
        titulo = input('Informe o titulo da música: \n').strip()
        artista = input('Informe o artista da música: ').strip()
        album = input('Informe o álbum da música: ').strip()
        M = Musicas(id, titulo, artista, album)
        for i in cls.lista_de_musicas:
            if i.get_id() == id or i.get_titulo() == titulo: print('Não foi possível adicionar a música, pois ela já existe!')
            return
        cls.lista_de_musicas.append(M)
    @classmethod
    def listar_musicas(cls):
        for i in cls.lista_de_musicas: print(i)
    @classmethod
    def atualizar_musica(cls):
        UI.listar_musicas()
        id = int(input('Informe o ID da música: '))
        for i in cls.lista_de_musicas:
            if i.get_id() == id: 
                i.set_titulo(input('Informe o novo titulo: '))
                i.set_artista(input('Informe o novo artista: '))
                i.set_album(input('Informe o novo album: '))
    @classmethod
    def excluir_musica(cls):
        UI.listar_musicas()
        id = int(input('Informe o ID da música que você deseja excluir: '))
        for i in cls.lista_de_musicas:
            if i.get_id() == id: cls.lista_de_musicas.remove(i)
    @classmethod
    def adicionando_musica_playlist(cls):
        id = cls.id_geral
        idpl = int(input('Informe o ID da playlist: '))
        idmusic = int(input('Informe o ID da música: '))
        sequecia = int(input('Informe a sequencia da música: '))
        PL = PlayListitem(id, idpl, idmusic, sequecia)
        cls.lista_de_itens.append(PL)
        cls.id_geral += 1
    @classmethod
    def remover_musica_playlist(cls):
        UI.ver_musicas_playlist()
        id = int(input('Informe o ID do item que você deseja remover: '))
        for i in cls.lista_de_itens:
            if i.get_id() == id: 
                cls.lista_de_itens.remove(i)
                print('Item removido com sucesso! ')
                return
        print('Item não encontrado na playlist!')
    @classmethod
    def ver_musicas_playlist(cls):
        UI.listar_playlist()
        id = int(input('Informe o ID da playlist que você deseja ouvir: '))
        for i in cls.lista_de_itens:
            if i.get_idpl() == id: 
                id_musica = i.get_idmusic()
                for e in cls.lista_de_musicas:
                    if e.get_id() == id_musica: print(e)
UI.main()