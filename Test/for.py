nomina=0
for v in range (1,11,1):
    sue= int(input("Ingresa el sueldo: "))
    nomina += sue
prom= nomina/10
print(f"La nomina de la empresa es: ${nomina} y el salario promedio es de: ${prom} .")
