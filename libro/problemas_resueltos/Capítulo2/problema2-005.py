num=int(input("\nIngresa un número entero: "))
if num > 0:
    print(f"\n{num} es positivo.")
else:
    if num == 0:
        print(f"\n{num} es nulo.")
    else:
        if num < 0:
            print(f"\n{num} es negativo. ")
print("\nTermina el programa. ")
