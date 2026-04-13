import datetime from datetime
class paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento
    def idade(self):
        dia, mes, ano = map(str, self.__nascimento.split("/"))
        idade = datetime()