def soma(x=0, y=0, z=0):
  """
  Função que soma até 3 valores inteiros
  Todos os parâmetros são opcionais
  :param x: valor inteiro opcional
  :param y: valor inteiro opcional
  :param z: valor inteiro opcional
  :return: Retorna o somatório de até 3 valores numéricos quaisquer.
  """
  return x + y + z

# programa principal
print(soma(7, 5))
help(soma)