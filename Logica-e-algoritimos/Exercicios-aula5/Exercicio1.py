def valida(x):
    """
    Esta função valida um dado digitado pelo usuário. Verifica se o número é positivo.
    :param x: Recebe um dado digitado pelo usuário
    :return: Retorna o valor quando ele for positivo
    """
    while (x < 0):
        x = int(input('Digite um valor positivo!: '))
    return x
def fatorial(num):
    """
    Faz o fatorial de um número positivo digitado pelo usuário
    :param num: Número de referência para o fatorial
    :return: Retorna o resultado da fatorial
    """
    multi = 1
    if num == 0:
        return multi
    for i in range(1, num + 1, 1):
        multi *= i
    return multi

x = int(input('Digite um valor: '))
x = valida(x)
print(fatorial(x))
