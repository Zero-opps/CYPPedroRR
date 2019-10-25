otra = True
suma = 0.0
cont = 0
while (otra == True):
    cal = float(input("Calificaciòn: "))
    cont+=1
    suma += cal
    otra = bool(int(input("Hay mas alumnos (0 No, 1): ")))
print("Suma:",suma)
print("Promedio:",suma/cont)
print("Fin del programa")
