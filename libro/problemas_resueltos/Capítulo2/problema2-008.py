compra= float(input("\nIngresa el total de tu compra: "))
pagar=0

if compra < 500:
    print(f"\nEl cliente debe pagar: ${compra}.")
elif compra <= 1000:
    pagar= compra*.95
    print(f"\nEl cliente debe pagar: ${pagar} .")
elif compra <= 7000:
    pagar= compra*.89
    print(f"\nEl cliente debe pagar: ${pagar} .")
else: 
    if compra <= 1500:
        pagar= compra*.82
        print(f"\nEl cliente debe pagar: ${pagar} .")
    else:
        pagar= compra*.75
        print(f"\nEl cliente debe pagar: ${pagar} .") 

print("\nFin del programa")
