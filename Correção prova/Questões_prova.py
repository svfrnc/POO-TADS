class abastecimento:
    def __innit__(self, data, km_rodados, num_litros, valor_pago):
        self.__data = data
        self.__km_rodados = km_rodados
        self.__num_litros = num_litros
        self.__valor_pago = valor_pago
    def set_data(self, data):
        self.__data = data
    def set_km_rodados(self, km_rodados):
        if km_rodado > 0:
            self.__km_rodados = km_rodados
        else:
            raise ValueError("O valor deve ser positivo")
    def set_num_litros(self, num_litros):
        if km_rodado > 0:
            self.__num_litros = num_litros
        else:
            raise ValueError("O valor deve ser positivo")
    def set_valor_pago(self, valor_pago):
        if valor_pago > 0:
            self.__valor_pago = valor_pago
        else:
            raise ValueError("O valor deve ser positivo")
    def get_data(self):
        return self.__data
    def get_km_rodados(self):
        return self.__km_rodados
    def get_num_litros(self):
        return self.__num_litros
    def get_valor_pago(self):
        return self.__valor_pago
    def get_km_por_litro(self):
        return self.__km_rodados / self.__num_litros
    def get_valor_por_km(self):
        return self.__valor_pago / self.__km_rodados
    def __str__(self):
        return f"{self.__data} - {self.__km_rodados}km - {self.__num_litros}L - R${self.__valor_pago:.2f}"
class UI:
    @staticmethod
    def main():
        lista = []
        for k in range(3):
            data = input("informe a data do abastecimento: ")
            km = float(input("Informe a quilometragem rodada: "))
            litros = float(input("informe o número de litros do abastecimento: "))
            valor = float(input("informe o valor pago em reais: "))
            x = abastecimento(data, km, litros, valor)
            lista.append(x)
        for x in lista:
            print(x)
        menor = lista[0]
        for x in lista:
            if x.km_por_litro() < menor.km_por_litro():
                menor = x
            if x.km_por_litro() > maior.km_por_litro():
                maior = x 
        print(menor)
        print(maior)