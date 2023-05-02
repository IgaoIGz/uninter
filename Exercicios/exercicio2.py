# Exercicio 2
km = float(input('Digite a quantidade de kms rodados: '))
dias = int(input('Quantos dias que o carro ficou alugado? '))
calculo = (km*0.15)+(dias*60)

print('Km: {}\nDias: {}'.format(km, dias))
print('O valor a ser pago pelo aluguel do carro é: {}'.format(calculo))
