Datos = int(input("\nIngresa tu fecha de nacimiento aa/mm/dd :  "))
print("\nIngresa tus cinco calificaciones del semestre: ")

a = float(input("\nPrimera calificación: "))
b = float(input("Segunda: "))
c = float(input("Tercera: "))
d = float(input("Cuarta: "))
e = float(input("Quinta: "))
Final = (a+b+c+d+e)/5

if Final >= 6:
    print(f"\nMatrícula: {Datos}CYP, tienes {Final} de promedio, estas aprobado. ")
else:
    print(f"\nMatrícula: {Datos}CYP, tienes {Final} de promedio, estás reprobado. ")

print("\nNo hay modificaciones a promedio final, finaliza la evaluación. ")
