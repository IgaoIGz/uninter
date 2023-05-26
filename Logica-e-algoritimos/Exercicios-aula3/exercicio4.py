kwh = float(input('Digite a quantidade de kWh consumida: '))
tipo = input('Qual o tipo de instalação? residência (R), indústria (I) e comércio (C): ')

if tipo == 'R':
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'I':
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'C':
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Digite um tipo válido')

print('O preço a pagar é: {}'.format(kwh * preco))
