from operator import le


def run():
    frase= input("Introduzca una frase: ")

    for letra in frase:
        print(letra.upper())



if __name__ == '__main__':
    run()