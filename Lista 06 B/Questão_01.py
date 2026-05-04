from datetime import datetime

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
class Venda:
    def __init__(self, id):
        self.__id = id
        self.__data = datetime.now()
        self.__carrinho = True
        self.__total = 0
        self.__idcliente = None
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__carrinho} R${self.__total:.2f} - {self.__idcliente}"
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_carrinho(self):
        return self.__carrinho
    def get_total(self):
        return self.__total
    def get_idcliente(self):
        return self.__idcliente
    
    def set_id(self, id):
        self.__id = id
    def set_data(self, data):
        self.__data = data
    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho
    def set_total(self, total):
        self.__total = total
    def set_idcliente(self, idcliente):
        self.__idcliente = idcliente

class VendaItem:
    def __init__(self, id, qtd, preco):
        self.__id = id
        self.__qtd = qtd
        self.__preco = preco
        self.__idvenda =  None
        self.__idproduto = None
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - R${self.__preco:.2f} - {self.__idvenda} - {self.__idproduto}"
    def set_id(self, id):
        self.__id = id
    def set_qtd(self, qtd):
        self.__qtd = qtd
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            raise ValueError ("Valor inválido de venda.")
    def set_idvenda(self, idvenda):
        if idvenda > 0:
            self.__idvenda = idvenda
        else:
            raise ValueError ("valor de id de venda inválido.")
    def set_idproduto(self, idproduto):
        if idproduto > 0:
            self.__idproduto = idproduto
        else:
            raise ValueError("valor de id do produto inválido.")
    def get_id(self):
        return self.__id
    def get_qtd(self):
        return self.__qtd
    def get_preco(self):
        
        return self.__preco
    def get_idvenda(self):
        return self.__idvenda
    def get_idproduto(self):
        return self.__idproduto
    
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
class CategoriaDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.__objetos.append(obj)
    @classmethod
    def listar(cls):
        return cls.__objetos
    @classmethod
    def listar_id(cls, id):
        for i in cls.__objetos:
            if i.get_id() == id:
                return i
        return None
    @classmethod
    def atualizar(cls, obj):
        for i in cls.listar():
            if (obj.get_id):
        
                
    


    
    

    

    
    



