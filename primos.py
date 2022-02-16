def es_primo(num):
    cont= 0
    
    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            cont+= 1
    if cont == 0:
        return False
    else:
        return True
    

def run():
    numero= int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")



if __name__ == '__main__':
    run()