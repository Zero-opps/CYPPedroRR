SAND= 1.0
SUMPOS= 0.0
SUMNEG= 0.0
POST= 0.0

N= int(input("\nIngresa un número entero: "))

if N>1:
    print(f"\nSerie de {N} números enteros, para realizar las operaciones correspondientes.")
else:
    print("\nSe comienza el ingreso de un número entero, para realizar las operaciones correspondientes. ")

while(SAND<=N):
    NUM= int(input("Ingresa un número entero: "))
    if NUM>0:
        SUMPOS+=NUM
        POST+=1
        PROMPOS= SUMPOS/POST
    else:
        SUMNEG+=NUM
    SAND+=1

PROMPOS= SUMPOS/POST
PROMGEN= (SUMPOS+SUMNEG)/N

print(f"\nNúmeros positivos leídos: {POST}, promedio de estos: {PROMPOS} .") 
print(f"\nPromedio general de los números ingresados: {PROMGEN} .")
print(F"\nFinaliza el programa .")
