"""############################## Função para validar se o jogo deve continuar ##########################"""

"""Modulos para validação da Matriz e melhorar semântica do código principal"""


def mostra_matriz(matriz):
    """
    Função exclusivamente para mostrar a matriz de forma tabular para evitar possíveis códigos repetidos
    :param matriz: Matriz a ser printada de forma tabular
    :return: None
    """
    print('-' * 30)
    #percorrendo a matriz para manipular
    for indice, fileira in enumerate(matriz):
        print(indice, end=' = ')
        for chave, valor in fileira.items():
            #criando uma variável a ser mostrada para melhorar a experiência do usuario
            variavel = valor if valor != None else f'--{chave}--'
            print(f'| {variavel:^5} |', end='')
        print()
    print('-' * 30)


def valida_fileira(frase_de_pergunta):
    """
    função para válidar a posição de uma fileira tratando possivéis erros do usuário
    :param frase_de_pergunta: Frase que acompanha o input para direcionar o usuário
    :return: a posiçõa da fileira
    """
    #o laço só vai se quebrar se o usuário escolher uma fileira válida
    while True:
        #tratando o erro de digitação de um número não válido
        try:
            fileira = int(input(frase_de_pergunta))
            #tratando possivéis números não válidos de fileira
            if 2 >= fileira >= 0:
                break
            else:
                print('\033[31mDigite um número entre 0 e 2 para fileira!\033[m')
        #Caso o usuário não digite um número inteiro o sistema o alerta com uma mensagem
        except:
            print('\033[31mDigite um número inteiro válido para a fileira!\033[m')
    return fileira


def valida_coluna(frase_de_pergunta):
    """
    função para válidar a posição de uma coluna tratando possivéis erros do usuário
    :param frase_de_pergunta: Frase que acompanha o input para direcionar o usuário
    :return: a posiçõa da coluna
    """
    #o laço só vai se quebrar se o usuário escolher uma coluna válida
    while True:
        #tratando o erro de digitação de um número não válido
        try:
            coluna = int(input(frase_de_pergunta))
            #tratando possivéis números não válidos de coluna
            if 3 >= coluna >= 1:
                break
            else:
                print('\033[31mDigite um número entre 1 e 3 para coluna!\033[m')
        # Caso o usuário não digite um número inteiro o sistema o alerta com uma mensagem
        except:
            print('\033[31mDigite um número inteiro válido para a coluna!\033[m')
    return coluna


def valida_jogada(matriz, jogador):
    """
    Função para válidar se é possível concluir a jogada e diminuir mais a quantidade de códigos no arquivo principal
    :param matriz: matriz a ser analisada para a jogada
    :param jogador: jogador que fará a jogada X ou O
    :return: a fileira e a coluna após a conclusão de que é uma jogada válida
    """
    #o laço só vai se quebrar quando o usuário fizer uma jogada válida
    while True:
        #usando funções já criadas para auxiliar na semântica do código
        try:
            jogador_fileira = valida_fileira(f'Em qual fileira deseja jogar {jogador}? ')
            jogador_coluna = valida_coluna(f'em qual coluna deseja jogar {jogador}? ')
            #localizando dentro da matriz se a posição está disponível para a jogada
            if matriz[jogador_fileira][jogador_coluna] != None:
                #caso não esteja disponível o sistema dispara um except para avisar o usuário
                raise
            return jogador_fileira, jogador_coluna
        #imprimindo uma mensagem ao usuário sobre a jogada inválida
        except:
            print('\033[31mDigite uma posição válida dentro da matriz!\033[m')


def ganhou(matriz):
    """
    Função para localizar uma vitória dentro da matriz
    :param matriz: matriz a ser analisada
    :return: uma resposta booleana para ser tratada no código principal
    """
    #localizando possível vitória pela diagonal
    if matriz[0][1] == matriz[1][2] == matriz[2][3] != None:
        return True
    #localizando possível vitória pela diagonal
    elif matriz[0][3] == matriz[1][2] == matriz[2][1] != None:
        return True
    #percorrendo a matriz para análise
    for indice, fileira in enumerate(matriz):
        #localizando possível vitória pela fileira completa
        if fileira[1] == fileira[2] == fileira[3] != None:
            return True
        #localizando possível vitória pela coluna completa
        elif matriz[0][indice+1] == matriz[1][indice+1] == matriz[2][indice+1] != None:
            return True
    #retornando falso caso não tenha nenhuma vitória para disparar um retorno brevemente
    return False


def deu_velha(matriz):
    """
    função para analisar possivél empate
    :param matriz: matriz a ser análisada
    :return: uma resposta booleana para ser tratada no código principal
    """
    #percorrendo a matriz para analisar cada valor
    for fileira in matriz:
        for chave, valor in fileira.items():
            #caso ainda tenha um espaço vazio dentro da matriz o sistema chama um return false
            if valor == None:
                return False
    #caso todos os espaços foram preenchidos e o sistema não capturou uma possível vitória
    return True