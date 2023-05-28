pessoas = {
    'nome': [],
    'ano': [],
    'sexo': []
}
i = 0
while True:
    nome = input('Digite seu nome: ')
    ano = int(input('Digite seu ano de nascimento: '))
    sexo = input('Digite seu sexo[Masculino/Feminino]: ')
    sexo = sexo.lower()
    pessoas['nome'].append(nome)
    pessoas['ano'].append(ano)
    pessoas['sexo'].append(sexo)
    i += 1
    sair = input('Deseja parar de cadastrar?[S/N]:\n>>>')
    sair = sair.upper()
    if (sair == 'S'):
        print('Parando de cadastrar...')
        break

print('Total de pessoas cadastradas: {}'.format(i))
indice = 0
soma_idade = 0
print('Mulheres com menos de 30 anos:')
for n in pessoas['ano']:
    idade = 2023 - pessoas['ano'][indice]
    if (idade < 30 and pessoas['sexo'][indice] == 'feminino'):
        print(' - Nome: {}'.format(pessoas['nome'][indice]))
    soma_idade += idade
    indice += 1
media = soma_idade / i
indice = 0
print('A média de idade das pessoas é: {}'.format(media))
print('Homens com idade acima da média:')
for n in pessoas['ano']:
    idade = 2023 - pessoas['ano'][indice]
    if (idade > media and pessoas['sexo'][indice] == 'masculino'):
        print(' - Nome: {}'.format(pessoas['nome'][indice]))
    indice += 1
