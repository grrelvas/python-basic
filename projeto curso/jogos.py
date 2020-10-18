import forca
import adivinhacao

print("**************************")
print("*****Escolha seu jogo*****")
print("**************************")

print("(1) Forca, (2) Adivinhação")

userChoice = int(input("Qual jogo? "))

if(userChoice == 1):
    print("Forca será!")
    forca.play()
elif(userChoice == 2):
    print("Adivinhação será!")
    adivinhacao.play()

print("Fim de jogo!")
