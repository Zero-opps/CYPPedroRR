compra= float(input("\nIngresa el total de tu compra: "))
pagar=0
if compra < 500:
    print(f"\nEl cliente debe pagar {compra}.")
else:
    if compra <= 1000:
        pagar= compra-(compra*.05)
        print(f"\nEl ciente debe pagar: ${pagar} .")
    else:
        if compra <= 7000:
            pagar= compra-(compra*.11)
            print(f"\nEl cliente debe pagar: ${pagar} .")
        else:
            if compra <= 1500:
                pagar= compra-(compra*.18)
                print(f"\n(El cliente debe pagar ${pagar} .")
            else:
                if compra >15000:
                    pagar= compra-(compra*.25)
                    print(f"\nEl cliente debe pagar ${pagar} .") 
print("Fin del programa")
