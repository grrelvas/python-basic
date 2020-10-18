import random

def play():
    print("********************************************************")
    print("Bem vindo ao jogo da adivinhação, número entre 1 e 100, você tem 7 tentativas.")
    print("********************************************************")

    print("Qual nivel de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    difficulty = int(input("Nível:"))

    totalPoints = 100

    if(difficulty == 1):
        totalAttempts = 7
    elif(difficulty == 2):
        totalAttempts = 5
    else:
        totalAttempts = 3

    # secretNumber = int(random.random()*100)
    secretNumber = random.randrange(1, 101)
    nailed = False

    for attempts in range(1, totalAttempts+1):
        userGuest = int(input("Digite o seu número: "))

        nailed = userGuest == secretNumber
        lesser = userGuest < secretNumber
        greater = userGuest > secretNumber

        if(userGuest < 1 or userGuest > 100):
            print("Número inválido")
            continue

        if(nailed):
            print(f"Você acertou! Você fez {totalPoints}")
            print("Fim de jogo!")
            break
        elif(greater):
            print("Seu chute foi maior que o número")
        elif(lesser):
            print("Seu chute foi menor que o número")

        lostPoints = abs(secretNumber - userGuest)
        totalPoints = totalPoints - lostPoints

        print(f"Você já tentou {attempts} vezes")

        if(attempts == totalAttempts):
            print(f"Fim de jogo! O número era {secretNumber}")

if(__name__ == "__main__"):
    play()