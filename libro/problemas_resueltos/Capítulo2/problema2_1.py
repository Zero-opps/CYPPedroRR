Sonidos = int(input("¿El grillo hizo sonidos esta noche?: ( 0 No / 1 Sí):  "))
if Sonidos == True:
    emitidos = int(input("¿Cúantos sonidos emitió durante un minuto?: "))
    T = (emitidos/4) + 40
    print(f"La temperatura fué de: {T}°F .")
print("Fin del resultado")

