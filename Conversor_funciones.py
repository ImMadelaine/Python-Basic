def conversor(tipo_moneda, valor_dolar):
    pesos = float(input("Cuantos pesos "+ tipo_moneda + " tienes?: "))
    dolares = round((pesos/valor_dolar), 2)
    dolares= str(dolares)
    print("Tienes " + dolares + " dolares")


menu= """ 
    Bienvenido al conversor de monedas 💰

    1- Pesos Colombianos
    2- Pesos Argentinos
    3- Pesos Mexicanos

    Elegie una opcion: """

    #para poner emojis es windows +  punto
    
opcion= int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)

elif opcion ==2:
    conversor("Argentinos", 65)

elif opcion == 3:
    conversor("Mexicanos", 24)

else:
    print("Ingresa una opcion correecta por favor :)")