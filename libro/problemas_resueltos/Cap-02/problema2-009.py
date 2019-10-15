precio= float(input("Ingresa el precio del producto: "))
total=0
if precio<20:
    print(f"\nPor: ${precio} no pagas impuesto .")
elif precio<40:
    total=(precio-20)*(.30)+precio
    print(f"\nPor: ${precio}, pagas impuesto del 30% dando un total de: ${total} ")
elif precio<500:
    total=(20*.30)+(precio-40)*(.40)+precio
    print(f"\nPor: ${precio}, pagas impuesto del 40% dando un total de: ${total} ")
else:
    total=(20*.30)+(precio-40)*(.50)+precio
    print(f"\nPor: ${precio}, pagas impuesto del 50% dando un total de: ${total} ")
print("\nPuedes pasar a pagar a la caja 7° .")
print("-\nFinaliza el programa .")
