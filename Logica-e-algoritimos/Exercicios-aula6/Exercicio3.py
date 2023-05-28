from random import randint

print('JOKENPÔ')
print('1 - pedra')
print('2 - papel')
print('3 - tesoura')
wins = []
while True:
    h = int(input('Escolha pedra, papel, ou tesoura!\n>>>'))
    p = randint(1, 3)
    if(h == 0):
        print('Você digitou 0, encerrando...')
        break
    elif(h < 0 or h > 3):
        print('Digite um valor válido!')
        continue
    if((h == 1 and p == 2) or (h == 2 and p == 3) or (h == 3 and p == 1)):
        vencedor = 'pc'
        wins.append(vencedor)
        print('O computador venceu o round!')
    elif(h == p):
        vencedor = 'empate'
        wins.append(vencedor)
        print('Empate!')
    else:
        vencedor = 'humano'
        wins.append(vencedor)
        print('O humano venceu o round!')

e = wins.count('empate')
hv = wins.count('humano')
pv = wins.count('pc')

if(hv > pv):
    print('O humano venceu por {} x {}'.format(hv, pv))
elif(hv == pv):
    print('Empate final! Placar: {} x {}'.format(hv, pv))
else:
    print('O computador venceu por {} x {}'.format(pv, hv))



