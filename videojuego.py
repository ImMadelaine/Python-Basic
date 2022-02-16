import random

def run(): 
    rand= random.randint(1,100)
    num= int(input("Adivina el número del 1 al 100: "))
    
    while num != rand:
        if num < rand:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        num: int(input("Escoge otro número: "))
    print("Ganaste!")


if __name__ == '__main__':
    run()