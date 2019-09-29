SUE=float(input("Ingresa tu sueldo actual: "))
if SUE < 1000:
    N_SUE= (SUE) * (1.15)
    print(f"Su nuevo sueldo es: ${N_SUE} ")
else:
    N_SUE= SUE*1.12
    print(f"Su nuevo sueldo es: ${N_SUE} ")
print("Se termina modificación al sueldo")
