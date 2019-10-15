compra= float(input("\nIngresa el total de tu compra: "))
pagar= 0
if compra<500:
    print(f"\nNo se aplica descuento, debes pagar: ${compra} .")
elif compra<=1000:
    pagar= compra*.95
    print(f"\nSe aplica descuento de 5% debes pagar: ${pagar} .")
elif compra<=7000:
    pagar= compra*.89
    print(f"\nSe aplica descuento de 11% debes pagar: ${pagar} .")
elif compra<=15000:
    pagar= compra*.82
    print(f"\nSe aplica descuento de 18% debes pagar: ${pagar} .")
else:
    pagar= compra*.75
    print(f"\nSe aplica descuento de 25% debes pagar: ${pagar} .")
print("\nPuedes pasar a pagar a la caja, con efectivo o tarjeta .")
print(f"\nFinaliza el programa .")
