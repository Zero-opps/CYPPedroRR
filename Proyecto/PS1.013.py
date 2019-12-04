print("\nIngresa los siguientes datos de un prisma pentagonal en centímetros:") # la unidad de cm es opccional

PER=float(input("\n  Perímetro de la base : "))
APO=float(input("  Apotema : "))
ALT=float(input("  Altura : "))

AB=(PER*APO)/2
AL=PER*ALT
AT=2*AB+AL
VOL=AB*ALT

print("\nLos resultados del prisma pentagonal son:")
print(f"\n    Área de la base: {AB} cm\u00b2 ")
print(f"    Área lateral: {AL}cm cm\u00b2")
print(f"    Área total: {AT}cm cm\u00b2")
print(f"    Volumen: {VOL} cm\u00b3 ")

print("-\nFinaliza el programa.")
