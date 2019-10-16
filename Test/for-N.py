a = int(input("Ingresa un número entero positivo: "))
cero=0
for v in range (1,a+1,1):
    b = int(input("Ingresa un número entero positivo: "))
    if b==0:
        cero += 1
print(f"En la lista anterio de numeros hay: {cero} ceros .")
