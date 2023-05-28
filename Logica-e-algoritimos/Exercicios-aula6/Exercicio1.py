notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# a
print(notas.count(7))
# b
notas[-1] = 4
print(notas)
# c
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
maior = 0
n = 0
for i in notas:
    atual = notas[n]
    if (atual > maior):
        maior = atual
    n += 1
print(maior)
# d
notas.sort()
print(notas)
# e
n = 0
soma = 0
for i in notas:
    soma += notas[n]
    n += 1
media = soma / n
print('A média é {}'.format(media))
