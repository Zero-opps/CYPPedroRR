nip= int(input("\nIngresa la clave de larga distancia: "))
MIN= int(input("Ingresa los minutos de la llamada: "))
if nip==12:
    precio=MIN*2
    print(f"\n{nip}-Norteamérica, $2.00 por minuto, total a pagar: ${precio} .")
elif nip==15:
    precio=MIN*2.2
    print(f"\n{nip}-Centroamérica, $2.20 por minuto, total a pagar: ${precio} .")
elif nip==18:
    precio=MIN*4.5
    print(f"\n{nip}-Sudamérica, $4.50 por minuto, total a pagar: ${precio} .")
elif nip==19:
    precio=MIN*3.5
    print(f"\n{nip}-Europa, $3.50 por minuto, total a pagar: ${precio} .")
elif nip==23:
    precio=MIN*6
    print(f"\n{nip}-Asia, $6.00 por minuto, total a pagar: ${precio} .")
elif nip==25:
    precio=MIN*6
    print(f"\n{nip}-Asia, $6.00 por minuto, total a pagar: ${precio} .")
elif nip==29:
    precio=MIN*5
    print(f"\n{nip}-Oceanía, $5.00 por minuto, total a pagar: ${precio} .")
else:
    print("\nIngresa una clave de larga distancia válida .")
print("\nFin del análisis de la llamada .")
