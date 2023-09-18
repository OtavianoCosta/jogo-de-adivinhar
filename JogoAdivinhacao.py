import random


def jogar():

    print("Bem vindos ou Jogo de Adivinha!")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    print("Qual dificuldade voce gostaria de jogar?", numero_secreto)
    print("(1) facil (2) Medio (3) Dificil")
    nivel = int(input("Digite a dificuldade que voce deseja jogar!!"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        chute = int(input("Tente adivinhar um numero de 1 a 100"))
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero de 1 a 100!!")
            continue
        if(chute == numero_secreto):
            print("Parabens voce acertou!!")
            break
        elif(chute < numero_secreto):
            print("O numero que voce chutou e menor que o numero secreto!!")
        elif(chute > numero_secreto):
            print("O numero que voce chutou e maior que o numero secreto!!")


    print("Fim do Jogo!!")

if(__name__ == "__main__"):
    jogar()




