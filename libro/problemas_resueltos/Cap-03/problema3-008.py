NUM= int(input("\nIngresa un número entero positivo: "))

if NUM>0:
    print(f"\nEl resultado de la conjetura de ULAM en el número {NUM}, es: ")

    while (NUM!=1):
        print(f"\n{NUM}")
        if (-1)**NUM>0:
            print(f"{NUM}/2 = {NUM/2} ")
            NUM/=2
        else:
            print(f"({NUM}*3)+1= {NUM*3+1} ")
            NUM=(NUM*3)+1
            
    print(f"\nEl resultado final de la serie es: '1' .")      

else:
    print("\nIngresa un número válido. ")

print("-\nFinaliza el programa .")
