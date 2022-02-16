#------------------------------Conversor de monedas------------------------------------------

monedas = float(input("Cuantos pesos colombianos tienes?: "))
valor_dolar= 3875

dolares = round((monedas/valor_dolar), 2)
dolares= str(dolares)

print("Tienes " + dolares + " dolares")