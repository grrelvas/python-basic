import random


def play():
    opening_message()

    secretWord = get_secretword()

    correctLetters = get_correctLetters(secretWord)

    hanged = False
    hit = False
    errors = 0

    print(correctLetters)

    while (not hanged and not hit):
        attempt = input("Qual letra?").strip().upper()

        if (attempt in secretWord):
            correctAttempt(secretWord, attempt, correctLetters)
        else:
            errors += 1

        hit = "_" not in correctLetters
        hanged = errors == 6
        print(correctLetters)

        if (hit):
            print("Parabéns, você ganhou!")
        if (hanged):
            print("Você perdeu :(")
            print("A palavra era: {}".format(secretWord))

    print(f"Fim de jogo!")


def opening_message():
    print("************************************")
    print("*****Bem vindo ao jogo de forca*****")
    print("************************************")


def get_secretword():
    words = []
    file = open("palavras.txt", "r")
    for line in file:
        line = line.strip()
        words.append(line)
    file.close()

    return words[random.randrange(0, len(words))].upper()


def get_correctLetters(secretWord):
    list = []
    ## correctLetters = ["_" for letter in secretWord] - outro jeito de fazer
    for letter in secretWord:
        list.append("_")
    return list


def correctAttempt(secretWord, attempt, correctLetters):
    index = 0
    for letter in secretWord:
        if (attempt == letter):
            correctLetters[index] = letter
        index += 1


if (__name__ == "__main__"):
    play()
