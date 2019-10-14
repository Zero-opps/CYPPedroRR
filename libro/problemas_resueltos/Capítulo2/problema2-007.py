A=int(input("\nIngresa un número entero: "))
B=int(input("Ingresa un número entero: "))
C=int(input("Ingresa un número entero: "))

if A<B:
    if B<C:
        print("\nLos numeros están en orden creciente.")
        print(f"{A} < {B} < {C} .")
    else:
        print("\nLos números no están en orden creciente")
else:
    print("\nLos números no están en orden creciente")

print("-\nFin del programa .")
