def titulo (s1):
    tam = len(s1)
    print('+', '-'*tam, '+')
    print('|', s1, '|')
    print('+', '-' * tam, '+')

def verifica_opcao ():
    i = 0
    while True:
        try:
            opc = int(input('O que deseja fazer?: '))
            if (opc < 1 or opc > 3):
                print('Digite uma opção válida!')
            else:
                break
        except ValueError:
            print('Erro! Você deve digitar um número!')
        finally:
            i += 1
            print('Tentativa {}'.format(i))
    return opc

def criaArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Algo deu errado!')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo (nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{} | {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

# Programa principal
arquivo = 'games.txt'
if(existeArquivo(arquivo)):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criaArquivo(arquivo)

while True:
    titulo('Meus jogos!')
    titulo('Menu de opções')
    print('Cadastrar | Digite 1')
    print('Consultar | Digite 2')
    print('  Sair    | Digite 3')
    opc = verifica_opcao()
    if (opc == 1):
        print('Cadastro')
        nomeJogo = input('Digite o nome do jogo: ')
        nomeVideogame = input('Digite o nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif (opc == 2):
        print('Consulta')
        listarArquivo(arquivo)
    else:
        print('Encerrando o programa...')
        break
