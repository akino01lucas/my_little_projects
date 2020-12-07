from random import randint
from time import sleep

num_sorteados = list()
participantes = list()

def apresentacao():
    print('===== TELE SENA FDS ===== \n')
    sleep(0.7)
    print(f'SERÃO SORTEADOS 5 NÚMEROS;\n')
    sleep(1.2)
    print('APENAS NÚMEROS DE 1 A 30;\n')
    sleep(1.2)
    print('BOA SORTE AE!\n')
    sleep(1.5)


def sorteio():
    """
    Sorteio realizado utilizando a função randint(), que aplica 5 números de 1 a 30.
    """
    cont = 1
    while cont <= 5:
        ok = False
        num = randint(1, 30)
        while True:
            if num not in num_sorteados:
                num_sorteados.append(num)
                cont += 1
                ok = True
            else:
                num = randint(1, 30)
            if ok:
                break
    print('\n\nOS NÚMEROS SORTEADOS FORAM:')
    for n in num_sorteados:
        print(f'{n} ', end='')
        sleep(2)

def jogo():
    """
    Função que aplica os nomes e números dos participantes a dicionários dentro da lista chamada "participantes".
    """
    n_de_pessoas = int(input('Quantas pessoas irão jogar? '))
    for j in range(1, n_de_pessoas + 1):
        nome = str(input(f'NOME DO JOGADOR {j}: '))
        dic = {'Nome': nome, 'Números': list()}
        participantes.append(dic)

    cont = 1
    for n in range(len(participantes)):
        for quant in range(1, 6):
            ok = False
            valor = 0
            while True:
                num = str(input(f'Informe o {quant}º número do JOGADOR {cont}: '))
                if num.isnumeric():
                    valor = int(num)
                    if 0 < valor < 31 and valor not in participantes[n]['Números']:
                        participantes[n]['Números'].append(valor)
                        ok = True
                    else:
                        print('\033[0;31mERRO! Número inválido\033[m')
                else:
                    print('\033[0;31mERRO! Número inválido\033[m')
                if ok:
                    break
        cont += 1
        sleep(1.5)
        print('\n')
    sorteio()

def resultado():
    """
    Gera o resultado do sorteio, aplicando os números solicitados dos participantes que são compativeis
    com os números sorteados pelo programa.
    :return: Números do jogadores, os números que o jogador conseguiu acertar e o nome do vencedor.
    """
    numeros_certos = list()
    for p in range(len(participantes)):
        jogador = participantes[p]['Nome']
        numeros = participantes[p]['Números']
        print(f'\nNúmeros do(a) \033[0;31m{jogador}\033[m: {numeros}')
        sleep(1.5)
        dic = {'Nome': jogador, 'Números': list()}
        numeros_certos.append(dic)
        for n in participantes[p]['Números']:
            if n in num_sorteados:
                numeros_certos[p]['Números'].append(n)
            else:
                pass
    sleep(1)

    for p in range(len(numeros_certos)):
        jogador = numeros_certos[p]['Nome']
        numeros = numeros_certos[p]['Números']
        if len(numeros_certos[p]['Números']) > 0:
            print(f'\nO jogador(a) \033[0;31m{jogador}\033[m acertou os números: {numeros}')
            sleep(1.5)
        else:
            print(f'\nO jogador {jogador} \033[0;31mERROU TUDO KKKKKK\033[m')
            sleep(1.5)

    vencedor = max(numeros_certos, key=lambda numero: len(numero['Números']))['Nome']
    if len(numeros_certos) > 1:
        print(f'\nE O VENCEDOR FOI: \033[0;31m{vencedor}\033[m!! Parabéns ae.')
    else:
        if len(numeros_certos[0]['Números']) > 0:
            print('Bem jogado campeão... valeu.')
        else:
            print('\033[0;31mGame Over\033[m')

apresentacao()
jogo()
resultado()






