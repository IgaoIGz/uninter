ingresso = 0
dindin = 0
soma = 0
while True:
    idade = int(input('Digite a idade: '))
    soma += idade
    if (0 < idade < 3):
        valor = 0
        ingresso = ingresso + 1
        print('ingresso gratuito!')
    elif (3 < idade <= 12):
        valor = 15
        dindin += valor
        ingresso += 1
        print('ingresso é R$ {}'.format(valor))
    elif (12 < idade <= 100):
        valor = 30
        dindin += valor
        ingresso += 1
        print('ingresso é R$ {}'.format(valor))
    else:
        print('Idade inválida!')

    sair = input('Para sair, digite sair: ')
    if (sair == 'sair'):
        break
    else:
        continue
media = soma / ingresso
print('Total de pessoas que compraram ingressos: {}'.format(ingresso))
print('Total de dinheiro arrecadado: {}'.format(dindin))
print('Média da idade dos clientes: {}'.format(media))
print('Encerrando...')