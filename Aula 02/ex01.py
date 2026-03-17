# Ler quatro números inteiros, calcular a soma dos números pares e a soma dos números ímpares.
print('Digite 4 valores Inteiros')
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
sp = 0
si = 0
if v1 % 2 == 0:
    sp += v1
else:
    si += v1
if v2 % 2 == 0:
    sp += v2
else:
    si += v2    
if v3 % 2 == 0:
    sp += v3
else:
    si += v3    
if v4 % 2 == 0:
    sp += v4
else:
    si += v4
print("Soma dos Pares = ", sp)
print("Soma dos Impares = ", si)

    
