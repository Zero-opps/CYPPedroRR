A= int(input("\nIngresa un número: "))
B= int(input("Ingresa otro: "))
C= int(input("Ingresa otro: "))
print(f"\nA={A}\nB={B}\nC={C}")
if A>B:
    if A>C:
        print(f"\nA es el número mayor, con valor: {A} .")
    elif A==C:
        print(f"\nA y C son los números más grandes con valor: {a} .")
    else:
        print(f"\nC es el número mayor, con valor: {C} .")
elif A==B:
    if A>C:
        print(f"\nA y B son los números más grandes con valor: {B} .")
    elif A==C:
        print(f"\nA, B y C son iguales con valor: {B} .")
    else:
        print(f"\nC es el número mayor con valor: {C} .")
elif B>C:
    print(f"\nB es el número mayor con valor: {B} .")
elif B==C:
    print(f"\nB y C son ios números más grandes con valor: {C} .")
else:
    print(f"\nC es el número mayor, con valor: {C} .")
print("\nTermina análisis a los números .")

