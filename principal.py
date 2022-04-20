from Jogo_Da_Velha.modularizacao import mostra_matriz, valida_jogada, deu_velha, ganhou
from time import sleep

        #1        #2        #3
a = {1: None, 2: None, 3: None} #0
b = {1: None, 2: None, 3: None} #1
c = {1: None, 2: None, 3: None} #2
matriz = [a, b, c]
#criando um laço com duração indefinida que só sera quebrado com uma vitória ou empate
while True:
    mostra_matriz(matriz)
    filiera_O, coluna_O = valida_jogada(matriz, '\033[33mO\033[m')
    matriz[filiera_O][coluna_O] = 'O'
    sleep(1)
    #usando as funções ganhou e deu_velha para quebrar o while ou não
    if ganhou(matriz):
        ganhador = '\033[33mO\033[m'
        break
    else:
        if deu_velha(matriz):
            break
    mostra_matriz(matriz)
    fileira_X, coluna_X = valida_jogada(matriz, '\033[34mX\033[m')
    matriz[fileira_X][coluna_X] = 'X'
    sleep(1)
    #usando as funções ganhou e deu_velha para quebrar o while ou não
    if ganhou(matriz):
        ganhador = '\033[34mX\033[m'
        break
    else:
        if deu_velha(matriz):
            break
#mostrando uma última vez a matriz com o resultado final
mostra_matriz(matriz)
#definindo que mensagem mostrar ao usuário com base no resultado admitido pelas funções ganhou e deu_velha
if deu_velha(matriz):
    print('\033[32mO JOGO DEU VELHA! NINGUEM GANHOU!!!\033[m')
else:
    print(f'O JOGADOR {ganhador} GANHOU!!!')

