# Ler 4 valores inteiros diferentes e realizar as seguintes operações: verificar se os valores são realmente diferentes
# e mostrar uma mensagem de erro, caso contrário; mostrar o maior valor lido; mostrar o menor valor lido e mostrar o
# resultado da soma entre o segundo maior valor e o segundo menor.
print('Digite quatro valores inteiros.')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b or a == c or a == d or b == c or  c == d or b == d:
    print('ERRO </3')
else:
    menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
if d < menor:
    menor = d

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d

soma = a + b + c + d - maior - menor
print(f'maior numero: {maior}')
print(f'menor numero: {menor}')
print(f'a soma do segundo maior com o segundo menor: {soma}')