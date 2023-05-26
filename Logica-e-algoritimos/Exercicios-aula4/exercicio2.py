valor = int(input('Qual é o valor? '))
while True:
    if (valor >= 100):
        cem = valor // 100
        valor = valor % 100
        print('{} notas de cem'.format(cem))
        if not valor:
            break
    if (valor >= 50):
        cinquenta = valor // 50
        valor = valor % 50
        print('{} notas de cinquenta'.format(cinquenta))
        if not valor:
            break
    if (valor >= 20):
        vinte = valor // 20
        valor = valor % 20
        print('{} notas de vinte'.format(vinte))
        if not valor:
            break
    if (valor >= 10):
        dez = valor // 10
        valor = valor % 10
        print('{} notas de dez'.format(dez))
        if not valor:
            break
    if (valor >= 5):
        cinco = valor // 5
        valor = valor % 5
        print('{} notas de cinco'.format(cinco))
        if not valor:
            break
    if (valor >= 1):
        um = valor // 1
        valor = valor % 1
        print('{} notas de um'.format(um))
        break
