def play():
    print("************************************")
    print("*****Bem vindo ao jogo de forca*****")
    print("************************************")

    secretWord = "nico".upper()
    correctLetters = []

    ## correctLetters = ["_" for letter in secretWord] - outro jeito de fazer
    for letter in secretWord:
        correctLetters.append("_")

    hanged = False
    hit = False
    errors = 0

    print(correctLetters)

    while (not hanged and not hit):
        attempt = input("Qual letra?").strip().upper()

        if (attempt in secretWord):
            index = 0
            for letter in secretWord:
                if (attempt == letter):
                    correctLetters[index] = letter
                index += 1
            print(correctLetters)
        else:
            errors += 1

        hit = "_" not in correctLetters
        hanged = errors == 6
        print(correctLetters)

        if (hit):
            print("Parabéns, você ganhou!")
        if (hanged):
            print("Você perdeu :(")


    print(f"Fim de jogo!")


if (__name__ == "__main__"):
    play()
