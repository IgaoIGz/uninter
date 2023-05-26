print('Calculadora')
print('+ ADIÇÃO')
print('- SUBTRAÇÃO')
print('x MULTIPLICAÇÃO')
print('/ DIVISÃO')
print('sair')
while True:
    op = input('Qual operação deseja fazer?')
    if (op == 'sair'):
        print('Encerrando...')
        break
    elif (op == '+' or op == '-' or op == 'x' or op == '/'):
        x = float(input('Digite o primeiro valor: '))
        y = float(input('Digite o segundo valor: '))
        if (op == '+'):
            r = x + y
        elif (op == '-'):
            r = x - y
        elif (op == 'x'):
            r = x * y
        else:
            r = x / y
        print('-' * 15)
        print('RESULTADO')
        print('{} {} {} = {}'.format(x, op, y, r))
        print('-'*15)
    else:
        print('-' * 15)
        print('Valor de operação inválido!')
        print('-' * 15)
        continue
