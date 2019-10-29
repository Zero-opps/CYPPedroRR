N= int(input("\n¿Cuántos empleados tiene la empresa?: "))

MANUM= 0
SUEmayor= 0

print("\n")
for i in range (1,N,1):
    NUMEMP= int(input("Número-Empleado: "))
    SUE= float(input("Sueldo-Empleado: "))

    if SUE > SUEmayor:
        MANUM=NUMEMP
        SUEmayor=SUE

print(f"\nEl empleado número: {MANUM}, tiene el mayor sueldo con: ${SUEmayor} .")
print("-\nFinaliza el programa .")
