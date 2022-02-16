'''def run():
    for cont in range(1, 50):
       if (cont%2) != 0:
           continue
    print(cont)


if __name__ == '__main__':
    run() '''


def run():
    for cont in range(100):
        print(cont)
        if cont == 50:
            break



if __name__ == '__main__':
    run()