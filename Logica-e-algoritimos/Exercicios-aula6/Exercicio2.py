palavras = ('carro', 'casa', 'cachorro', 'sabonete', 'beard', 'samba', 'playoff', 'bucket', 'ovo', 'cuscuz')
for i in palavras:
    vogais = i.count('a') + i.count('e') + i.count('i') + i.count('o') + i.count('u')
    print('Palavra: {}. {} vogais: '.format(i, vogais), end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end='')
    print()
