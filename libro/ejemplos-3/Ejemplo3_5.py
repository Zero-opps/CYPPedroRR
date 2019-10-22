a=True
CUB=0
while (a==True):
    b= int(input("Ingresa un número: "))
    CUB= b**3
    print(f"El cubo de {b}, es: {CUB} ")
    a= bool(int(input("¿Quieres conocer el cubo de otro número? ( 1-sí, 0-no ): ")))
print("Finaliza el programa .")
