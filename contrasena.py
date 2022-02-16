import random

def generador_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos= ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros #Concateno las listas 

    contrasena= []

    for i in range(8):
        caracter_random = random.choice(caracteres) #Elije un elemento aleatorio de una lista no vacia(caracteres)
        contrasena.append(caracter_random) #Agrego los caracteres random a la lista de contraseña vacia

    contrasena =  ''.join(contrasena) #convierte la lista en string
    return contrasena

def run():
    contrasena= generador_contrasena()
    print("Tu nueva contrasena es: " +  contrasena)


if __name__ == '__main__':
    run()