a= True
total=0.0
while (a==True):
    gasto= float(input("Ingresa tu gasto: "))
    total += gasto
    a = bool(int(input("¿Tienes algun otro gasto? (1 Si, 2 No): ")))
print(f"Tus gastos totales son: ${total} .")
