NUM=int(input("\nInroduce un valor 'N' entero positivo, para la expresión  [1**1+2**2+3**3+...N**N] : "))

serie= 0

print("\n")

for sand in range (1,NUM+1,1):
    serie += (sand**sand)
    print(f" {sand}**{sand} = {sand**sand} ")

print(f"\nEl resultado de la suma de la serie anterior es: {serie} ")
print("-\nFinaliza el programa .")
