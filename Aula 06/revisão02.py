class Cliente:
    def __init__(self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
    def set_socio(self, c):
        self.__socio = c
        c.__socio = self
    def get_limite(self):
        if self.__socio == None:
            return self.__limite
            return self.__limite + self.__socio.__limite
    def __str__(self):
        if self.__socio == None:
            return 

