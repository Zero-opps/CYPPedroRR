otra= True
suma= 0.0
while (otra == True):
    cal = float(input("Calificaciòn: "))
    suma += cal
    otra = bool(int(input("Hay mas alumnos (0 No, 1): ")))
print("Suma",suma)
print("Fin del programa")
