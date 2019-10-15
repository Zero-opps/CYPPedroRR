MAT= int(input("Ingresa tu marícula: "))
CARR= str(input("Carrera (Mayúculas-acntos): "))
SEM= int(input("Semestre: "))
PROM= float(input("Promedio: "))
a='ECONOMIA'
if CARR==a: 
    if SEM>=6 and PROM>=8.8:
        print(f"Alumno con matrícula: {MAT}, Carrera: {CARR}, estás aceptado .")
    else:
        print(f"Alumno con matrícula: {MAT}, Carrera: {CARR}, no estás aceptado .")
else:
    print(f"Ingresa datos válidos")
print("Fin del programa .")
