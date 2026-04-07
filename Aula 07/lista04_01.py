class Música:
    def __init__(self, título, artista, album):
        self.__título = título
        self.__artista = artista
        self.__album = album
    def get_título(self):
        return self.__título
    def set_titulo(self, título):
        self.__título = título
    def get_artista(self):
        return self.__artista
    def set_artista(self, artista):
        self.__artista = artista
    def get_album(self):
        return self.__album
    def set_album(self, album):
        self.__album = album
    def __str__(self):
        return f"nome da música: {self.__título}, artista: {self.__artista}, album: {self.__album}"

class Playlist:
    def __init__(self, nome, descrição):
        self.__nome = nome
        self.__descrição = descrição
        self.__musicas = []
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_descrição(self):
        return self.__descrição
    def set_descrição(self, descrição):
        self.__descrição = descrição
    def inserir(self, música):
        self.__musicas.append(música)        
    def listar(self):
        return self.__musicas
    def __str__(self):
        return f"nome: {self.__nome} descrição: {self.__descrição}"
    
    m1 = musica("ribs")
