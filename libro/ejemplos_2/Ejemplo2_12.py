A=int(input("Ingresa un numero entero: "))
B=int(input("Ingresa un numero entero: "))
C=int(input("Ingresa un numero entero: "))
if A > B:
    if A > C:
            if B > C:
                print(f"{A} > {B} > {C}")
            else:
                print(f"{A} > {C} > {B}")
    else:
        print (f"c")
else:
        if B > C:
                if A > C:
                    print(f"{B} {A} {C}")
                else:
                    print(f"{B} {C} {A}")
        else:
            print(f" {C} {B} {A}")

print("Fin del programa")

            

        
