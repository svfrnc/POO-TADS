from datetime import datetime

data1 = datetime.strptime("24/04/1997 16:05", "%d/%m/%Y %H:%M")
data2 = datetime.now()
dias_vividos = data2 - data1
print(dias_vividos)