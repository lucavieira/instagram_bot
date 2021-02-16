def existe_arquivo(arquivo):
    try:
        file = open(arquivo, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(arquivo):
    try:
        file = open(arquivo, 'wt+')
        file.close()
    except:
        print('Ocorreu um erro ao criar o arquivo')
    else:
        print('Arquivo criado com sucesso')


def ler_arquivo(arquivo, nome_perfil):
    try:
        file = open(arquivo, 'rt')
    except:
        print('Ocorreu um erro ao ler o arquivo')
    else:
        linhas = file.readlines()
        if len(linhas) == 0:
            return True
        else:
            if linhas.count(nome_perfil + '\n') == 1:
                return False
            else:
                return True
    finally:
        file.close()


def cadastrar_perfil(arquivo, perfil):
    try:
        file = open(arquivo, 'at')
    except:
        print('Ocorreu um erro ao cadastrar o perfil')
    else:
        try:
            file.write(f'{perfil}\n')
        except:
            print('Erro ao gravar perfil')
        else:
            print(f'Perfil {perfil} adicionado com sucesso')
            file.close()

