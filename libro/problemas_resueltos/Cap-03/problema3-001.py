a=True
SUMPAR=0.0
CUEPAR=0.0
PROPAR=0.0
SUMIMP=0.0
while (a==True):
    NUM= int(input("Ingresa un número entero: "))
    if (-1)**NUM>0:
        CUEPAR+=1
        PROPAR=(PROPAR+NUM)/CUEPAR
    else:
        SUMIMP+=NUM
    a=bool(int(input("¿Agregas otro número? (1-sí, 2-no): ")))
print(f"Promedio de los números pares: {PROPAR} , suma de los impares: {SUMIMP} .")
