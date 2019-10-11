tabla= float(input("\n ¿Cuál tabla de multiplicar?: "))
v=0
print(f"\nLa tabla de multiplicar del número {tabla} es: \n")
for v in range (-1,11,2):
    print(f"{tabla} x {v} = {tabla*v}")
print("\nFinaliza el programa .")
