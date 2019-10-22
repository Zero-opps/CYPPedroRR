sand=1

N= int(input("¿Cuántas ventas realizaste?: "))
CHICA=0
MED=0
GRANDE=0

while (sand<=N):
    venta=float(input("Ingresa el monto de la venta: "))
    if venta<=200:
        CHICA+=1
    elif venta<400:
        MED+=1
    else:
        GRANDE+=1
    sand+=1
print("\nRecuento de ventas finalizado .")
print(f"\nTotal de ventas correspondiente a cada rango de monto: \n{CHICA} <= $200.00 \n$200.00 < {MED} < $400.00 \n{GRANDE} > $400.00 ")
print("\nFinaliza el programa .")
