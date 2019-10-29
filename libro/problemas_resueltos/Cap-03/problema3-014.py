Zona1= float(input("\nIngresa el precio de la zona '1' del estadio: "))
Zona2= float(input("Costo-Zona '2' : "))
Zona3= float(input("Costo-Zona '3' : "))
Zona4= float(input("Costo-Zona '4' : "))
Zona5= float(input("Costo-Zona '5' : "))

precio = True

AP1= 0
AP2= 0
AP3= 0
AP4= 0
AP5= 0

RECAU= 0

while (precio == True):
    CLAVE= int(input("\nIngresa la zona del estadio: "))
    CANT= int(input("¿Cuántos bolestos?: "))
    if CLAVE == 1:
        PRE= Zona1*CANT
        AP1+= CANT
    if CLAVE == 2:
        PRE= Zona2*CANT
        AP2+= CANT
    if CLAVE == 3:
        PRE= Zona3*CANT
        AP3+= CANT
    if CLAVE == 4:
        PRE= Zona4*CANT
        AP4+= CANT
    if CLAVE == 5:
        PRE= Zona5*CANT
        AP5+= CANT
    print(f"El precio Para {CANT} boletos, en la zona {CLAVE}, es de: ${PRE} .")
    RECAU += PRE
    precio= bool(int(input("\nIngresa '1' para calcular otro precio, '0' para finalizar: ")))
print(f"\nTotal de boletos para la zona 1: {AP1} .")
print(f"Total de boletos para la zona 2: {AP2} .")
print(f"Total de boletos para la zona 3: {AP3} .")
print(f"Total de boletos para la zona 4: {AP4} .")
print(f"Total de boletos para la zona 5: {AP5} .")
print(f"\nRecuadacion total del estadio: ${RECAU} .")
print("-\nFinaliza el programa . ")
