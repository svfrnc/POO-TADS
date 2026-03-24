# Ler uma data no formato "dd/mm/aaaa" e verificar se é uma data válida, considerando como válidos os anos entre
# 1900 e 2100, meses de 1 a 12 e dias de acordo com o mês.
print('Digite uma data.')
dia, mes, ano = map(int,input().split('/'))
valida = False
if ano >= 1900 and ano <=2100:
    valida = True
if mes > 0 and mes <= 12:
    valida = True
if dia > 0 and dia <= 31:
    valida = True

