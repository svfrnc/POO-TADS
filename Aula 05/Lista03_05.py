class data:
    def __init__(self, dia, mes, ano):
        self.set_Data(f"{dia}/{mes}/{ano}")
    def set_Data(self, data):
        dia, mes, ano = map(int,data.split("/"))
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
        max_dia = 31
        if mes in [4,6,9,11]:
            max_dia = 30
        if mes == 2:
            if ano == bissexto:
                max_dia = 29
            else:
                max_dia = 28
        if 1 <= dia <= max_dia and 1 < mes < 12 and 1 < ano:
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
        else: raise ValueError("Data inválida")
    def __str__(self):
        return f"Data: {self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}"
    def get_dia(self):
        return self.__dia
    def get_mes(self):
        return self.__mes
    def get_ano(self):
        return self.__ano 
calendario = data(12, 11, 1996)
print(calendario)