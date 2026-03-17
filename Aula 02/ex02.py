# Ler o número do mês (1 – janeiro; 2 – fevereiro; ...; 12 – dezembro) e identificar o nome do mês e em que trimestre o mês está incluído.
print('Informe o número do mês')
meses = [0, 'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
numero_mes = int(input())

nome_mes = 0
trimestre = len(meses) // 4
for i in meses:
    if trimestre >= 1 and trimestre < 4:
        trimestre_ano = 1
    elif trimestre >= 4 and trimestre < 7:
        trimestre_ano = 2
    elif trimestre >= 7 and trimestre < 10:
        trimestre_ano = 3
    elif trimestre >= 10 and trimestre <= 12:
        trimestre_ano = 4
print(f"o mês de {meses[numero_mes]} é do {trimestre_ano} do ano.")




