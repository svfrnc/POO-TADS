class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        pass
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    def set_id(self):
        if id > 0:
            self.__id = id
        else:
            raise ValueError("valor de ID incompatível")
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone
    def get_id(self):
        return id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone

class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao
    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
    def set_id(self, id):
        if id > 0:
            self.__id = id
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
class Produto:
    def __init__(self, id, descricao, preco, estoque, idcategoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idcategoria = idcategoria
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__preco:.2f} - {self.__estoque} - {self.__idcategoria}"
    def set_id(self, id):
        if id > 0:
            self.__id = id
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            raise ValueError("Valor inválido de produto")
    def set_estoque(self, estoque):
        if estoque >= 0:
            self.__estoque = estoque
        else:
            raise ValueError("Quantidade de estoque inválida.")
    def set_idcategoria(self, idcategoria):
            if idcategoria > 0:
                self.__idcategoria = idcategoria
            else:
                raise ValueError("Valor de ID da categoria inválido")
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__preco
    def get_estoque(self):
        return self.__preco
    def get_idcategoria(self):
        return self.__idcategoria
class VendaItem:
    def __init__(self, id, qtd, preco, idvenda, idproduto):
        self.__id = id
        self.__qtd = qtd
        self.__preco = preco
        self.__idvenda = idvenda
        self.__idproduto = idproduto
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - R${self.__preco:.2f} - {self.__idvenda} - {self.__idproduto}"
    def set_id(self, id):
        self.__id = id
    def set_qtd(self, qtd):
        self.__qtd = qtd
        

    

    
    



