import random

print("********************************************************")
print("Bem vindo ao jogo da adivinhação, número entre 1 e 100, você tem 7 tentativas.")
print("********************************************************")

# secretNumber = int(random.random()*100)
secretNumber = random.randrange(1, 101)
nailed = False

while (nailed == False):
    userGuest = int(input("Digite o seu número: "))
    nailed = userGuest == secretNumber
    lesser = userGuest < secretNumber
    greater = userGuest > secretNumber

    if (userGuest < 1 or userGuest > 100):
        print("Número inválido")
        continue

    if (nailed):
        print("Você acertou!")
        print("Fim de jogo!")
        break
    elif (greater):
        print("Seu chute foi maior que o número")
    elif (lesser):
        print("Seu chute foi menor que o número")

    print(f"Você já tentou {attempts} vezes")

    if (attempts == 7):
        nailed = True

    if (attempts == 7):
        print(f"Fim de jogo! O número era {secretNumber}")

    attempts = attempts + 1
