from datetime import datetime

data1 = datetime.strptime("12/11/1996 07:10", "%d/%m/%Y %H:%M")
data2 = datetime.now()
dias_vividos = data2 - data1
print(dias_vividos)