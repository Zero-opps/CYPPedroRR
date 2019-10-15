MAT= int(input("Ingresa tu matrícula: "))
CARR= str(input("Carrera (mayúculas-sin acentos): "))
SEM= int(input("Semestre: "))
PROM= float(input("Promedio: "))
#Git bash no identifica acentos
a='ECONOMIA'
if CARR==a:
      if SEM>=6 and PROM>=8.8:
            cost=10+17
            print(f"{cost} .")
      else:
            print("Datos no válidos .")
print("Finaliza el programa .")
