sand=1
MAYOR= -100000
MENOR=  100000

N=int(input("\nIngresa la cantidad de cifras, para la serie: "))
while (sand<=N):
    NUM= int(input("Ingresa un número entero: "))
    if NUM>MAYOR:
        MAYOR=NUM
    if NUM<MENOR:
        MENOR=NUM
    sand+=1
print(f"\nDe la serie anterior, el número mayor es: {MAYOR}, y el menor es: {MENOR} .")
print("-\nFinaliza el programa .")
