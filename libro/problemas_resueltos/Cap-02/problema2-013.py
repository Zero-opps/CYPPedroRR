MAT= int(input("\nIngresa tu marícula: "))
CARR= str(input("Carrera (Mayúculas-sin acntos): "))
SEM= int(input("Semestre: "))
PROM= float(input("Promedio: "))
a='ECONOMIA'
b='COMPUTACION'
c='ADMINISTRACION'
d='CONTABILIDAD'
if CARR==a: 
    if SEM>=6 and PROM>=8.8:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, estás aceptado .")
    else:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, no estás aceptado .")
elif CARR==b:
    if SEM>6 and PROM>8.5:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, estás aceptado .")
    else:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, no estás aceptado .")
elif CARR==c:
    if SEM>5 and PROM>8.5:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, estás aceptado .")
    else:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, no estás aceptado .")
elif CARR==d:
    if SEM>5 and PROM>8.5:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, estás aceptado .")
    else:
        print(f"\nAlumno con matrícula: {MAT}, Carrera: {CARR}, no estás aceptado .")
else:
    print(f"\nIngresa datos válidos")
print("-\nFin del programa .")
