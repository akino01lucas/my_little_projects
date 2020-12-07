from random import randint
from time import sleep
pergunta = 'Qual é seu palpite? '

def adivinha(palpite):
    """
    Jogo da adivinhação
    :param palpite: o jogador irá adivinhar qual número de 1 a 10 o programa escolheu aleatoriomente.
    :return: a função irá retornar se o jogador acertou. Caso não acerte, a função retorna a opção de palpite
    até o acerto, dando dicas.
    """
    print('Sou seu computador...\n'
          'Acabei de pensar em um número entre 0 e 10.\n'
          'Será que você consegue adivinhar qual foi?')
    num_comp = randint(1, 10)  # Número aleatório a ser adivinhado.
    tentativas = 1
    ok = False
    while True:
        try:
            palpite = int(input(pergunta))
            if palpite == num_comp:
                return 'Acertou com {} tentativa(s). Parabéns!'.format(tentativas)
                ok = True
            elif palpite < num_comp:
                print('Mais... Tente novamente:')
                tentativas += 1
            elif palpite > num_comp:
                print('Menos... Tente novamente:')
                tentativas += 1
            if ok:
                break
        except:
            print('Digita um número aí poxa...')
            sleep(0.5)

print(adivinha(pergunta))















