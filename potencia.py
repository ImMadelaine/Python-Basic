'''num = int(input("Ingresa un número para calcularle su potencia: "))
cont= 0

for x in range(num):
    potencia= num ** cont
    print(potencia)
    cont= cont + 1

    if num == cont:
        break'''

def run():
    LIMITE= 1000

    cont= 0 
    potencia = 2**cont
    
    while potencia < LIMITE:
        print(potencia)
        cont+= 1
        potencia= 2**cont


if __name__ == '__main__':
    run()